import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
# Not reading in HD114662B because only has NIR spectrum, None for 1256-1408, and problem for 0616

df_1256 = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# -------------- Subdwarfs ----------------------------------
df_0532 = pd.read_csv('Data/0532+8246 (L7sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_0616 = pd.read_csv('Data/0616-6407 (L5sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1013 = pd.read_csv('Data/1013-1356 (-) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
# df_125614 = pd.read_csv('', sep=" ", comment='#', header=None, names=["w", "f", "err"])
# df_HD = pd.read_csv('Data/HD114762B (M9sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1425 = pd.read_csv('Data/1425+7102 (M8sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_LHS = pd.read_csv('Data/1439+1839 (M7sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1444 = pd.read_csv('Data/1444-2019 (M9sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1610 = pd.read_csv('Data/1610-0040 (M7sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1626 = pd.read_csv('Data/1626+3925 (L4sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_2036 = pd.read_csv('Data/2036+5059 (M7.5sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ---------------------- Remove Tails ------------------------------------------------
# -------------------------------------------------------------------------------------
# df_HD = df_HD[(df_HD['w'] > 0.91) & (df_HD['w'] <= 3)]

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

# norm_region_HD = df_HD[(df_HD['w'] >= 0.825) & (df_HD['w'] <= 0.840)]
# norm_df_HD = df_HD['f']/(np.average(norm_region_HD['f']))

norm_region_2036 = df_2036[(df_2036['w'] >= 0.825) & (df_2036['w'] <= 0.840)]
norm_df_2036 = df_2036['f']/(np.average(norm_region_2036['f']))

# norm_region_125614 = df_125614[(df_125614['w'] >= 0.825) & (df_125614['w'] <=0.840)]
# norm_df_125614 = df_125614['f']/(np.average(norm_region_125614['f']))

# -------------------------------------------------------------------------------------
# --------- Plotting: Comparison of in order of decreasing Teff/ Spt Type -------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8, 10)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.6, 0.9])
plt.ylim([-0.05, 9.5])

# ------ Axes Labels --------
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Normalized Flux  ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_0532['w'], norm_df_0532, c='indigo')                                # sdL7 1647
ax1.plot(df_0616['w'], norm_df_0616 + 1, c='darkviolet')                          # sdL5 ???
ax1.plot(df_1626['w'], norm_df_1626 + 2, c='#531CF7')                               # sdL4 2158
ax1.plot(df_1444['w'], norm_df_1444 + 3, c='mediumblue')                            # sdM9 2303
ax1.plot(df_1256['w'], norm_df_1256 + 4, c='k')                                     # sdL3.5  2338
ax1.plot(df_1013['w'], norm_df_1013 + 5, c='#015DF7')                               # sdM9.5 2457
ax1.plot(df_LHS['w'], norm_df_LHS + 6, c='#01A1D6')                                 # sdM7 2824
# ax1.plot(df_1425['w'], norm_df_1425, c='#09D5D6')                               # sdM8 2823
ax1.plot(df_1610['w'], norm_df_1610 + 7, c='#04A57F')                               # sdM7 2852
# ax1.plot(df_HD['w'], norm_df_HD + 7, c='#09D67E')                                   # sd--IRM9 2859
ax1.plot(df_2036['w'], norm_df_2036 + 8, c='#F7BE0F')                               # sdM7.5 3049
# ax1.plot(df_125614['w'], norm_df_125614, c='#C56201')                         # sdM8


# ------- Label Sources -------------
ax1.text(0, 0.04, '0532+8246 (sdL7) T$_\mathrm{eff}: 1647 \pm 42$ K ', transform=ax1.transAxes, color='indigo',
         fontsize=12)
ax1.text(0, 0.16, '0616-6407 (sdL5) T$_\mathrm{eff}: 1668 \pm 284$ K ', transform=ax1.transAxes, color='darkviolet',
         fontsize=12)
ax1.text(0, 0.27, '1626+3925 (sdL4) T$_\mathrm{eff}: 2158 \pm 41$ K', transform=ax1.transAxes, color='#531CF7',
         fontsize=12)
ax1.text(0, 0.39, '1444-2019 (sdM9) T$_\mathrm{eff}: 2303 \pm 67$ K', transform=ax1.transAxes, color='mediumblue',
         fontsize=12)
ax1.text(0, 0.48, '1256-0224 (sdL3.5) T$_\mathrm{eff}: 2338 \pm 313$ K', transform=ax1.transAxes, color='k',
         fontsize=12)
ax1.text(0, 0.6, '1013-1356 (sdM9.5) T$_\mathrm{eff}: 2457 \pm 124$ K', transform=ax1.transAxes, color='#015DF7',
         fontsize=12)
ax1.text(0, 0.76, 'LHS 377 (sdM7) T$_\mathrm{eff}: 2824 \pm 37$ K', transform=ax1.transAxes, color='#01A1D6',
         fontsize=12)
ax1.text(0, 0.82, '1610-0040 (sdM7) T$_\mathrm{eff}: 2852 \pm 20$ K', transform=ax1.transAxes, color='#04A57F',
         fontsize=12)
ax1.text(0, 0.92, '2036+5059 (sdM7.5) T$_\mathrm{eff}: 3049 \pm 108$ K', transform=ax1.transAxes, color='#F7BE0F',
         fontsize=12)

# ---- Label Features ------

CaH = pd.DataFrame()
CaH['x'] = [0.69, 0.69]
CaH['y'] = [6.42, 6.75]
ax1.plot(CaH['x'], CaH['y'], color='k')
ax1.text(0.27, 0.72, 'CaH', transform=ax1.transAxes, color='k', fontsize=12)

TiO = pd.DataFrame()
TiO['x'] = [0.715, 0.715]
TiO['y'] = [6.45, 6.75]
ax1.plot(TiO['x'], TiO['y'], color='k')
ax1.text(0.36, 0.72, 'TiO', transform=ax1.transAxes, color='k', fontsize=12)

KII = pd.DataFrame()
KII['x'] = [0.767, 0.767]
KII['y'] = [6.7, 7]
ax1.plot(KII['x'], KII['y'], color='k')
ax1.text(0.54, 0.75, 'K II', transform=ax1.transAxes, color='k', fontsize=12)

Rb = pd.DataFrame()
Rb['x'] = [0.795, 0.795]
Rb['y'] = [5, 5.5]
ax1.plot(Rb['x'], Rb['y'], color='k')
ax1.text(0.62, 0.5, 'Rb', transform=ax1.transAxes, color='k', fontsize=12)


ax1.text(0.71, 0.35, 'NaI', transform=ax1.transAxes, color='k', fontsize=12)

CrH = pd.DataFrame()
CrH['x'] = [0.864, 0.864]
CrH['y'] = [5, 5.3]
ax1.plot(CrH['x'], CrH['y'], color='k')
ax1.text(0.84, 0.57, 'CrH', transform=ax1.transAxes, color='k', fontsize=12)

FeH = pd.DataFrame()
FeH['x'] = [0.872, 0.872]
FeH['y'] = [5, 5.3]
ax1.plot(FeH['x'], FeH['y'], color='k')
ax1.text(0.9, 0.57, 'FeH', transform=ax1.transAxes, color='k', fontsize=12)

plt.savefig('Plots/Subdwarfs_redoptical_split.png')
