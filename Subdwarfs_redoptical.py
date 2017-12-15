import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
# Not reading in HD114662B because only has NIR spectrum, None for 1256-1408, and problem for 0616

df_1256 = pd.read_csv('Data/Smoothed_data/Subdwarfs_red_optical_smoothed/correctpi1256-0224 (L3.5sd) SED_smoothed.txt',
                      sep=",", comment='#', header=None, names=["w", "f", "err"])

# -------------- Subdwarfs ----------------------------------
df_0532 = pd.read_csv('Data/Smoothed_data/Subdwarfs_red_optical_smoothed/0532+8246 (L7sd) SED_smoothed.txt', sep=",", comment='#', header=None, names=["w", "f", "err"])
df_0616 = pd.read_csv('Data/Smoothed_data/Subdwarfs_red_optical_smoothed/0616-6407 (L5sd) SED_smoothed.txt', sep=",", comment='#', header=None, names=["w", "f", "err"])
df_1013 = pd.read_csv('Data/Smoothed_data/Subdwarfs_red_optical_smoothed/1013-1356 (M9.5sd) SED_smoothed.txt', sep=",", comment='#', header=None, names=["w", "f", "err"])
df_1425 = pd.read_csv('Data/Smoothed_data/Subdwarfs_red_optical_smoothed/1425+7102 (M8sd) SED_smoothed.txt', sep=",", comment='#', header=None, names=["w", "f", "err"])
df_LHS = pd.read_csv('Data/Smoothed_data/Subdwarfs_red_optical_smoothed/1439+1839 (M7sd) SED_smoothed.txt', sep=",", comment='#', header=None, names=["w", "f", "err"])
df_1444 = pd.read_csv('Data/1444-2019 (M9sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1610 = pd.read_csv('Data/Smoothed_data/Subdwarfs_red_optical_smoothed/1610-0040 (M7sd) SED_smoothed.txt', sep=",", comment='#', header=None, names=["w", "f", "err"])
df_1626 = pd.read_csv('Data/1626+3925 (L4sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_2036 = pd.read_csv('Data/Smoothed_data/Subdwarfs_red_optical_smoothed/2036+5059 (M7.5sd) SED_smoothed.txt', sep=",", comment='#', header=None, names=["w", "f", "err"])

# ------------------------------------------------------------------------------------
# ------------------- Fix files to read all columns as Floats-------------------------
# ------------------------------------------------------------------------------------
df_1256 = df_1256.astype(float)
df_0532 = df_0532.astype(float)
df_0616 = df_0616.astype(float)
df_1013 = df_1013.astype(float)
df_1425 = df_1425.astype(float)
df_LHS = df_LHS.astype(float)
df_1610 = df_1610.astype(float)
df_2036 = df_2036.astype(float)

# -------------------------------------------------------------------------------------
# --------- Normalize the spectra to same as before for 1256 --------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_1256[(df_1256['w'] >= 0.825) & (df_1256['w'] <= 0.840)]
norm_df_1256 = df_1256['f']/(np.average(norm_region['f']))

norm_region_0532 = df_0532[(df_0532['w'] >= 0.825) & (df_0532['w'] <= 0.840)]
norm_df_0532 = df_0532['f']/(np.average(norm_region_0532['f']))

norm_region_0616 = df_0616[(df_0616['w'] >= 0.825) & (df_0616['w'] <= 0.840)]
norm_df_0616 = df_0616['f']/(np.average(norm_region_0616['f']))

norm_region_1626 = df_1626[(df_1626['w'] >= 0.825) & (df_1626['w'] <= 0.840)]
norm_df_1626 = df_1626['f']/(np.average(norm_region_1626['f']))

norm_region_1444 = df_1444[(df_1444['w'] >= 0.825) & (df_1444['w'] <= 0.840)]
norm_df_1444 = df_1444['f']/(np.average(norm_region_1444['f']))

norm_region_1013 = df_1013[(df_1013['w'] >= 0.825) & (df_1013['w'] <= 0.840)]
norm_df_1013 = df_1013['f']/(np.average(norm_region_1013['f']))

norm_region_LHS = df_LHS[(df_LHS['w'] >= 0.825) & (df_LHS['w'] <= 0.840)]
norm_df_LHS = df_LHS['f']/(np.average(norm_region_LHS['f']))

norm_region_1425 = df_1425[(df_1425['w'] >= 0.825) & (df_1425['w'] <= 0.840)]
norm_df_1425 = df_1425['f']/(np.average(norm_region_1425['f']))

norm_region_1610 = df_1610[(df_1610['w'] >= 0.825) & (df_1610['w'] <= 0.840)]
norm_df_1610 = df_1610['f']/(np.average(norm_region_1610['f']))

norm_region_2036 = df_2036[(df_2036['w'] >= 0.825) & (df_2036['w'] <= 0.840)]
norm_df_2036 = df_2036['f']/(np.average(norm_region_2036['f']))

# -------------------------------------------------------------------------------------
# --------- Plotting: Comparison of in order of decreasing Teff/ Spt Type -------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8, 10)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
plt.xlim([0.6, 0.9])
plt.ylim([-0.05, 11])

# ------ Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux  ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_0532['w'], norm_df_0532, c='indigo')                                # sdL7 1647
ax1.plot(df_0616['w'], norm_df_0616 + 1.35, c='darkviolet')                          # sdL5 1731
ax1.plot(df_1626['w'], norm_df_1626 + 2.1, c='#531CF7')                               # sdL4 2158
ax1.plot(df_1256['w'], norm_df_1256 + 3, c='k')                                     # sdL3.5  2338
ax1.plot(df_1444['w'], norm_df_1444 + 4, c='mediumblue')                            # sdM9 2359
ax1.plot(df_1013['w'], norm_df_1013 + 5, c='#015DF7')                               # sdM9.5 2457
ax1.plot(df_LHS['w'], norm_df_LHS + 6, c='#01A1D6')                                 # sdM7 2748
ax1.plot(df_1425['w'], norm_df_1425 + 7, c='#09D5D6')                               # sdM8 2822
# ax1.plot(df_HD['w'], norm_df_HD + 7, c='#09D67E')                                 # sd--IRM9 2859
ax1.plot(df_1610['w'], norm_df_1610 + 8, c='#04A57F')                               # sdM7 2878
ax1.plot(df_2036['w'], norm_df_2036 + 9, c='#F7BE0F')                               # sdM7.5 3021
# ax1.plot(df_125614['w'], norm_df_125614, c='#C56201')                         # sdM8


# ------- Label Sources -------------
ax1.text(0.005, 0.04, 'J0532+8246 (sdL7) $T_\mathrm{eff}: 1647 \pm 42$ K ', transform=ax1.transAxes, color='indigo',
         fontsize=12)
ax1.text(0.005, 0.17, 'J0616-6407 (sdL5) $T_\mathrm{eff}: 1730 \pm 280$ K ', transform=ax1.transAxes, color='darkviolet',
         fontsize=12)
ax1.text(0.005, 0.24, 'J1626+3925 (sdL4) $T_\mathrm{eff}: 2115 \pm 22$ K', transform=ax1.transAxes, color='#531CF7',
         fontsize=12)
ax1.text(0.005, 0.34, 'J1256-0224 (sdL3.5) $T_\mathrm{eff}: 2340 \pm 310$ K', transform=ax1.transAxes, color='k',
         fontsize=12)
ax1.text(0.005, 0.43, 'J1444-2019 (sdM9) $T_\mathrm{eff}: 2417 \pm 12$ K', transform=ax1.transAxes, color='mediumblue',
         fontsize=12)
ax1.text(0.005, 0.52, 'J1013-1356 (sdM9.5) $T_\mathrm{eff}: 2545 \pm 31$ K', transform=ax1.transAxes, color='#015DF7',
         fontsize=12)
ax1.text(0.005, 0.615, 'LHS 377 (sdM7) $T_\mathrm{eff}: 2748 \pm 36$ K', transform=ax1.transAxes, color='#01A1D6',
         fontsize=12)
ax1.text(0.005, 0.71, 'J1425+7102 (sdM8) $T_\mathrm{eff}: 2825 \pm 54$ K', transform=ax1.transAxes, color='#09D5D6',
         fontsize=12)
ax1.text(0.005, 0.79, 'J1610-0040 (sdM7) $T_\mathrm{eff}: 2878 \pm 20$ K', transform=ax1.transAxes, color='#04A57F',
         fontsize=12)
ax1.text(0.005, 0.97, 'J2036+5059 (sdM7.5) $T_\mathrm{eff}: 2983 \pm 22$ K', transform=ax1.transAxes, color='#F7BE0F',
         fontsize=12)

# ---- Label Features ------
CaH2 = pd.DataFrame()
CaH2['x'] = [0.635, 0.64]
CaH2['y'] = [9.5, 9.5]
ax1.plot(CaH2['x'], CaH2['y'], color='k')
CaHd2 = pd.DataFrame()
CaHd2['x'] = [0.635, 0.635]
CaHd2['y'] = [9.3, 9.5]
ax1.plot(CaHd2['x'], CaHd2['y'], color='k')
ax1.annotate('CaH', xy=(0.63, 9.55), color='k', fontsize=12)

CaI = pd.DataFrame()
CaI['x'] = [0.65711, 0.65711]
CaI['y'] = [9.4, 9.55]
ax1.plot(CaI['x'], CaI['y'], color='k')
ax1.annotate('Ca$\,$I', xy=(0.651, 9.6), color='k', fontsize=12)

TiO2 = pd.DataFrame()
TiO2['x'] = [0.658, 0.685]
TiO2['y'] = [10, 10]
ax1.plot(TiO2['x'], TiO2['y'], color='k')
ax1.annotate('TiO', xy=(0.665, 10.05), color='k', fontsize=12)

CaH = pd.DataFrame()
CaH['x'] = [0.675, 0.705]
CaH['y'] = [9.55, 9.55]
ax1.plot(CaH['x'], CaH['y'], color='k')
CaHd = pd.DataFrame()
CaHd['x'] = [0.675, 0.675]
CaHd['y'] = [9.3, 9.55]
ax1.plot(CaHd['x'], CaHd['y'], color='k')
ax1.annotate('CaH', xy=(0.675, 9.56), color='k', fontsize=12)

TiO = pd.DataFrame()
TiO['x'] = [0.7053, 0.72]
TiO['y'] = [9.75, 9.755]
ax1.plot(TiO['x'], TiO['y'], color='k')
TiOd = pd.DataFrame()
TiOd['x'] = [0.7053, 0.705]
TiOd['y'] = [9.61, 9.75]
ax1.plot(TiOd['x'], TiOd['y'], color='k')
ax1.annotate('TiO', xy=(0.704, 9.8), color='k', fontsize=12)

KII = pd.DataFrame()
KII['x'] = [0.7665, 0.7665]
KII['y'] = [9.7, 10]
ax1.plot(KII['x'], KII['y'], color='k')
KII2 = pd.DataFrame()
KII2['x'] = [0.7699, 0.7699]
KII2['y'] = [9.7, 10]
ax1.plot(KII2['x'], KII2['y'], color='k')
ax1.annotate('K$\,$I', xy=(0.764, 10.065), color='k', fontsize=12)

Rb1 = pd.DataFrame()
Rb1['x'] = [0.78, 0.78]
Rb1['y'] = [3.4, 3.7]
ax1.plot(Rb1['x'], Rb1['y'], color='k')
ax1.annotate('Rb$\,$I', xy=(0.77, 3.75), color='k', fontsize=12)

Rb = pd.DataFrame()
Rb['x'] = [0.7948, 0.7948]
Rb['y'] = [10, 10.3]
ax1.plot(Rb['x'], Rb['y'], color='k')
ax1.annotate('Rb$\,$I', xy=(0.785, 10.35), color='k', fontsize=12)

NaI = pd.DataFrame()
NaI['x'] = [0.8183, 0.8183]
NaI['y'] = [10.1, 10.5]
ax1.plot(NaI['x'], NaI['y'], color='k', linewidth=0.5)
NaI2 = pd.DataFrame()
NaI2['x'] = [0.8195, 0.8195]
NaI2['y'] = [10.1, 10.5]
ax1.plot(NaI2['x'], NaI2['y'], color='k', linewidth=0.5)
ax1.annotate('NaI', xy=(0.81, 10.55), color='k', fontsize=12)

TiI = pd.DataFrame()
TiI['x'] = [0.844, 0.844]
TiI['y'] = [9.4, 9.6]
ax1.plot(TiI['x'], TiI['y'], color='k')
ax1.annotate('Ti$\,$I', xy=(0.836, 9.1), color='k', fontsize=12)

CsI = pd.DataFrame()
CsI['x'] = [0.8521, 0.8521]
CsI['y'] = [10.1, 10.4]
ax1.plot(CsI['x'], CsI['y'], color='k')
ax1.annotate('Cs$\,$I', xy=(0.845, 10.45), color='k', fontsize=12)

CrH = pd.DataFrame()
CrH['x'] = [0.8611, 0.865]
CrH['y'] = [4.5, 4.5]
ax1.plot(CrH['x'], CrH['y'], color='k')
CrHd = pd.DataFrame()
CrHd['x'] = [0.8611, 0.8611]
CrHd['y'] = [4.3, 4.5]
ax1.plot(CrHd['x'], CrHd['y'], color='k')
ax1.annotate('CrH', xy=(0.85, 4.55), color='k', fontsize=12)

FeH = pd.DataFrame()
FeH['x'] = [0.8692, 0.875]
FeH['y'] = [4.2, 4.2]
ax1.plot(FeH['x'], FeH['y'], color='k')
FeH = pd.DataFrame()
FeH['x'] = [0.8692, 0.8692]
FeH['y'] = [4, 4.2]
ax1.plot(FeH['x'], FeH['y'], color='k')
ax1.annotate('FeH', xy=(0.865, 4.25), color='k', fontsize=12)

plt.tight_layout()
plt.savefig('Plots/Subdwarfs_redoptical_split.png')
