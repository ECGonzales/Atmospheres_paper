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

# -------- Remove lines from when trimming with SEDkit for 1256
df_1256h = df_1256[(df_1256['w'] >= 1.49786) & (df_1256['w'] <= 1.79593)]

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_1256h[(df_1256h['w'] >= 1.5) & (df_1256h['w'] <= 1.52)]
norm_df_1256 = df_1256h['f']/(np.average(norm_region['f']))

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
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.42, 1.80])
plt.ylim([0, 3.5])

# ------Tick size and Axes Labels --------
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Normalized Flux (F$_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_1256h['w'], norm_df_1256, c='blue')
ax1.plot(df_field['w'], norm_df_field + 0.5, c='#7C7D70')
ax1.plot(df_young['w'], norm_df_young + 1, c='#D01810')

# ------- Label Features --------------------------
FeH = pd.DataFrame()
FeH['x'] = [1.581, 1.66]
FeH['y'] = [2.6, 2.6]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.text(0.5, 0.75, 'FeH', transform=ax1.transAxes, color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.581, 1.581]
FeHd['y'] = [2.5, 2.6]
plt.plot(FeHd['x'], FeHd['y'], color='k')

CH4 = pd.DataFrame()
CH4['x'] = [1.67, 1.75]
CH4['y'] = [2.8, 2.8]
plt.plot(CH4['x'], CH4['y'], color='k')
ax1.text(0.74, 0.81, 'CH$_\mathrm{4}$', transform=ax1.transAxes, color='k', fontsize=15)
CH4d = pd.DataFrame()
CH4d['x'] = [1.67, 1.67]
CH4d['y'] = [2.6, 2.8]
plt.plot(CH4d['x'], CH4d['y'], color='k')

plt.savefig('Plots/HbandTeff.png')
