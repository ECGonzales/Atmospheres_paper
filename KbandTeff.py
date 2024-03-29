import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_1256 = pd.read_csv('Data/Smoothed_data/teff_bandbyband_smoothed/correctpi1256-0224 (L3.5sd) SED_smoothed.txt',
                      sep=",", comment='#', header=None, names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff ----------------------------------
df_young = pd.read_csv('Data/Smoothed_data/teff_bandbyband_smoothed/teff2000-7523 (M9gamma) SED_updated_smoothed.txt',
                       sep=",", comment='#', header=None, names=["w", "f", "err"])
df_field = pd.read_csv('Data/Smoothed_data/teff_bandbyband_smoothed/teff0024-0158 (M9.5) SED_smoothed.txt', sep=",",
                       comment='#', header=None, names=["w", "f", "err"])

# ------------------------------------------------------------------------------------
# ------------------- Fix files to read all columns as Floats-------------------------
# ------------------------------------------------------------------------------------
df_1256 = df_1256.astype(float)
df_young = df_young.astype(float)
df_field = df_field.astype(float)

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_1256[(df_1256['w'] >= 2.16) & (df_1256['w'] <= 2.20)]
norm_df_1256 = df_1256['f']/(np.average(norm_region['f']))

norm_region2 = df_young[(df_young['w'] >= 2.16) & (df_young['w'] <= 2.20)]
norm_df_young = df_young['f']/(np.average(norm_region2['f']))

norm_region3 = df_field[(df_field['w'] >= 2.16) & (df_field['w'] <= 2.20)]
norm_df_field = df_field['f']/(np.average(norm_region3['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: K band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
plt.xlim([2.0, 2.35])
plt.ylim([0, 3.5])

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_1256['w'], norm_df_1256, c='blue')
ax1.plot(df_field['w'], norm_df_field + 1.2, c='#7C7D70')
ax1.plot(df_young['w'], norm_df_young + 1.7, c='#D01810')

# ------- Label Features --------------------------
H2O = pd.DataFrame()
H2O['x'] = [2.00, 2.20]
H2O['y'] = [2.84, 2.84]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.text(0.25, 0.825, 'H$_\mathrm{2} $O', transform=ax1.transAxes, color='k', fontsize=15)

CIA_H2 = pd.DataFrame()
CIA_H2['x'] = [2.01, 2.34]
CIA_H2['y'] = [3.2, 3.2]
plt.plot(CIA_H2['x'], CIA_H2['y'], color='k')
ax1.text(0.45, 0.925, 'CIA H$_\mathrm{2} $', transform=ax1.transAxes, color='k', fontsize=15)

CO = pd.DataFrame()
CO['x'] = [2.295, 2.34]
CO['y'] = [2.95, 2.95]
plt.plot(CO['x'], CO['y'], color='k')
ax1.text(0.88, 0.85, 'CO', transform=ax1.transAxes, color='k', fontsize=15)
COd = pd.DataFrame()
COd['x'] = [2.295, 2.295]
COd['y'] = [2.8, 2.95]
plt.plot(COd['x'], COd['y'], color='k')
# Create a Legend for the sources
ax1.annotate('J2000-7523', xy=(2.003, 0.5), color='#D01810', fontsize=15)
ax1.annotate('J0024-0158', xy=(2.003, 0.3), color='#7C7D70', fontsize=15)
ax1.annotate('J1256-0224', xy=(2.003, 0.1), color='blue', fontsize=15)

plt.tight_layout()
plt.savefig('Plots/KbandTeff.pdf', dpi=150)
