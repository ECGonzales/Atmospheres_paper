import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from astropy import units as u
from astropy.analytic_functions import blackbody_lambda as bblam
import numpy as np

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas Dataframes TODO: Add in new smoothed data

df_1256 = pd.read_csv('Data/Smoothed_data/lbol_smoothed/correctpi1256-0224 (L3.5sd) SED_nan_smoothed.txt', sep=",",
                      comment='#', header=None, names=["w", "f", "err"])
df_1256_phot = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) phot.txt', sep=" ", header=1, names=["w", "f", "err"])

# -------------- Comparison objects of the same Lbol ----------------------------------
df_young = pd.read_csv('Data/Smoothed_data/lbol_smoothed/lbol0223-5815 (L0gamma) SED_updated_smoothed.txt', sep=",",
                       comment='#', header=None, names=["w", "f", "err"])
df_young_phot = pd.read_csv('Data/lbol0223-5815 (L0gamma) phot_updated.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
df_field = pd.read_csv('Data/Smoothed_data/lbol_smoothed/1048-3956 (M9) SED_smoothed.txt', sep=",", comment='#',
                       header=None, names=["w", "f", "err"])
df_field_phot = pd.read_csv('Data/1048-3956 (M9) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])

# ------------------------------------------------------------------------------------
# ------------------- Fix files to read all columns as Floats-------------------------
# ------------------------------------------------------------------------------------
df_1256 = df_1256.astype(float)
df_young = df_young.astype(float)
df_field = df_field.astype(float)

# -----------------------------------------------------------------------------------------
# ---------------------------------- Create a Blackbody -----------------------------------
# -----------------------------------------------------------------------------------------
# Solve for temp from the Lbol = log(L/L_solar)
L_sun = 3.828*10**26/(4*np.pi*(3.086*10**17)**2)  # Lsun in W / 4pi(distance of 10pc)^2

L_1256 = (10**(-3.518)*L_sun)/(((1.03/10)*(2.2657*10**(-9)))**2)  # 10^(Lbol)*L_sun/(radius of 1256/10pc)*(1 Rjup in pc)
temp_lbol_1256 = (L_1256/(5.670*10**(-8)))**(1.0/4.0)  # 5.670-> stefan-boltzmann constant

# create the BB with the solved temp.
wavelengths = list(range(1000000)) * u.AA

temperature_1256 = temp_lbol_1256 * u.K
flux_lam_1256 = bblam(wavelengths, temperature_1256)
flux_lam_scaled_1256 = flux_lam_1256*(((1.03/10.0)*(2.2657*10**(-9)))**2)

# field bb
L_field = (10**(-3.518)*L_sun)/(((1.07/10)*(2.2657*10**(-9)))**2)
temp_lbol_field = (L_field/(5.670*10**(-8)))**(1.0/4.0)
temperature_field = temp_lbol_field * u.K
flux_lam_field = bblam(wavelengths, temperature_field)
flux_lam_scaled_field = flux_lam_field * (((1.07/10.0)*(2.2657*10**(-9)))**2)

# Young bb
L_young = (10**(-3.518)*L_sun)/(((1.53/10)*(2.2657*10**(-9)))**2)
temp_lbol_young = (L_young/(5.670*10**(-8)))**(1.0/4.0)
temperature_young = temp_lbol_field * u.K
flux_lam_young = bblam(wavelengths, temperature_young)
flux_lam_scaled_young = flux_lam_young * (((1.53/10.0)*(2.2657*10**(-9)))**2)


# -------------------------------------------------------------------------------------
# ------------------- Plotting: Comparison of same Lbol -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# -------- Add data -----------
ax1.loglog(df_young['w'], df_young['f'], c='#D01810')
ax1.scatter(df_young_phot['w'], df_young_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
ax1.scatter(df_young_phot['w'], df_young_phot['f'], c='#D01810', s=50)        # black border
ax1.loglog(df_field['w'], df_field['f'], c='#7C7D70')
ax1.scatter(df_field_phot['w'], df_field_phot['f'], c='k', s=70)
ax1.scatter(df_field_phot['w'], df_field_phot['f'], c='#7C7D70', s=50)
ax1.loglog(df_1256['w'], df_1256['f'], c='blue')
ax1.scatter(df_1256_phot['w'], df_1256_phot['f'], c='k', s=70)
ax1.scatter(df_1256_phot['w'], df_1256_phot['f'], c='blue', s=50)

# -------- Plot the blackbodies -------------------
# Decided not to show in the paper currently
# ax1.loglog(wavelengths.to(u.um), flux_lam_scaled_1256, c='blue', ls='dashed', zorder=1, alpha=0.75)
# ax1.loglog(wavelengths.to(u.um), flux_lam_scaled_field, c='#7C7D70', ls='dashed', zorder=1, alpha=0.75)
# ax1.loglog(wavelengths.to(u.um), flux_lam_scaled_young, c='#D01810', ls='dashed', zorder=1, alpha=0.75)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.5, 24])
plt.ylim([6*10**(-19),2*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.6, 2, 3, 22]))
ax1.tick_params(axis='both', which='major', labelsize=20, length=8, width=1.1)
ax1.tick_params(axis='both', which='minor', labelsize=18, length=4, width=1.1)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Flux ($\mathrm{erg\ s^{-1} cm^{-2} A^{-1}}$)', fontsize=25)

# ------ Labeling Spectra and Photometric points --------
# Old
ax1.text(0.1, 0.4, 'J1256-0224', transform=ax1.transAxes, color='blue', fontsize=15)
ax1.text(0.1, 0.35, 'Age: >> 1 Gyr', transform=ax1.transAxes, color='blue', fontsize=15)
ax1.text(0.1, 0.3, 'Old', transform=ax1.transAxes, color='blue', fontsize=15)
ax1.text(0.1, 0.25, '$L_\mathrm{bol}:-3.625\pm 0.05$', transform=ax1.transAxes, color='blue', fontsize=15)

# Field
ax1.text(0.58, 0.2, 'J1048-3956', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
ax1.text(0.58, 0.15, 'Age: 500 - 10000 Myr ', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
ax1.text(0.58, 0.1, 'Field', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
ax1.text(0.58, 0.05, '$L_\mathrm{bol}:-3.485\pm 0.001$', transform=ax1.transAxes, color='#7C7D70', fontsize=15)

# Young
ax1.text(0.6, 0.95, 'J0223-5815', transform=ax1.transAxes, color='#D01810', fontsize=15)
ax1.text(0.6, 0.9, 'Age: 10-40 Myr (Tuc-Hor)', transform=ax1.transAxes, color='#D01810', fontsize=15)
ax1.text(0.6, 0.85, 'Young', transform=ax1.transAxes, color='#D01810', fontsize=15)
ax1.text(0.6, 0.8, '$L_\mathrm{bol}:-3.515\pm0.022 $', transform=ax1.transAxes, color='#D01810', fontsize=15)

plt.tight_layout()
plt.savefig('Plots/comparison_Lbol.png', dpi=150)
