import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas Dataframes

df_1256 = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_1256_phot = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) phot.txt', sep=" ", header=1, names=["w", "f", "err"])

# -------------- Comparison objects of the same Lbol ----------------------------------
df_young = pd.read_csv('Data/lbol0223-5815 (L0gamma) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_young_phot = pd.read_csv('Data/lbol0223-5815 (L0gamma) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])
df_field = pd.read_csv('Data/lbol1048-3956 (M9) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_field_phot = pd.read_csv('Data/lbol1048-3956 (M9) phot.txt', sep=" ", comment='#', header=None,
                            names=["w", "f", "err"])


# -------------------------------------------------------------------------------------
# ------------------- Plotting: Comparison of same Lbol -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

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

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.33, 24])
plt.ylim([6*10**(-19),2*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.35, 0.6, 2, 3, 22]))
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
ax1.text(0.23, 0.25, '$L_\mathrm{bol}:-3.518\pm 0.225$', transform=ax1.transAxes, color='blue', fontsize=15)

# Field
ax1.text(0.58, 0.2, 'J1048-3956', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
ax1.text(0.58, 0.15, 'Age: 500 - 10000 Myr ', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
ax1.text(0.58, 0.1, 'Field', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
ax1.text(0.58, 0.05, '$L_\mathrm{bol}:-3.513\pm0.003 $', transform=ax1.transAxes, color='#7C7D70', fontsize=15)

# Young
ax1.text(0.6, 0.95, 'J0223-5815', transform=ax1.transAxes, color='#D01810', fontsize=15)
ax1.text(0.6, 0.9, 'Age: 10-40 Myr (Tuc-Hor)', transform=ax1.transAxes, color='#D01810', fontsize=15)
ax1.text(0.6, 0.85, 'Young', transform=ax1.transAxes, color='#D01810', fontsize=15)
ax1.text(0.6, 0.8, '$L_\mathrm{bol}:-3.632\pm0.082 $', transform=ax1.transAxes, color='#D01810', fontsize=15)

plt.tight_layout()
plt.savefig('Plots/comparison_Lbol.png')
