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

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_1256[(df_1256['w'] >= 0.98) & (df_1256['w'] <= 0.988)]
norm_df_1256 = df_1256['f']/(np.average(norm_region['f']))

norm_region2 = df_young[(df_young['w'] >= 0.98) & (df_young['w'] <= 0.988)]
norm_df_young = df_young['f']/(np.average(norm_region2['f']))

norm_region3 = df_field[(df_field['w'] >= 0.98) & (df_field['w'] <= 0.988)]
norm_df_field = df_field['f']/(np.average(norm_region3['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Y band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.95, 1.10])
plt.ylim([0, 3.5])

# ------Tick size and Axes Labels --------
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Normalized Flux (F$_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_1256['w'], norm_df_1256, c='blue')
ax1.plot(df_field['w'], norm_df_field + 0.5, c='#7C7D70')
ax1.plot(df_young['w'], norm_df_young + 1, c='#D01810')

# ------- Label Features --------------------------
# --- To make line for feature
Ti1 = pd.DataFrame()
Ti1['x'] = [0.96, 0.97]
Ti1['y'] = [0.3, 0.3]
plt.plot(Ti1['x'], Ti1['y'], color='k')
ax1.text(0.075, 0.04, 'Ti I', transform=ax1.transAxes, color='k', fontsize=15)
# -- To make a vertical line
Ti1up = pd.DataFrame()
Ti1up['x'] = [0.96, 0.96]
Ti1up['y'] = [0.3, 0.45]
plt.plot(Ti1up['x'], Ti1up['y'], color='k')
Ti1up2 = pd.DataFrame()
Ti1up2['x'] = [0.97, 0.97]
Ti1up2['y'] = [0.3, 0.45]
plt.plot(Ti1up2['x'], Ti1up2['y'], color='k')

# --- To make line for feature
FeH1 = pd.DataFrame()
FeH1['x'] = [0.9896, 1.0]
FeH1['y'] = [2.4, 2.4]
plt.plot(FeH1['x'], FeH1['y'], color='k')
ax1.text(0.272, 0.69, 'FeH', transform=ax1.transAxes, color='k', fontsize=15)
# -- To make a vertical line
FeH1d = pd.DataFrame()
FeH1d['x'] = [0.9896, 0.9896]
FeH1d['y'] = [2.3, 2.4]
plt.plot(FeH1d['x'], FeH1d['y'], color='k')

FeH2 = pd.DataFrame()
FeH2['x'] = [0.998, 1.085]
FeH2['y'] = [2.85, 2.85]
plt.plot(FeH2['x'], FeH2['y'], color='k')
ax1.text(0.55, 0.82, 'FeH', transform=ax1.transAxes, color='k', fontsize=15)
FeH2d = pd.DataFrame()
FeH2d['x'] = [0.998, 0.998]
FeH2d['y'] = [2.7, 2.85]
plt.plot(FeH2d['x'], FeH2d['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.08, 1.099]
H2O['y'] = [3.1, 3.1]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.text(0.9, 0.9, 'H$_\mathrm{2} $O', transform=ax1.transAxes, color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.08, 1.08]
H2Od['y'] = [2.95, 3.1]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.savefig('Plots/YbandTeff.png')
