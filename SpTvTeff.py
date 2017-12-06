import pandas as pd
import matplotlib.pyplot as plt
import emcee
import numpy as np
import pdb  # Use pdb.set_trace() to put a stop in the code like idl
import corner


# Set as stop for debugging
stop = pdb.set_trace  # stop() to run

# ---------- Read in the data -------------
df_sub = pd.read_csv('Data/Subdwarf_Spt_v_Teff.txt', sep="\s+", comment='#', header=None,
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
# ------ Fit polynomial for subdwarfs, use this as starting point for the emcee ------
# drop nan from column need to get polynomial
df_subpoly = df_sub[pd.notnull(df_sub['Teff'])]

# --- Get uncertainites for upper and lower teff limits ----
df_subpoly['Terr_up'] = df_subpoly['Teff'] + df_subpoly['Teff_err']
df_subpoly['Terr_d'] = df_subpoly['Teff'] - df_subpoly['Teff_err']

# ------ Fit the values --------
coeffs = np.polyfit(df_subpoly['SpT'], df_subpoly['Teff'], 1)
line = np.poly1d(coeffs)

coeffs_up = np.polyfit(df_subpoly['SpT'], df_subpoly['Terr_up'], 1)
line_up = np.poly1d(coeffs_up)

coeffs_d = np.polyfit(df_subpoly['SpT'], df_subpoly['Terr_d'], 1)
line_d = np.poly1d(coeffs_d)

# ---- print values to screen to use for emcee -------
print coeffs
print coeffs_up
print coeffs_d

# -----Plotting (not correct values, from W1 for example)
# xp = np.linspace(5, 30, 100)
#
# # define the uncertainty range based on the values from the calcuated uncertainties on the coeffs. (See my table)
# fit = 0.266*xp + 7.270
# up = 0.323*xp + 7.648
# down = 0.209*xp + 6.892
#
# plt.plot(xp, fit, color='k')
# plt.plot(xp, up, color='#17becf', alpha=.25)
# plt.plot(xp, down, color='#17becf', alpha=.25)
# ax1.fill_between(xp, up, down, alpha=.25, color='#17becf')

# -------------------------------------------------------------------------------------
# ------------------------------ Use emcee to fit instead -----------------------------
# -------------------------------------------------------------------------------------

# Define the likelihood function: a line y=mx+b


def lnprob(x, teff, teff_err, spt):
    if x[2] < 0:
        return -np.inf
    model_line = x[0]*spt + x[1]
    sigma_dm = (teff - model_line)/np.sqrt(teff_err**2+x[2]**2)  # Distance between the data points and the model line
    return -(1./2.)*sum(np.log(x[2]**2+teff_err**2))-(1./2.)*sum(sigma_dm**2)-np.log(x[2])  # np.log(x[2]) is an uninformative prior on the intrinsic dispersion
                                                    # It favors large numbers less

# Define the parameters we need to imput into the mcmc
ndim = 3  # Number of parameters in my lnprob after the x
nwalkers = 12
nsteps = 1000  # this is a standard starting point of 1000

parm_est = [-120, 4000, 0]  # This is my estimate on the slope and y-intercept from my polyfits
parm_scale = [12, 500, 100]  # the scatter about my estimated start points 10% for teff, 500 Degrees for K
parm_scale_2d = np.array(parm_scale).reshape(1, ndim).repeat(nwalkers, axis=0)  # Create a 2D array of values with
parm_est_2d = np.array(parm_est).reshape(1, ndim).repeat(nwalkers, axis=0)      # nwalkers rows
pos = parm_est_2d + np.random.rand(nwalkers, ndim)*parm_scale_2d


# Start the mcmc add .values to the pandas dataframe to convert to numpy array
# Use the df_subpoly array that has removed the nans before can rum the mcmc
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(df_subpoly['Teff'].values,
                                                              df_subpoly['Teff_err'].values,df_subpoly['SpT'].values))
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
# ------------------------- Make Plot: Spt v Teff -------------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([5.5, 18.5])
plt.ylim([900, 3200])

# ------ Axes Labels --------
plt.xticks([6, 8, 10, 12, 14, 16, 18], ['M6','M8', 'L0', 'L2', 'L4', 'L6', 'L8'], fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Spectral Type', fontsize=25)
plt.ylabel('$T_\mathrm{eff}$ (K)', fontsize=25)

# ------- Add Data ------
fld = plt.scatter(df_fld['spt'], df_fld['Teff'], color='#7C7D70')
ax1.errorbar(df_fld['spt'], df_fld['Teff'], yerr=df_fld['Teff_err'], c='#7C7D70', fmt='o')
young = plt.scatter(df_young['spt'], df_young['Teff'], color='#D01810')
ax1.errorbar(df_young['spt'], df_young['Teff'], yerr=df_young['Teff_err'], c='#D01810', fmt='o')
sub = plt.scatter(df_sub['SpT'], df_sub['Teff'], color='blue', s=100, zorder=5)
ax1.errorbar(df_sub['SpT'], df_sub['Teff'], yerr=df_sub['Teff_err'], c='blue', fmt='o', zorder=6)
# zorder makes it go on top even if it covers other points!

# --- Designate 1256-0224 -----
sub1256 = plt.scatter(df_sub['SpT'][0], df_sub['Teff'][0], color='blue', s=500, zorder=7, marker="*")
ax1.annotate('J1256-0224', xy=(12.7, 2700), color='k', fontsize=12)

# ---- Add Legend ----
plt.legend([fld, young, sub], ["Field", "Young", 'Subdwarf'], frameon=False, fontsize=12)

# ---- Plot fit lines  from the mcmc, random 100 -----
xl = np.array([0, 20])
for x in samples[np.random.randint(len(samples), size=500)]:
    plt.plot(xl, x[0]*xl+x[1], color="#17becf", alpha=0.05)

# To get the best fit line
best_fit_coeffs = np.median(samples, axis=0)
best_fit_line = best_fit_coeffs[0]*xl + best_fit_coeffs[1]
plt.plot(xl, best_fit_line, c='k', zorder=8)

# ---- Print the best fit coeffs and the std -----
print(best_fit_coeffs)
print(np.std(samples, axis=0))

plt.tight_layout()
plt.savefig('Plots/SptvTeff.png')

# From this example on curve fitting using the cov=True
# https://stackoverflow.com/questions/28505008/numpy-polyfit-how-to-get-1-sigma-uncertainty-around-the-estimated-curve
# Doesn't look much different
# x= df_subpoly['SpT']
# y = df_subpoly['Teff']
# n = 1
# p, C_p = np.polyfit(x, y, n, cov=True)  # C_z is estimated covariance matrix
# # Do the interpolation for plotting:
# t = np.linspace(5, 19, 500)
# # Matrix with rows 1, t, t**2, ...:
# TT = np.vstack([t**(n-i) for i in range(n+1)]).T
# yi = np.dot(TT, p)  # matrix multiplication calculates the polynomial values
# C_yi = np.dot(TT, np.dot(C_p, TT.T)) # C_y = TT*C_z*TT.T
# sig_yi = np.sqrt(np.diag(C_yi))  # Standard deviations are sqrt of diagonal
# # Do the plotting:
# fg, ax = plt.subplots(1, 1)
# ax.set_title("Fit for Polynomial (degree {}) with $\pm1\sigma$-interval".format(n))
# ax.fill_between(t, yi+sig_yi, yi-sig_yi, alpha=.25)
# ax.plot(t, yi,'-')
# ax.plot(x, y, 'ro')
# ax.axis('tight')
# fg.canvas.draw()
# plt.show()


# Another example says that you can get the errors for m and b from the square of the diagonals of the covarient matrix
# i.e coeffs, cov = np.polyfit(df_subpoly['SpT'], df_subpoly['Teff'], 1, cov=True)
# err = np.sqrt(np.diag(cov))
# Out[73]: array([  18.5512183 ,  206.48294636])

