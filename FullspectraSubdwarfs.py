import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
# None for 1256-1408, and 1425 can't be normalized in this region, choosing to show HD instead.

df_1256 = pd.read_csv('Data/Smoothed_data/Subdwarfs_overall_smoothed/correctpi1256-0224 (L3.5sd) SED_smoothed.txt',
                      sep=",", comment='#', header=None, names=["w", "f", "err"])

# -------------- Subdwarfs ----------------------------------
df_0532 = pd.read_csv('Data/Scaled0532+8246 (L7sd) SED.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_0616 = pd.read_csv('Data/X-shooter0616-6407 (L5sd) SED.txt', sep=" ",
                      comment='#', header=None, names=["w", "f", "err"])
df_1013 = pd.read_csv('Data/Smoothed_data/Subdwarfs_overall_smoothed/1013-1356 (M9.5sd) SED_smoothed.txt', sep=",",
                      comment='#', header=None, names=["w", "f", "err"])
# df_125614 = pd.read_csv('', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_HD = pd.read_csv('Data/HD114762B (M9sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
# df_1425 = pd.read_csv('Data/1425+7102 (M8sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_LHS = pd.read_csv('Data/Smoothed_data/Subdwarfs_overall_smoothed/1439+1839 (M7sd) SED_smoothed.txt', sep=",",
                     comment='#', header=None, names=["w", "f", "err"])
df_1444 = pd.read_csv('Data/1444-2019 (M9sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1610 = pd.read_csv('Data/Smoothed_data/Subdwarfs_overall_smoothed/1610-0040 (M7sd) SED_smoothed.txt', sep=",",
                      comment='#', header=None, names=["w", "f", "err"])
df_1626 = pd.read_csv('Data/1626+3925 (L4sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_2036 = pd.read_csv('Data/Smoothed_data/Subdwarfs_overall_smoothed/2036+5059 (M7.5sd) SED_smoothed.txt', sep=",",
                      comment='#', header=None, names=["w", "f", "err"])

# ------------------------------------------------------------------------------------
# ------------------- Fix files to read all columns as Floats-------------------------
# ------------------------------------------------------------------------------------
df_1256 = df_1256.astype(float)
df_0532 = df_0532.astype(float)
df_0616 = df_0616.astype(float)
df_1013 = df_1013.astype(float)
df_LHS = df_LHS.astype(float)
df_1610 = df_1610.astype(float)
df_2036 = df_2036.astype(float)

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
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
plt.xlim([0.6, 2.35])
plt.ylim([0, 6.65])

# ------ Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
ax1.xaxis.set_major_locator(plt.FixedLocator([0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2]))
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

# -------- Label a few features --------------
KII = pd.DataFrame()
KII['x'] = [0.76, 0.76]
KII['y'] = [6, 6.25]
ax1.plot(KII['x'], KII['y'], color='k')
KII2 = pd.DataFrame()
KII2['x'] = [0.7699, 0.7699]
KII2['y'] = [6, 6.25]
ax1.plot(KII2['x'], KII2['y'], color='k')
ax1.annotate('K$\,$I', xy=(0.74, 6.3), color='k', fontsize=12)

CrH = pd.DataFrame()
CrH['x'] = [0.8611, 0.9]
CrH['y'] = [6.25, 6.25]
ax1.plot(CrH['x'], CrH['y'], color='k')
CrHd = pd.DataFrame()
CrHd['x'] = [0.8611, 0.8611]
CrHd['y'] = [6, 6.25]
ax1.plot(CrHd['x'], CrHd['y'], color='k')
ax1.annotate('CrH', xy=(0.85, 6.3), color='k', fontsize=12)

CrH2 = pd.DataFrame()
CrH2['x'] = [0.9969, 1.05]
CrH2['y'] = [6.35, 6.35]
ax1.plot(CrH2['x'], CrH2['y'], color='k')
CrHd2 = pd.DataFrame()
CrHd2['x'] = [0.9969, 0.9969]
CrHd2['y'] = [6.15, 6.35]
ax1.plot(CrHd2['x'], CrHd2['y'], color='k')
ax1.annotate('CrH, FeH', xy=(0.996, 6.38), color='k', fontsize=12)

H2O = pd.DataFrame()
H2O['x'] = [1.3, 1.51]
H2O['y'] = [6.35, 6.35]
ax1.plot(H2O['x'], H2O['y'], color='k')
H2Od = pd.DataFrame()
H2Od['x'] = [1.3, 1.3]
H2Od['y'] = [6.2, 6.35]
ax1.plot(H2Od['x'], H2Od['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.35, 6.4), color='k', fontsize=12)

CIA = pd.DataFrame()
CIA['x'] = [1.8, 2.8]
CIA['y'] = [6.35, 6.35]
ax1.plot(CIA['x'], CIA['y'], color='k')
ax1.annotate('CIA H$_\mathrm{2} $', xy=(2, 6.4), color='k', fontsize=12)

# ------- Label Sources -------------
# not alot of space to label
ax1.text(0.73, 0.12, 'J0532+8246 (sdL7)', transform=ax1.transAxes, color='indigo', fontsize=12)
ax1.text(0.73, 0.08, '$T_\mathrm{eff}: 1664 \pm 24$ K ', transform=ax1.transAxes, color='indigo',fontsize=12)
ax1.text(0.73, 0.38, 'J0616-6407 (sdL5)', transform=ax1.transAxes, color='darkviolet', fontsize=12)
ax1.text(0.73, 0.34, '$T_\mathrm{eff}: 1720 \pm 280$ K ', transform=ax1.transAxes, color='darkviolet',fontsize=12)
ax1.text(0.73, 0.54, 'J1626+3925 (sdL4)', transform=ax1.transAxes, color='#531CF7', fontsize=12)
ax1.text(0.73, 0.5, '$T_\mathrm{eff}: 2148 \pm 14$ K', transform=ax1.transAxes, color='#531CF7', fontsize=12)
ax1.text(0.73, 0.68, 'J1256-0224 (sdL3.5)', transform=ax1.transAxes, color='k', fontsize=12)
ax1.text(0.73, 0.64, '$T_\mathrm{eff}: 2307 \pm 71$ K', transform=ax1.transAxes, color='k', fontsize=12)
ax1.text(0.73, 0.86, 'J1444-2019 (sdM9)', transform=ax1.transAxes, color='mediumblue', fontsize=12)
ax1.text(0.73, 0.82, '$T_\mathrm{eff}: 2477 \pm 13$ K', transform=ax1.transAxes, color='mediumblue', fontsize=12)

plt.tight_layout()
plt.savefig('Plots/Subdwarfs_secondpannel.png', dpi=150)

# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8, 10)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
plt.xlim([0.6, 2.35])
plt.ylim([0, 5.55])

# ------ Axes Labels --------
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)
ax1.xaxis.set_major_locator(plt.FixedLocator([0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2]))
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

# -------- Label a few features --------------
KII = pd.DataFrame()
KII['x'] = [0.76, 0.76]
KII['y'] = [4.75, 5]
ax1.plot(KII['x'], KII['y'], color='k')
KII2 = pd.DataFrame()
KII2['x'] = [0.7699, 0.7699]
KII2['y'] = [4.75, 5]
ax1.plot(KII2['x'], KII2['y'], color='k')
ax1.annotate('K$\,$I', xy=(0.74, 5.1), color='k', fontsize=12)

CrH = pd.DataFrame()
CrH['x'] = [0.8611, 0.9]
CrH['y'] = [5.25, 5.25]
ax1.plot(CrH['x'], CrH['y'], color='k')
CrHd = pd.DataFrame()
CrHd['x'] = [0.8611, 0.8611]
CrHd['y'] = [5, 5.25]
ax1.plot(CrHd['x'], CrHd['y'], color='k')
ax1.annotate('CrH', xy=(0.85, 5.3), color='k', fontsize=12)

CrH2 = pd.DataFrame()
CrH2['x'] = [0.9969, 1.05]
CrH2['y'] = [5.25, 5.25]
ax1.plot(CrH2['x'], CrH2['y'], color='k')
CrHd2 = pd.DataFrame()
CrHd2['x'] = [0.9969, 0.9969]
CrHd2['y'] = [5.1, 5.25]
ax1.plot(CrHd2['x'], CrHd2['y'], color='k')
ax1.annotate('CrH, FeH', xy=(0.996, 5.3), color='k', fontsize=12)

H2O = pd.DataFrame()
H2O['x'] = [1.3, 1.51]
H2O['y'] = [5.25, 5.25]
ax1.plot(H2O['x'], H2O['y'], color='k')
H2Od = pd.DataFrame()
H2Od['x'] = [1.3, 1.3]
H2Od['y'] = [5.1, 5.25]
ax1.plot(H2Od['x'], H2Od['y'], color='k')
ax1.annotate('H$_\mathrm{2} $O', xy=(1.35, 5.3), color='k', fontsize=12)

CIA = pd.DataFrame()
CIA['x'] = [1.8, 2.8]
CIA['y'] = [5.25, 5.25]
ax1.plot(CIA['x'], CIA['y'], color='k')
ax1.annotate('CIA H$_\mathrm{2} $', xy=(2, 5.3), color='k', fontsize=12)

# ------- Label Sources -------------
ax1.text(0.72, 0.11, 'J1013-1356 (sdM9.5)', transform=ax1.transAxes, color='#015DF7', fontsize=12)
ax1.text(0.72, 0.07, '$T_\mathrm{eff}: 2621 \pm 22$ K', transform=ax1.transAxes, color='#015DF7', fontsize=12)
ax1.text(0.72, 0.29, 'LHS 377 (sdM7)', transform=ax1.transAxes, color='#01A1D6',  fontsize=12)
ax1.text(0.72, 0.25, '$T_\mathrm{eff}: 2839 \pm 6$ K', transform=ax1.transAxes, color='#01A1D6', fontsize=12)
ax1.text(0.72, 0.52, 'HD114762$\,$B (d/sdM9)', transform=ax1.transAxes, color='#09D67E', fontsize=12)
ax1.text(0.72, 0.48, '$T_\mathrm{eff}: 2894 \pm 24$ K', transform=ax1.transAxes, color='#09D67E', fontsize=12)
ax1.text(0.72, 0.70, 'J1610-0040 (sdM7)', transform=ax1.transAxes, color='#04A57F', fontsize=12)
ax1.text(0.72, 0.66, '$T_\mathrm{eff}: 2890 \pm 20$ K', transform=ax1.transAxes, color='#04A57F', fontsize=12)
ax1.text(0.72, 0.84, 'J2036+5059 (sdM7.5)', transform=ax1.transAxes, color='#F7BE0F', fontsize=12)
ax1.text(0.72, 0.8, '$T_\mathrm{eff}: 2983 \pm 22$ K', transform=ax1.transAxes, color='#F7BE0F',fontsize=12)

plt.tight_layout()
plt.savefig('Plots/Subdwarfs_firstpannel.png', dpi=150)
