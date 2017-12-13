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
norm_region = df_1256[(df_1256['w'] >= 1.5) & (df_1256['w'] <= 1.52)]
norm_df_1256 = df_1256['f']/(np.average(norm_region['f']))

norm_region2 = df_young[(df_young['w'] >= 1.5) & (df_young['w'] <= 1.52)]
norm_df_young = df_young['f']/(np.average(norm_region2['f']))

norm_region3 = df_field[(df_field['w'] >= 1.5) & (df_field['w'] <= 1.52)]
norm_df_field = df_field['f']/(np.average(norm_region3['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: H band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
plt.xlim([1.42, 1.80])
plt.ylim([0, 3.5])

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_1256['w'], norm_df_1256, c='blue')
ax1.plot(df_field['w'], norm_df_field + 0.5, c='#7C7D70')
ax1.plot(df_young['w'], norm_df_young + 1, c='#D01810')

# ------- Label Features --------------------------
FeH = pd.DataFrame()
FeH['x'] = [1.581, 1.66]
FeH['y'] = [2.5, 2.5]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.text(0.5, 0.72, 'FeH', transform=ax1.transAxes, color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.581, 1.581]
FeHd['y'] = [2.35, 2.5]
plt.plot(FeHd['x'], FeHd['y'], color='k')

CH4 = pd.DataFrame()
CH4['x'] = [1.67, 1.75]
CH4['y'] = [2.7, 2.7]
plt.plot(CH4['x'], CH4['y'], color='k')
ax1.text(0.74, 0.785, 'CH$_\mathrm{4}$', transform=ax1.transAxes, color='k', fontsize=15)
CH4d = pd.DataFrame()
CH4d['x'] = [1.67, 1.67]
CH4d['y'] = [2.5, 2.7]
plt.plot(CH4d['x'], CH4d['y'], color='k')

plt.tight_layout()
plt.savefig('Plots/HbandTeff.png')
