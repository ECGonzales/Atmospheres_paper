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
df_comb = pd.read_csv('Data/Lbol+Teff-February2017_updated.txt', sep="\s+", comment='#', header=None,
                      names=["name", "Lbol", "Lbol_err", 'Teff', 'Teff_err', 'spt', 'spt_unc', 'group', 'grav'])

# ----- Remove the -100 -----------------
# df_comb.loc[df_comb['grav'] == -100]
df_comb.set_value(174, 'grav', 3)

# ---- Split combined dataframe into field (group 3) and low g groups 1,2) ----------
df_fld = df_comb[(df_comb['grav'] == 3)]
df_young = df_comb[(df_comb['grav'] >= 1) & (df_comb['grav'] <= 2)]

# -------------------------------------------------------------------------------------
# ------------------------- Polynomial fits  -----------------------------------------
# -------------------------------------------------------------------------------------
# ------ Fit polynomial for subdwarfs ------
# drop nan from column need to get polynomial
df_subpoly = df_sub[pd.notnull(df_sub['lbol'])]

# --- Get uncertainites for upper and lower teff limits ----
df_subpoly['Lbol_up'] = df_subpoly['lbol'] + df_subpoly['lbol_err']
df_subpoly['Lbol_d'] = df_subpoly['lbol'] - df_subpoly['lbol_err']

# ------ Fit the values --------
coeffs = np.polyfit(df_subpoly['SpT'], df_subpoly['lbol'], 1)
line = np.poly1d(coeffs)

coeffs_up = np.polyfit(df_subpoly['SpT'], df_subpoly['Lbol_up'], 1)
line_up = np.poly1d(coeffs_up)

coeffs_d = np.polyfit(df_subpoly['SpT'], df_subpoly['Lbol_d'], 1)
line_d = np.poly1d(coeffs_d)

# ---- print values to screen -------
print coeffs
print coeffs_up
print coeffs_d

# ---- Plot the fit lines -----
# xp = np.linspace(5, 30, 100)
# plt.plot(xp, line(xp), '-', color='k')
# plt.plot(xp, line_up(xp), '-', color='#17becf', alpha=.25)
# plt.plot(xp, line_d(xp), '-', color='#17becf', alpha=.25)
# ax1.fill_between(xp, line_up(xp), line_d(xp), alpha=.25, color='#17becf')

# -------------------------------------------------------------------------------------
# ------------------------------ Use emcee to fit instead -----------------------------
# -------------------------------------------------------------------------------------

# Define the likelihood function: a line y=mx+b


def lnprob(x, lbol, lbol_err, spt):
    if x[2] < 0:
        return -np.inf
    model_line = x[0]*spt + x[1]
    sigma_dm = (lbol - model_line)/np.sqrt(lbol_err**2+x[2]**2)  # Distance between the data points and the model line
    return -(1./2.)*sum(np.log(x[2]**2+lbol_err**2))-(1./2.)*sum(sigma_dm**2)-np.log(x[2])  # np.log(x[2]) is an uninformative prior on the intrinsic dispersion
                                                    # It favors large numbers less

# Define the parameters we need to imput into the mcmc
ndim = 3  # Number of parameters in my lnprob after the x
nwalkers = 12
nsteps = 1000  # this is a standard starting point of 1000

parm_est = [-0.124, -2.089, 0]  # This is my estimate on the slope and y-intercept from my polyfits
parm_scale = [0.012, 0.21, 0.21]  # the scatter about my estimated start points 10% for teff, 500 Degrees for K
parm_scale_2d = np.array(parm_scale).reshape(1, ndim).repeat(nwalkers, axis=0)  # Create a 2D array of values with
parm_est_2d = np.array(parm_est).reshape(1, ndim).repeat(nwalkers, axis=0)      # nwalkers rows
pos = parm_est_2d + np.random.rand(nwalkers, ndim)*parm_scale_2d


# Start the mcmc add .values to the pandas dataframe to convert to numpy array
# Use the df_subpoly array that has removed the nans before can rum the mcmc
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(df_subpoly['lbol'].values,
                                                              df_subpoly['lbol_err'].values,df_subpoly['SpT'].values))
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
# ------------------------- Make Plot: Spt v Teff ------------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
plt.xlim([5.5, 18.5])
plt.ylim([-5, -2.3])

# ------ Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xticks([6, 8, 10, 12, 14, 16, 18], ['M6','M8', 'L0', 'L2', 'L4', 'L6', 'L8'], fontsize=20)
plt.xlabel('Spectral Type', fontsize=25)
plt.ylabel('log($L_\mathrm{bol}$/$L_\odot$)', fontsize=25)

# ------- Add Data ------
fld = plt.scatter(df_fld['spt'], df_fld['Lbol'], color='#7C7D70')
ax1.errorbar(df_fld['spt'], df_fld['Lbol'], yerr=df_fld['Lbol_err'], c='#7C7D70', fmt='o')
young = plt.scatter(df_young['spt'], df_young['Lbol'], color='#D01810')
ax1.errorbar(df_young['spt'], df_young['Lbol'], yerr=df_young['Lbol_err'], c='#D01810', fmt='o')
sub = plt.scatter(df_sub['SpT'], df_sub['lbol'], color='blue', s=100, zorder=5)
ax1.errorbar(df_sub['SpT'], df_sub['lbol'], yerr=df_sub['lbol_err'], c='blue', fmt='o', zorder=6)

# --- Designate 1256-0224 -----
plt.scatter(df_sub['SpT'][0], df_sub['lbol'][0], color='blue', s=500, zorder=7, marker="*")
ax1.annotate('J1256-0224', xy=(12.7, -3.4), color='k', fontsize=12)

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
plt.savefig('Plots/SptvLbol.pdf',dpi=150)
