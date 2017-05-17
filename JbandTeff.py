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
df_1256j = df_1256[(df_1256['w'] >= 1.15311) & (df_1256['w'] <= 1.34807)]

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_1256j[(df_1256j['w'] >= 1.29) & (df_1256j['w'] <= 1.31)]
norm_df_1256 = df_1256j['f']/(np.average(norm_region['f']))

norm_region2 = df_young[(df_young['w'] >= 1.29) & (df_young['w'] <= 1.31)]
norm_df_young = df_young['f']/(np.average(norm_region2['f']))

norm_region3 = df_field[(df_field['w'] >= 1.29) & (df_field['w'] <= 1.31)]
norm_df_field = df_field['f']/(np.average(norm_region3['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: J band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.12, 1.35])
plt.ylim([0, 3.5])

# ------Tick size and Axes Labels --------
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Normalized Flux (F$_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_1256j['w'], norm_df_1256, c='blue')
ax1.plot(df_field['w'], norm_df_field + 1, c='#7C7D70')
ax1.plot(df_young['w'], norm_df_young + 1.5, c='#D01810')

# ------- Label Features --------------------------
NaI = pd.DataFrame()
NaI['x'] = [1.13656, 1.14269]
NaI['y'] = [1.3, 1.3]
plt.plot(NaI['x'], NaI['y'], color='k')
ax1.text(0.0625, 0.32, 'NaI', transform=ax1.transAxes, color='k', fontsize=15)
# ----- Making each of the vertical lines on each end --------
NaId = pd.DataFrame()
NaId['x'] = [1.13656, 1.13656]
NaId['y'] = [1.3, 1.4]
plt.plot(NaId['x'], NaId['y'], color='k')
NaId2 = pd.DataFrame()
NaId2['x'] = [1.14269, 1.14269]
NaId2['y'] = [1.3, 1.4]
plt.plot(NaId2['x'], NaId2['y'], color='k')

KI1 = pd.DataFrame()
KI1['x'] = [1.16569, 1.18225]
KI1['y'] = [0.3, 0.3]
plt.plot(KI1['x'], KI1['y'], color='k')
ax1.text(0.22, 0.04, 'KI', transform=ax1.transAxes, color='k', fontsize=15)
# ----- Making each of the vertical lines on each end --------
KI1up1 = pd.DataFrame()
KI1up1['x'] = [1.16569, 1.16569]
KI1up1['y'] = [0.3, 0.4]
plt.plot(KI1up1['x'], KI1up1['y'], color='k')
KI1up2 = pd.DataFrame()
KI1up2['x'] = [1.18225, 1.18225]
KI1up2['y'] = [0.3, 0.4]
plt.plot(KI1up2['x'], KI1up2['y'], color='k')

FeH = pd.DataFrame()
FeH['x'] = [1.19, 1.24]
FeH['y'] = [2.6, 2.6]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.text(0.38, 0.75, 'FeH', transform=ax1.transAxes, color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.19, 1.19]
FeHd['y'] = [2.45, 2.6]
plt.plot(FeHd['x'], FeHd['y'], color='k')

KI2 = pd.DataFrame()
KI2['x'] = [1.24175, 1.25616]
KI2['y'] = [0.6, 0.6]
plt.plot(KI2['x'], KI2['y'], color='k')
ax1.text(0.55, 0.12, 'KI', transform=ax1.transAxes, color='k', fontsize=15)
KI2up1 = pd.DataFrame()
KI2up1['x'] = [1.24175, 1.24175]
KI2up1['y'] = [0.6, 0.7]
plt.plot(KI2up1['x'], KI2up1['y'], color='k')
KI2up2 = pd.DataFrame()
KI2up2['x'] = [1.25616, 1.25616]
KI2up2['y'] = [0.6, 0.7]
plt.plot(KI2up2['x'], KI2up2['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.32, 1.35]
H2O['y'] = [2.8, 2.8]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.text(0.9, 0.81, 'H$_\mathrm{2} $O', transform=ax1.transAxes, color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.32, 1.32]
H2Od['y'] = [2.65, 2.8]
plt.plot(H2Od['x'], H2Od['y'], color='k')

plt.savefig('Plots/JbandTeff.png')
