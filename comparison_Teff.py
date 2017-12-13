import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from astropy import units as u
from astropy.analytic_functions import blackbody_lambda as bblam


# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes, commas for Jonathan's

df_1256 = pd.read_csv('Data/Smoothed_data/teff_smoothed/correctpi1256-0224 (L3.5sd) SED_nan_smoothed.txt', sep=",",
                      comment='#', header=None, names=["w", "f", "err"])
df_1256_phot = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) phot.txt', sep=" ", header=1, names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff ----------------------------------
df_young = pd.read_csv('Data/Smoothed_data/teff_smoothed/teff2000-7523 (M9gamma) SED_updated_smoothed.txt', sep=",",
                       comment='#', header=None, names=["w", "f", "err"])
df_young_phot = pd.read_csv('Data/teff2000-7523 (M9gamma) phot_updated.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
# df_young_phot_synth = pd.read_csv('Data/teff2000-7523_synthetic_phot.txt', sep=" ", comment='#', header=None,
#                             names=["w", "f", "err"])
df_field = pd.read_csv('Data/Smoothed_data/teff_smoothed/teff0024-0158 (M9.5) SED_smoothed.txt', sep=",", comment='#',
                       header=None, names=["w", "f", "err"])
df_field_phot = pd.read_csv('Data/teff0024-0158 (M9.5) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])

# ------------------------------------------------------------------------------------
# ------------------- Fix files to read all columns as Floats-------------------------
# ------------------------------------------------------------------------------------
df_1256 = df_1256.astype(float)
df_young = df_young.astype(float)
df_field = df_field.astype(float)

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Comparison of same Teff -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# -------- Add data -----------
ax1.loglog(df_young['w'], df_young['f'], c='#D01810')
ax1.scatter(df_young_phot['w'], df_young_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
ax1.scatter(df_young_phot['w'], df_young_phot['f'], c='#D01810', s=50)        # black border
# ax1.scatter(df_young_phot_synth['w'], df_young_phot_synth['f'], c='k', s=70, marker='d')
# ax1.scatter(df_young_phot_synth['w'], df_young_phot_synth['f'], c='#D01810', s=50, marker='d')
ax1.loglog(df_field['w'], df_field['f'], c='#7C7D70')
ax1.scatter(df_field_phot['w'], df_field_phot['f'], c='k', s=70)
ax1.scatter(df_field_phot['w'], df_field_phot['f'], c='#7C7D70', s=50)
ax1.loglog(df_1256['w'], df_1256['f'], c='blue')
ax1.scatter(df_1256_phot['w'], df_1256_phot['f'], c='k', s=70)
ax1.scatter(df_1256_phot['w'], df_1256_phot['f'], c='blue', s=50)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.45, 16])
plt.ylim([4*10**(-18), 4*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.45, 0.6, 2, 3, 16]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=18, length=4, width=1.1)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Flux ($\mathrm{erg\ s^{-1} cm^{-2} A^{-1}}$)', fontsize=25)

# ------ Labeling Spectra and Photometric points --------
# Old
ax1.text(0.17, 0.4, 'J1256-0224', transform=ax1.transAxes, color='blue', fontsize=15)
ax1.text(0.17, 0.35, 'Age: >> 1 Gyr', transform=ax1.transAxes, color='blue', fontsize=15)
ax1.text(0.17, 0.3, 'Old', transform=ax1.transAxes, color='blue', fontsize=15)
ax1.text(0.17, 0.25, '$T_\mathrm{eff}:2340\pm 310$ K', transform=ax1.transAxes, color='blue', fontsize=15)

# Field
ax1.text(0.58, 0.2, 'J0024-0158', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
ax1.text(0.58, 0.15, 'Age: 500 - 10000 Myr ', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
ax1.text(0.58, 0.1, 'Field', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
ax1.text(0.58, 0.05, '$T_\mathrm{eff}:2385\pm 77$ K', transform=ax1.transAxes, color='#7C7D70', fontsize=15)

# Young
ax1.text(0.6, 0.95, 'J2000-7523', transform=ax1.transAxes, color='#D01810', fontsize=15)
ax1.text(0.6, 0.9, r'Age: 12 - 22 Myr ($\beta$ Pictoris)', transform=ax1.transAxes, color='#D01810', fontsize=15)
# r is to deal with \a or \b as being special python characters
ax1.text(0.6, 0.85, 'Young', transform=ax1.transAxes, color='#D01810', fontsize=15)
ax1.text(0.6, 0.8, '$T_\mathrm{eff}:2450\pm 62$ K', transform=ax1.transAxes, color='#D01810', fontsize=15)

plt.tight_layout()  # use to reduce whitespace in paper
plt.savefig('Plots/comparison_Teff.png')





# ---------------------------------------------------------------------------------------------------------------------
# --------------------- Adding a blackbody and setting objects to the same radius -------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# ---------------------------------- Create a Blackbody -----------------------------------
# -----------------------------------------------------------------------------------------
wavelengths = list(range(1000000)) * u.AA
temperature = 2344 * u.K
flux_lam = bblam(wavelengths, temperature)
flux_lam_scaled = flux_lam*(((1.03/10.0)*(2.2657*10**(-9)))**2)  # scale blackbody to distance of 10 pc and

# Scale all of the objects to 1 Jupiter radius. To do that I need to divide all of the fluxes by their r**2
young_rscaled_spec = df_young['f']/(1.79**2)
young_rscaled_phot = df_young_phot['f']/(1.79**2)
field_rscaled_spec = df_field['f']/(1.09**2)
field_rscaled_phot = df_field_phot['f']/(1.09**2)
sub_rscaled_spec = df_1256['f']/(1.03**2)
sub_rscaled_phot = df_1256_phot['f']/(1.03**2)
# import SEDkit.utilities as ut
# import numpy as np
# wavelengths = np.arange(0, 20, 0.25)
# ut.blackbody(wavelengths, 2344)


# -------------------------------------------------------------------------------------
# ------------------- Plotting: Comparison of same Teff of same size-------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # match other plots on github (the size will change if done in pieces

# -------- Add data R-scaled -----------
ax1.loglog(df_young['w'], young_rscaled_spec, c='#D01810')
ax1.scatter(df_young_phot['w'], young_rscaled_phot, c='k', s=70)  # The ones with size 70 are to give the circles a
ax1.scatter(df_young_phot['w'], young_rscaled_phot, c='#D01810', s=50)        # black border
ax1.loglog(df_field['w'], field_rscaled_spec, c='#7C7D70')
ax1.scatter(df_field_phot['w'], field_rscaled_phot, c='k', s=70)
ax1.scatter(df_field_phot['w'], field_rscaled_phot, c='#7C7D70', s=50)
ax1.loglog(df_1256['w'], sub_rscaled_spec, c='blue')
ax1.scatter(df_1256_phot['w'], sub_rscaled_phot, c='k', s=70)
ax1.scatter(df_1256_phot['w'], sub_rscaled_phot, c='blue', s=50)

# --------- Plot the blackbody --------------------
ax1.loglog(wavelengths.to(u.um), flux_lam_scaled, c='k', ls='dashed', zorder=1)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.33, 16])
plt.ylim([6*10**(-19), 4*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.35, 0.6, 2, 3, 16]))
ax1.tick_params(axis='x', which='major', labelsize=20)
ax1.tick_params(axis='x', which='minor', labelsize=20)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Flux ($\mathrm{erg\ s^{-1} cm^{-2} A^{-1}}$)', fontsize=25)

# ------ Labeling Spectra and Photometric points --------
# Old
ax1.text(0.23, 0.4, 'J1256-0224', transform=ax1.transAxes, color='blue', fontsize=15)
ax1.text(0.23, 0.35, 'Age: >> 1 Gyr', transform=ax1.transAxes, color='blue', fontsize=15)
ax1.text(0.23, 0.3, 'Old', transform=ax1.transAxes, color='blue', fontsize=15)
ax1.text(0.23, 0.25, '$T_\mathrm{eff}:2344\pm 314$ K', transform=ax1.transAxes, color='blue', fontsize=15)

# Field
ax1.text(0.62, 0.2, 'J0024-0158', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
ax1.text(0.62, 0.15, 'Age: 500 - 10000 Myr ', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
ax1.text(0.62, 0.1, 'Field', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
ax1.text(0.62, 0.05, '$T_\mathrm{eff}:2385\pm 77$ K', transform=ax1.transAxes, color='#7C7D70', fontsize=15)

# Young
ax1.text(0.6, 0.95, 'J2000-7523', transform=ax1.transAxes, color='#D01810', fontsize=15)
ax1.text(0.6, 0.9, r'Age: 12 - 22 Myr ($\beta$ Pictoris)', transform=ax1.transAxes, color='#D01810', fontsize=15)
# r is to deal with \a or \b as being special python characters
ax1.text(0.6, 0.85, 'Young', transform=ax1.transAxes, color='#D01810', fontsize=15)
ax1.text(0.6, 0.8, '$T_\mathrm{eff}:2363\pm 74$ K', transform=ax1.transAxes, color='#D01810', fontsize=15)

plt.tight_layout()  # use to reduce whitespace in paper
plt.savefig('Plots/comparison_Teff_sameradius.png')
