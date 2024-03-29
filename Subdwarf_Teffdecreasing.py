import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.patches as mpatches

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_1256 = pd.read_csv('Data/Gaia1256-0224 (L3.5sd) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_1256_phot = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) phot.txt', sep=" ", header=1, names=["w", "f", "err"])

# -------------- Subdwarfs ----------------------------------
df_0532 = pd.read_csv('Data/0532+8246 (L7sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_0532_phot = pd.read_csv('Data/0532+8246 (L7sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_0616 = pd.read_csv('Data/0616-6407 (L5sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_0616_phot = pd.read_csv('Data/0616-6407 (L5sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_1013 = pd.read_csv('Data/1013-1356 (-) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1013_phot = pd.read_csv('Data/1013-1356 (-) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

# df_125614 = pd.read_csv('', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_HD = pd.read_csv('Data/HD114762B (M9sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_HD_phot = pd.read_csv('Data/HD114762B (M9sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_1425 = pd.read_csv('Data/1425+7102 (M8sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1425_phot = pd.read_csv('Data/1425+7102 (M8sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_LHS = pd.read_csv('Data/1439+1839 (M7sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_LHS_phot = pd.read_csv('Data/1439+1839 (M7sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_1444 = pd.read_csv('Data/1444-2019 (M9sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1444_phot = pd.read_csv('Data/1444-2019 (M9sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_1610 = pd.read_csv('Data/1610-0040 (M7sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1610_phot = pd.read_csv('Data/1610-0040 (M7sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_1626 = pd.read_csv('Data/1626+3925 (L4sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1626_phot = pd.read_csv('Data/1626+3925 (L4sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_2036 = pd.read_csv('Data/2036+5059 (M7.5sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_2036_phot = pd.read_csv('Data/2036+5059 (M7.5sd) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# ---------------------- Remove Tails ------------------------------------------------
# -------------------------------------------------------------------------------------
df_HD = df_HD[(df_HD['w'] > 0.91) & (df_HD['w'] <= 3)]

# -------------------------------------------------------------------------------------
# --------- Plotting: Comparison of in order of decreasing Teff/ Spt Type -------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(11.71, 7.43)   # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

# -------- Add data -----------
ax1.loglog(df_0532['w'], df_0532['f'], c='indigo')                                 # sdL7 1647
ax1.scatter(df_0532_phot['w'], df_0532_phot['f'], c='k', s=70)
ax1.scatter(df_0532_phot['w'], df_0532_phot['f'], c='indigo', s=50)

ax1.loglog(df_0616['w'], df_0616['f'], c='darkviolet')                             # sdL5 1668
ax1.scatter(df_0616_phot['w'], df_0616_phot['f'], c='k', s=70)
ax1.scatter(df_0616_phot['w'], df_0616_phot['f'], c='darkviolet', s=50)

ax1.loglog(df_1626['w'], df_1626['f'], c='#531CF7')                                # sdL4 2158
ax1.scatter(df_1626_phot['w'], df_1626_phot['f'], c='k', s=70)
ax1.scatter(df_1626_phot['w'], df_1626_phot['f'], c='#531CF7', s=50)

ax1.loglog(df_1444['w'], df_1444['f'], c='mediumblue')                             # sdM9 2303
ax1.scatter(df_1444_phot['w'], df_1444_phot['f'], c='k', s=70)
ax1.scatter(df_1444_phot['w'], df_1444_phot['f'], c='mediumblue', s=50)

ax1.loglog(df_1256['w'], df_1256['f'], c='k')                                      # sdL3.5  2338
ax1.scatter(df_1256_phot['w'], df_1256_phot['f'], c='k', s=70)
ax1.scatter(df_1256_phot['w'], df_1256_phot['f'], c='k', s=50)

ax1.loglog(df_1013['w'], df_1013['f'], c='#015DF7')                               # sdM9.5 2457
ax1.scatter(df_1013_phot['w'], df_1013_phot['f'], c='k', s=70)
ax1.scatter(df_1013_phot['w'], df_1013_phot['f'], c='#015DF7', s=50)

ax1.loglog(df_LHS['w'], df_LHS['f'], c='#01A1D6')                                 # sdM7 2775
ax1.scatter(df_LHS_phot['w'], df_LHS_phot['f'], c='k', s=70)
ax1.scatter(df_LHS_phot['w'], df_LHS_phot['f'], c='#01A1D6', s=50)

ax1.loglog(df_1425['w'], df_1425['f'], c='#09D5D6')                               # sdM8 2823
ax1.scatter(df_1425_phot['w'], df_1425_phot['f'], c='k', s=70)
ax1.scatter(df_1425_phot['w'], df_1425_phot['f'], c='#09D5D6', s=50)

ax1.loglog(df_1610['w'], df_1610['f'], c='#04A57F')                               # sdM7 2852
ax1.scatter(df_1610_phot['w'], df_1610_phot['f'], c='k', s=70)
ax1.scatter(df_1610_phot['w'], df_1610_phot['f'], c='#04A513', s=50)

ax1.loglog(df_HD['w'], df_HD['f'], c='#09D67E')                                   # sd--IRM9 2859
ax1.scatter(df_HD_phot['w'], df_HD_phot['f'], c='k', s=70)
ax1.scatter(df_HD_phot['w'], df_HD_phot['f'], c='#09D67E', s=50)

ax1.loglog(df_2036['w'], df_2036['f'], c='#F7BE0F')                               # sdM7.5 3049
ax1.scatter(df_2036_phot['w'], df_2036_phot['f'], c='k', s=70)
ax1.scatter(df_2036_phot['w'], df_2036_phot['f'], c='#F7BE0F', s=50)

# ax1.loglog(df_125614['w'], df_125614['f'], c='#C56201')                         # sdM8
# ax1.scatter(df_125614_phot['w'], df_125614_phot['f'], c='k', s=70)
# ax1.scatter(df_125614_phot['w'], df_125614_phot['f'], c='#C56201', s=50)

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.33, 15])
plt.ylim([6*10**(-20), 4*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.35, 0.6, 2, 3]))
ax1.tick_params(axis='x', which='major', labelsize=20)
ax1.tick_params(axis='x', which='minor', labelsize=20)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($erg\ s^{-1} cm^{-2} A^{-1}$)', fontsize=25)


# Label Sources
spec_0532 = mpatches.Patch(color='indigo', label='0532+8246')
spec_0616 = mpatches.Patch(color='darkviolet', label='0616-6407')
spec_1626 = mpatches.Patch(color='#531CF7', label='1626+3925')
spec_1444 = mpatches.Patch(color='mediumblue', label='1444-2019')
spec_1256 = mpatches.Patch(color='k', label='1256-0224')
spec_1013 = mpatches.Patch(color='#015DF7', label='1013-1356')
spec_LHS = mpatches.Patch(color='#01A1D6', label='LHS 377')
spec_1425 = mpatches.Patch(color='#09D5D6', label='1425+7102')
spec_1610 = mpatches.Patch(color='#04A57F', label='1610-0040')
spec_HD = mpatches.Patch(color='#09D67E', label='HD114762B')
spec_2036 = mpatches.Patch(color='#F7BE0F', label='2036+5059')
spec_125614 = mpatches.Patch(color='#C56201', label='1256-1408')
ax1.legend(handles=[spec_0532, spec_0616, spec_1626, spec_1444, spec_1256, spec_1013, spec_LHS, spec_1425, spec_1610,
                    spec_HD, spec_2036, spec_125614])

plt.savefig('Plots/Subdwarfs_nonnormalized.png')
