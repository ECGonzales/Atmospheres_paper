import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import emcee
import pdb  # Use pdb.set_trace() to put a stop in the code like idl
import corner

# Set as stop for debugging
stop = pdb.set_trace  # stop() to run

# -------- Read in the data --------
df_sub = pd.read_csv('Data/Subdwarf_Spt_vs_Teff_new.txt', sep="\s+", comment='#', header=None,
                     names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ', 'MJ_unc',
                            'MH', 'MH_unc', 'MK', 'MK_unc', 'MW1', 'MW1_unc', 'MW2', 'MW2_unc'])

df_field = pd.read_csv('Data/Parallaxes-Normal_modified.txt', sep="\t", comment='#', header=0,
                       names=['name', 'spt', 'Pi', 'Pi_er', 'Jmagn_MKO', 'Jerr_MKO', 'Hmagn_MKO', 'Herr_MKO',
                              'Kmagn_MKO', 'Kerr_MKO', 'W1magn', 'W1err', 'W2magn', 'W2err', 'W3magn', 'W3err',
                              'W4magn', 'W4err', 'Jmagn', 'Jerr', 'Hmagn', 'Herr', 'Kmagn', 'Kerr', 'Lmag', 'Lerr'])

df_young = pd.read_csv('Data/For-CMD-NEW-NEW.txt', sep='\t', comment="#", header=0,
                       names=['Grp', 'ID', 'SpT', 'lowg', 'Jmag', 'Jerr', 'H', 'Herr', 'K', 'Kerr', 'W1', 'W1er', 'W2',
                              'W2er', 'W3', 'W3er', 'W4', 'W4er', 'PI', 'Pier', 'MKOJ', 'MKOJer', 'MKOH', 'MKOHer',
                              'MKOK', 'MKOKer', 'Lband', 'Lbander'])

# ------------ remove -100s from Dataframe ---------
df_field = df_field[df_field['Kmagn'] > -100]

# -------------------------------------------------------------------------------------
# ------------------- Get abs Mag from relative mag -----------------------------------
# -------------------------------------------------------------------------------------
# --- Get Distance: Field ---
d = np.round(1000/(df_field['Pi']), 2)  # 1000/mas or 1/arcsec round to 2 decimal points
d_err = np.round((df_field['Pi_er']/(df_field['Pi']**2))*1000, 2)  # convert to arcsec from mas

# ------ Convert apparent mag to Abs Mag: Field -------
AbsK = np.round(df_field['Kmagn']-(5*np.log10(d)-5), 3)
AbsK_err = np.round(np.sqrt(df_field['Kerr'] ** 2 + 25 * (d_err/(d * np.log(10))) ** 2), 3)
df_field['AbsK'] = AbsK
df_field['AbsK_err'] = AbsK_err

# --- Get Distance: Young ---
dy = np.round(1000/(df_young['PI']), 2)  # 1000/mas or 1/arcsec round to 2 decimal points
dy_err = np.round((df_young['Pier']/(df_young['PI']**2))*1000, 2)  # convert to arcsec from mas

# ------ Convert apparent mag to Abs Mag: Young -------
AbsKy = np.round(df_young['K']-(5*np.log10(dy)-5), 3)
AbsKy_err = np.round(np.sqrt(df_young['Kerr'] ** 2 + 25 * (dy_err/(dy * np.log(10))) ** 2), 3)
df_young['AbsK'] = AbsKy
df_young['AbsK_err'] = AbsKy_err

# -------------------------------------------------------------------------------------
# ------------------------- Polynomial fits  -----------------------------------------
# -------------------------------------------------------------------------------------
# ------ Fit polynomial for subdwarfs ------
# Need to drop nans
df_sub2 = df_sub.drop(df_sub.index[2])

# --- Get uncertainites for upper and lower teff limits ----
df_sub2['AbsK_up'] = df_sub2['MK'] + df_sub2['MK_unc']
df_sub2['AbsK_d'] = df_sub2['MK'] - df_sub2['MK_unc']

# ------ Fit the values --------
coeffs = np.polyfit(df_sub2['SpT'], df_sub2['MK'], 1)
line = np.poly1d(coeffs)

coeffs_up = np.polyfit(df_sub2['SpT'], df_sub2['AbsK_up'], 1)
line_up = np.poly1d(coeffs_up)

coeffs_d = np.polyfit(df_sub2['SpT'], df_sub2['AbsK_d'], 1)
line_d = np.poly1d(coeffs_d)

# ---- print values to screen -------
print coeffs
print coeffs_up
print coeffs_d

# ---- Plot the fit lines -----
# xp = np.linspace(5, 30, 100)

# define the uncertainty range based on the values from the calcuated uncertainties on the coeffs. (See my table)
# fit = 0.328*xp + 7.363
# up = 0.348*xp + 7.426
# down = 0.308*xp + 7.30
#
# plt.plot(xp, fit, color='k')
# plt.plot(xp, up, color='#17becf', alpha=.25)
# plt.plot(xp, down, color='#17becf', alpha=.25)
# ax1.fill_between(xp, up, down, alpha=.25, color='#17becf')

# -------------------------------------------------------------------------------------
# ------------------------------ Use emcee to fit instead -----------------------------
# -------------------------------------------------------------------------------------

# Define the likelihood function: a line y=mx+b


def lnprob(x, MK, MK_unc, spt):
    if x[2] < 0:
        return -np.inf
    model_line = x[0]*spt + x[1]
    sigma_dm = (MK - model_line)/np.sqrt(MK_unc**2+x[2]**2)  # Distance between the data points and the model line
    return -(1./2.)*sum(np.log(x[2]**2+MK_unc**2))-(1./2.)*sum(sigma_dm**2)-np.log(x[2])  # np.log(x[2]) is an uninformative prior on the intrinsic dispersion
                                                    # It favors large numbers less

# Define the parameters we need to imput into the mcmc
ndim = 3  # Number of parameters in my lnprob after the x
nwalkers = 12
nsteps = 1000  # this is a standard starting point of 1000

parm_est = [0.326, 7.381, 0]  # This is my estimate on the slope and y-intercept from my polyfits
parm_scale = [0.033, 0.74, 0.74]  # the scatter about my estimated start points 10%
parm_scale_2d = np.array(parm_scale).reshape(1, ndim).repeat(nwalkers, axis=0)  # Create a 2D array of values with
parm_est_2d = np.array(parm_est).reshape(1, ndim).repeat(nwalkers, axis=0)      # nwalkers rows
pos = parm_est_2d + np.random.rand(nwalkers, ndim)*parm_scale_2d


# Start the mcmc add .values to the pandas dataframe to convert to numpy array
# Use the df_subpoly array that has removed the nans before can rum the mcmc
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(df_sub2['MK'].values,
                                                              df_sub2['MK_unc'].values, df_sub2['SpT'].values))
sampler.run_mcmc(pos, nsteps)

# Check what the burn in is so it can be thrown out
labels = ["slope", "intercept", 'dispersion']
for k in range(ndim):
    plt.figure()
    for n in range(nwalkers):
        plt.plot(sampler.chain[n,:,k])
    plt.ylabel(labels[k], fontsize='16')
    plt.xlabel("step number", fontsize='12')

# Burn in was around 50 steps, so drop 200 to be safe them from the chain
samples = sampler.chain[:, 200:, :].reshape((-1, ndim))

# Check the corner plot of the chain
figcheck = corner.corner(samples, labels=["$m$", "$b$",'dispersion'])

# -------------------------------------------------------------------------------------
# ------------------------- Make Plot: Spt v Abs Mags K---------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([5, 18.5])
plt.ylim([17, 7.5])

# ------ Axes Labels --------
plt.xticks([6, 8, 10, 12, 14, 16, 18], ['M6', 'M8', 'L0', 'L2', 'L4', 'L6', 'L8'], fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Spectral Type', fontsize=25)
plt.ylabel('$M_K$ (2MASS)', fontsize=25)

# ----- Add data -----
fld = plt.scatter(df_field['spt'], df_field['AbsK'], color='#7C7D70')
ax1.errorbar(df_field['spt'], df_field['AbsK'], yerr=df_field['AbsK_err'], c='#7C7D70', fmt='o')
young = plt.scatter(df_young['SpT'], df_young['AbsK'], color='#D01810')
ax1.errorbar(df_young['SpT'], df_young['AbsK'], yerr=df_young['AbsK_err'], c='#D01810', fmt='o')
sub = plt.scatter(df_sub['SpT'], df_sub['MK'], color='blue', s=100, zorder=5)
ax1.errorbar(df_sub['SpT'], df_sub['MK'], yerr=df_sub['MK_unc'], c='blue', fmt='o', zorder=6)

# --- Designate 1256-0224 -----
plt.scatter(df_sub['SpT'][0], df_sub['MK'][0], color='blue', s=500, zorder=7, marker="*")
ax1.annotate('J1256-0224', xy=(12.7, 13), color='k', fontsize=12)

# ---- Add Legend ----
plt.legend([fld, young, sub], ["Field", "Young", 'Subdwarf'], frameon=False, fontsize=12)

# ---- Plot fit lines  from the mcmc, random 100 -----
xl = np.array([0, 20])
for x in samples[np.random.randint(len(samples), size=500)]:
    plt.plot(xl, x[0]*xl+x[1], color="#17becf", alpha=0.05, zorder=1)

# To get the best fit line
best_fit_coeffs = np.median(samples, axis=0)
best_fit_line = best_fit_coeffs[0]*xl + best_fit_coeffs[1]
plt.plot(xl, best_fit_line, c='k', zorder=8)

# ---- Print the best fit coeffs and the std -----
print(best_fit_coeffs)
print(np.std(samples, axis=0))

plt.tight_layout()
plt.savefig('Plots/MKvspt.pdf', dpi=150)
