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
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.95, 1.10])
plt.ylim([0, 3.5])
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)


# ------Tick size and Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_1256['w'], norm_df_1256, c='blue')
ax1.plot(df_field['w'], norm_df_field + 0.5, c='#7C7D70')
ax1.plot(df_young['w'], norm_df_young + 1, c='#D01810')

# ------- Label Features --------------------------
# --- To make line for feature
Ti1 = pd.DataFrame()
Ti1['x'] = [0.96042912, 0.97884568]
Ti1['y'] = [0.3, 0.3]
plt.plot(Ti1['x'], Ti1['y'], color='k')
ax1.text(0.12, 0.04, 'Ti$\,$I', transform=ax1.transAxes, color='k', fontsize=15)
# -- To make vertical lines
Ti1up = pd.DataFrame()
Ti1up['x'] = [0.96042912, 0.96042912]
Ti1up['y'] = [0.3, 0.45]
plt.plot(Ti1up['x'], Ti1up['y'], color='k')

Ti1up2 = pd.DataFrame()
Ti1up2['x'] = [0.96408301, 0.96408301]
Ti1up2['y'] = [0.3, 0.45]
plt.plot(Ti1up2['x'], Ti1up2['y'], color='k')

Ti1up3 = pd.DataFrame()
Ti1up3['x'] = [0.96516997, 0.96516997]
Ti1up3['y'] = [0.3, 0.45]
plt.plot(Ti1up3['x'], Ti1up3['y'], color='k')

Ti1up4 = pd.DataFrame()
Ti1up4['x'] = [0.96774343, 0.96774343]
Ti1up4['y'] = [0.3, 0.45]
plt.plot(Ti1up4['x'], Ti1up4['y'], color='k')

Ti1up5 = pd.DataFrame()
Ti1up5['x'] = [0.96923371, 0.96923371]
Ti1up5['y'] = [0.3, 0.45]
plt.plot(Ti1up5['x'], Ti1up5['y'], color='k')

Ti1up6 = pd.DataFrame()
Ti1up6['x'] = [0.97085682, 0.97085682]
Ti1up6['y'] = [0.3, 0.45]
plt.plot(Ti1up6['x'], Ti1up6['y'], color='k')

Ti1up7 = pd.DataFrame()
Ti1up7['x'] = [0.97315592, 0.97315592]
Ti1up7['y'] = [0.3, 0.45]
plt.plot(Ti1up7['x'], Ti1up7['y'], color='k')

Ti1up8 = pd.DataFrame()
Ti1up8['x'] = [0.97465017, 0.97465017]
Ti1up8['y'] = [0.3, 0.45]
plt.plot(Ti1up8['x'], Ti1up8['y'], color='k')

Ti1up9 = pd.DataFrame()
Ti1up9['x'] = [0.97708032, 0.97708032]
Ti1up9['y'] = [0.3, 0.45]
plt.plot(Ti1up9['x'], Ti1up9['y'], color='k')

Ti1up10 = pd.DataFrame()
Ti1up10['x'] = [0.97884568, 0.97884568]
Ti1up10['y'] = [0.3, 0.45]
plt.plot(Ti1up10['x'], Ti1up10['y'], color='k')

# --- To make line for features ---------
FeH1 = pd.DataFrame()
FeH1['x'] = [0.9896, 1.0]
FeH1['y'] = [2.3, 2.3]
plt.plot(FeH1['x'], FeH1['y'], color='k')
ax1.text(0.272, 0.66, 'FeH', transform=ax1.transAxes, color='k', fontsize=15)
# -- To make a vertical line
FeH1d = pd.DataFrame()
FeH1d['x'] = [0.9896, 0.9896]
FeH1d['y'] = [2.15, 2.3]
plt.plot(FeH1d['x'], FeH1d['y'], color='k')

FeH2 = pd.DataFrame()
FeH2['x'] = [0.998, 1.085]
FeH2['y'] = [2.75, 2.75]
plt.plot(FeH2['x'], FeH2['y'], color='k')
ax1.text(0.55, 0.79, 'FeH', transform=ax1.transAxes, color='k', fontsize=15)
FeH2d = pd.DataFrame()
FeH2d['x'] = [0.998, 0.998]
FeH2d['y'] = [2.6, 2.75]
plt.plot(FeH2d['x'], FeH2d['y'], color='k')

VO = pd.DataFrame()
VO['x'] = [1.0456, 1.08]
VO['y'] = [2.54, 2.54]
plt.plot(VO['x'], VO['y'], color='k')
ax1.text(0.72, 0.73, 'VO', transform=ax1.transAxes, color='k', fontsize=15)
VOd = pd.DataFrame()
VOd['x'] = [1.0456, 1.0456]
VOd['y'] = [2.54, 2.41]
plt.plot(VOd['x'], VOd['y'], color='k')

H2O = pd.DataFrame()
H2O['x'] = [1.08, 1.099]
H2O['y'] = [3, 3]
plt.plot(H2O['x'], H2O['y'], color='k')
ax1.text(0.9, 0.87, 'H$_\mathrm{2} $O', transform=ax1.transAxes, color='k', fontsize=15)
H2Od = pd.DataFrame()
H2Od['x'] = [1.08, 1.08]
H2Od['y'] = [2.85, 3]
plt.plot(H2Od['x'], H2Od['y'], color='k')

# Create a Legend for the sources
ax1.annotate('J2000-7523', xy=(0.951, 3.3), color='#D01810', fontsize=15)
ax1.annotate('J0024-0158', xy=(0.951, 3.1), color='#7C7D70', fontsize=15)
ax1.annotate('J1256-0224', xy=(0.951, 2.9), color='blue', fontsize=15)

plt.tight_layout()
plt.savefig('Plots/YbandTeff.pdf', dpi=150)
