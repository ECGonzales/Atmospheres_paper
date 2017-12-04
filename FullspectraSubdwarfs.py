import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
# None for 1256-1408, and 1425 can't be normalized in this region, choosing to show HD instead.

df_1256 = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# -------------- Subdwarfs ----------------------------------
df_0532 = pd.read_csv('Data/0532+8246 (L7sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_0616 = pd.read_csv('Data/0616-6407 (L5sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1013 = pd.read_csv('Data/1013-1356 (-) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
# df_125614 = pd.read_csv('', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_HD = pd.read_csv('Data/HD114762B (M9sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
# df_1425 = pd.read_csv('Data/1425+7102 (M8sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_LHS = pd.read_csv('Data/1439+1839 (M7sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1444 = pd.read_csv('Data/1444-2019 (M9sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1610 = pd.read_csv('Data/1610-0040 (M7sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1626 = pd.read_csv('Data/1626+3925 (L4sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_2036 = pd.read_csv('Data/2036+5059 (M7.5sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ---------------------- Remove Tails ------------------------------------------------
# -------------------------------------------------------------------------------------
df_HD = df_HD[(df_HD['w'] > 0.91) & (df_HD['w'] <= 3)]

# -------------------------------------------------------------------------------------
# --------- Normalize the spectra to same as before for 1256 --------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_1256[(df_1256['w'] >= 0.98) & (df_1256['w'] <= 0.988)]
norm_df_1256 = df_1256['f']/(np.average(norm_region['f']))

norm_region_0532 = df_0532[(df_0532['w'] >= 0.98) & (df_0532['w'] <= 0.988)]
norm_df_0532 = df_0532['f']/(np.average(norm_region_0532['f']))

norm_region_0616 = df_0616[(df_0616['w'] >= 0.98) & (df_0616['w'] <= 0.988)]
norm_df_0616 = df_0616['f']/(np.average(norm_region_0616['f']))

norm_region_1626 = df_1626[(df_1626['w'] >= 0.98) & (df_1626['w'] <= 0.988)]
norm_df_1626 = df_1626['f']/(np.average(norm_region_1626['f']))

norm_region_1444 = df_1444[(df_1444['w'] >= 0.98) & (df_1444['w'] <= 0.988)]
norm_df_1444 = df_1444['f']/(np.average(norm_region_1444['f']))

norm_region_1013 = df_1013[(df_1013['w'] >= 0.98) & (df_1013['w'] <= 0.988)]
norm_df_1013 = df_1013['f']/(np.average(norm_region_1013['f']))

norm_region_LHS = df_LHS[(df_LHS['w'] >= 0.98) & (df_LHS['w'] <= 0.988)]
norm_df_LHS = df_LHS['f']/(np.average(norm_region_LHS['f']))

# norm_region_1425 = df_1425[(df_1425['w'] >= 0.90) & (df_1425['w'] <= 0.91)] region that works fro 1425 but not HD
# norm_df_1425 = df_1425['f']/(np.average(norm_region_1425['f']))

norm_region_1610 = df_1610[(df_1610['w'] >= 0.98) & (df_1610['w'] <= 0.988)]
norm_df_1610 = df_1610['f']/(np.average(norm_region_1610['f']))

norm_region_HD = df_HD[(df_HD['w'] >= 0.98) & (df_HD['w'] <= 0.988)]
norm_df_HD = df_HD['f']/(np.average(norm_region_HD['f']))

norm_region_2036 = df_2036[(df_2036['w'] >= 0.98) & (df_2036['w'] <= 0.988)]
norm_df_2036 = df_2036['f']/(np.average(norm_region_2036['f']))

# norm_region_125614 = df_125614[(df_125614['w'] >= 1.29) & (df_125614['w'] <= 1.31)]
# norm_df_125614 = df_125614['f']/(np.average(norm_region_125614['f']))

# -------------------------------------------------------------------------------------
# --------- Plotting: Comparison of in order of decreasing Teff/ Spt Type -------------
# -------------------------------------------------------------------------------------

# ------- Not enough detail if in one figure => make two ------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8, 10)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.6, 2.35])
plt.ylim([0, 6.25])

# ------ Axes Labels --------
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_0532['w'], norm_df_0532, c='indigo')                                # sdL7 1647
ax1.plot(df_0616['w'], norm_df_0616 + 2, c='darkviolet')                        # sdL5 1731
ax1.plot(df_1626['w'], norm_df_1626 + 3, c='#531CF7')                           # sdL4 2158
ax1.plot(df_1256['w'], norm_df_1256 + 4, c='k')                                 # sdL3.5  2344
ax1.plot(df_1444['w'], norm_df_1444 + 5, c='mediumblue')                        # sdM9 2359
# ax1.plot(df_1013['w'], norm_df_1013 + 5, c='#015DF7')                         # sdM9.5 2457
# ax1.plot(df_LHS['w'], norm_df_LHS + 6, c='#01A1D6')                           # sdM7 2748
# # ax1.plot(df_1425['w'], norm_df_1425, c='#09D5D6')                           # sdM8 2822      only MIR spectra
# ax1.plot(df_HD['w'], norm_df_HD + 8, c='#09D67E')                             # sd--IRM9 2859
# ax1.plot(df_1610['w'], norm_df_1610 + 7, c='#04A57F')                         # sdM7 2878
# ax1.plot(df_2036['w'], norm_df_2036 + 9, c='#F7BE0F')                         # sdM7.5 3021
# # ax1.plot(df_125614['w'], norm_df_125614, c='#C56201')                         # sdM8

# ------- Label Sources -------------
# not alot of space to label
ax1.text(0.73, 0.12, 'J0532+8246 (sdL7)', transform=ax1.transAxes, color='indigo', fontsize=12)
ax1.text(0.73, 0.08, '$T_\mathrm{eff}: 1647 \pm 42$ K ', transform=ax1.transAxes, color='indigo',fontsize=12)
ax1.text(0.73, 0.4, 'J0616-6407 (sdL5)', transform=ax1.transAxes, color='darkviolet', fontsize=12)
ax1.text(0.73, 0.36, '$T_\mathrm{eff}: 1731 \pm 283$ K ', transform=ax1.transAxes, color='darkviolet',fontsize=12)
ax1.text(0.73, 0.56, 'J1626+3925 (sdL4)', transform=ax1.transAxes, color='#531CF7', fontsize=12)
ax1.text(0.73, 0.52, '$T_\mathrm{eff}: 2158 \pm 41$ K', transform=ax1.transAxes, color='#531CF7', fontsize=12)
ax1.text(0.73, 0.72, 'J1256-0224 (sdL3.5)', transform=ax1.transAxes, color='k', fontsize=12)
ax1.text(0.73, 0.68, '$T_\mathrm{eff}: 2344 \pm 314$ K', transform=ax1.transAxes, color='k', fontsize=12)
ax1.text(0.73, 0.90, 'J1444-2019 (sdM9)', transform=ax1.transAxes, color='mediumblue', fontsize=12)
ax1.text(0.73, 0.86, '$T_\mathrm{eff}: 2363 \pm 42$ K', transform=ax1.transAxes, color='mediumblue', fontsize=12)

plt.savefig('Plots/Subdwarfs_secondpannel.png')

# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8, 10)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.6, 2.35])
plt.ylim([0, 5.15])

# ------ Axes Labels --------
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_1013['w'], norm_df_1013, c='#015DF7')                         # sdM9.5 2457
ax1.plot(df_LHS['w'], norm_df_LHS + 1, c='#01A1D6')                       # sdM7 2748
# ax1.plot(df_1425['w'], norm_df_1425 + 2, c='#09D5D6')                   # sdM8 2822
ax1.plot(df_HD['w'], norm_df_HD + 2, c='#09D67E')                         # sd--IRM9 2859
ax1.plot(df_1610['w'], norm_df_1610 + 3, c='#04A57F')                     # sdM7 2878
ax1.plot(df_2036['w'], norm_df_2036 + 4, c='#F7BE0F')                     # sdM7.5 3021
# ax1.plot(df_125614['w'], norm_df_125614, c='#C56201')                         # sdM8

# ------- Label Sources -------------
ax1.text(0.72, 0.11, 'J1013-1356 (sdM9.5)', transform=ax1.transAxes, color='#015DF7', fontsize=12)
ax1.text(0.72, 0.07, '$T_\mathrm{eff}: 2457 \pm 124$ K', transform=ax1.transAxes, color='#015DF7', fontsize=12)
ax1.text(0.72, 0.31, 'LHS 377 (sdM7)', transform=ax1.transAxes, color='#01A1D6',  fontsize=12)
ax1.text(0.72, 0.27, '$T_\mathrm{eff}: 2748 \pm 36$ K', transform=ax1.transAxes, color='#01A1D6', fontsize=12)
ax1.text(0.7, 0.55, 'HD114762$\,$B (d/sdM9)', transform=ax1.transAxes, color='#09D67E', fontsize=12)
ax1.text(0.72, 0.51, '$T_\mathrm{eff}: 2859 \pm 50$ K', transform=ax1.transAxes, color='#09D67E', fontsize=12)
ax1.text(0.72, 0.74, 'J1610-0040 (sdM7)', transform=ax1.transAxes, color='#04A57F', fontsize=12)
ax1.text(0.72, 0.7, '$T_\mathrm{eff}: 2878 \pm 20$ K', transform=ax1.transAxes, color='#04A57F', fontsize=12)
ax1.text(0.7, 0.9, 'J2036+5059 (sdM7.5)', transform=ax1.transAxes, color='#F7BE0F', fontsize=12)
ax1.text(0.72, 0.86, '$T_\mathrm{eff}: 3021 \pm 102$ K', transform=ax1.transAxes, color='#F7BE0F',fontsize=12)

plt.savefig('Plots/Subdwarfs_firstpannel.png')
