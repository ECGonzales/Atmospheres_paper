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
norm_region = df_1256[(df_1256['w'] >= 1.29) & (df_1256['w'] <= 1.31)]
norm_df_1256 = df_1256['f']/(np.average(norm_region['f']))

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
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([1.12, 1.35])
plt.ylim([0, 3.5])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)

# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_1256['w'], norm_df_1256, c='blue')
ax1.plot(df_field['w'], norm_df_field + 1, c='#7C7D70')
ax1.plot(df_young['w'], norm_df_young + 1.6, c='#D01810')

# ------- Label Features --------------------------
NaI = pd.DataFrame()
NaI['x'] = [1.13656, 1.14269]
NaI['y'] = [1.3, 1.3]
plt.plot(NaI['x'], NaI['y'], color='k')
ax1.text(0.0625, 0.32, 'Na$\,$I', transform=ax1.transAxes, color='k', fontsize=15)
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
ax1.text(0.22, 0.04, 'K$\,$I', transform=ax1.transAxes, color='k', fontsize=15)
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
FeH['y'] = [2.7, 2.7]
plt.plot(FeH['x'], FeH['y'], color='k')
ax1.text(0.38, 0.78, 'FeH', transform=ax1.transAxes, color='k', fontsize=15)
FeHd = pd.DataFrame()
FeHd['x'] = [1.19, 1.19]
FeHd['y'] = [2.55, 2.7]
plt.plot(FeHd['x'], FeHd['y'], color='k')

KI2 = pd.DataFrame()
KI2['x'] = [1.24175, 1.25616]
KI2['y'] = [0.6, 0.6]
plt.plot(KI2['x'], KI2['y'], color='k')
ax1.text(0.55, 0.12, 'K$\,$I', transform=ax1.transAxes, color='k', fontsize=15)
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
H2O['y'] = [2.9, 2.9]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.text(0.9, 0.84, 'H$_\mathrm{2} $O', transform=ax1.transAxes, color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.32, 1.32]
H2Od['y'] = [2.75, 2.9]
plt.plot(H2Od['x'], H2Od['y'], color='k')

# Create a Legend for the sources
ax1.annotate('J2000-7523', xy=(1.122, 3.3), color='#D01810', fontsize=15)
ax1.annotate('J0024-0158', xy=(1.122, 3.1), color='#7C7D70', fontsize=15)
ax1.annotate('J1256-0224', xy=(1.122, 2.9), color='blue', fontsize=15)

plt.tight_layout()
plt.savefig('Plots/JbandTeff.pdf', dpi=150)
