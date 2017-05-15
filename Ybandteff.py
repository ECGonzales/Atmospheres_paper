import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_1256 = pd.read_csv('Data/FIRE_rereduced1256-0224 (L3.5sd) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff ----------------------------------
df_young = pd.read_csv('Data/teff0223-5815 (L0gamma) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_field = pd.read_csv('Data/0036+1821 (L3.5) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

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
FeH1 = pd.DataFrame()
FeH1['x'] = [0.989, 1.0]
FeH1['y'] = [2.3, 2.3]
plt.plot(FeH1['x'], FeH1['y'], color='k')
ax1.text(0.26, 0.66, 'FeH', transform=ax1.transAxes, color='k', fontsize=15)
FeH2 = pd.DataFrame()
FeH2['x'] = [0.998, 1.085]
FeH2['y'] = [2.85, 2.85]
plt.plot(FeH2['x'], FeH2['y'], color='k')
ax1.text(0.33, 0.82, 'FeH', transform=ax1.transAxes, color='k', fontsize=15)
H2O = pd.DataFrame()
H2O['x'] = [1.08, 1.099]
H2O['y'] = [3.1, 3.1]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.text(0.9, 0.9, 'H$_\mathrm{2} $O', transform=ax1.transAxes, color='k', fontsize=15)

plt.savefig('Plots/YbandTeff.png')