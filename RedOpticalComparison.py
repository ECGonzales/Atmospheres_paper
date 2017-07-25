import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_1256 = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff ----------------------------------
df_young = pd.read_csv('Data/teff2000-7523 (M9gamma) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_field = pd.read_csv('Data/teff0024-0158 (M9.5) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

# ----------------------- Same SpT ----------------------------------------------------
df_fieldspt = pd.read_csv('Data/NotUsingAsCompariosn/0036+1821 (L3.5) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_1256[(df_1256['w'] >= 0.64) & (df_1256['w'] <= 0.65)]
norm_df_1256 = df_1256['f']/(np.average(norm_region['f']))

norm_region2 = df_young[(df_young['w'] >= 0.64) & (df_young['w'] <= 0.65)]
norm_df_young = df_young['f']/(np.average(norm_region2['f']))

norm_region3 = df_field[(df_field['w'] >= 0.64) & (df_field['w'] <= 0.65)]
norm_df_field = df_field['f']/(np.average(norm_region3['f']))

norm_region4 = df_fieldspt[(df_fieldspt['w'] >= 0.64) & (df_fieldspt['w'] <= 0.65)]
norm_df_fieldspt = df_fieldspt['f']/(np.average(norm_region4['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Red Optical comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.60, 0.90])
plt.ylim([-0.01, 58])

# ------Tick size and Axes Labels --------
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Normalized Flux (F$_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_fieldspt['w'], norm_df_fieldspt, c='#7C7D70')
ax1.plot(df_1256['w'], norm_df_1256 + 15, c='blue')
ax1.plot(df_field['w'], norm_df_field + 30, c='#7C7D70')
ax1.plot(df_young['w'], norm_df_young + 45, c='#D01810')

# -------- Dividing Line ----------
divide = pd.DataFrame()
divide['x'] = [0.75, 0.75]
divide['y'] = [0, 58]
plt.plot(divide['x'], divide['y'], color='k', linestyle='dashed')


# -------- Label the Objects ---------
ax1.text(0.01, 0.1, '0036+1821  (L3.5)', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.05, 'T$_\mathrm{eff}: 1868 \pm 68$ K ', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.4, '1256-0024  (sdL3.5)', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.35, 'T$_\mathrm{eff}: 2344 \pm 314$ K', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.63, '0024-0158  (M9)', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.58, 'T$_\mathrm{eff}: 2385 \pm 77$ K', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.87, '2000-7523  (M9$\gamma$)', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.82, 'T$_\mathrm{eff}: 2363 \pm 74$ K', transform=ax1.transAxes, color='k', fontsize=15)

plt.savefig('Plots/RedOpticalComparison.png')
