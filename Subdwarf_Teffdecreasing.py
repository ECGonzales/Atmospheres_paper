import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_1256 = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
df_1256_phot = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) phot.txt', sep=" ", header=1, names=["w", "f", "err"])

# -------------- Subdwarfs ----------------------------------
df_0532 = pd.read_csv('Data/0532+8246 (L7sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_0532_phot = pd.read_csv('Data/0532+8246 (L7sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

# df_0616 = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) SED.txt', sep=" ", comment='#', header=None,
#                       names=["w", "f", "err"])
# df_0616_phot = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) SED.txt', sep=" ", comment='#', header=None,
#                       names=["w", "f", "err"])

df_1013 = pd.read_csv('Data/1013-1356 (-) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1013_phot = pd.read_csv('Data/1013-1356 (-) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

#df_125614 = pd.read_csv('', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_HD = pd.read_csv('Data/HD114762B (M9sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_HD_phot = pd.read_csv('Data/HD114762B (M9sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_1425 = pd.read_csv('Data/1425+7102 (M8sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1425_phot = pd.read_csv('Data/1425+7102 (M8sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_LHS = pd.read_csv('Data/1439+1839 (M7sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_LHS_phot = pd.read_csv('Data/1439+1839 (M7sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

#df_1444 = pd.read_csv(' ', sep=" ", comment='#', header=None,names=["w", "f", "err"])

df_1610 = pd.read_csv('Data/1610-0040 (M7sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1610_phot = pd.read_csv('Data/1610-0040 (M7sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_1626 = pd.read_csv('Data/1626+3925 (L4sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_1626_phot = pd.read_csv('Data/1626+3925 (L4sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

df_2036 = pd.read_csv('Data/2036+5059 (M7.5sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_2036_phot = pd.read_csv('Data/2036+5059 (M7.5sd) phot.txt', sep=" ", comment='#', header=None,
                           names=["w", "f", "err"])

# -------------------------------------------------------------------------------------
# --------- Remove connecting lines -------------
# -------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------
# --------- Normalize -------------
# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------
# --------- Plotting: Comparison of in order of decreasing Teff/ Spt Type -------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(8, 10)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

# -------- Add data -----------
ax1.loglog(df_0532['w'], df_0532['f'], c='k')                               # sdL7
ax1.scatter(df_0532_phot['w'], df_0532_phot['f'], c='k', s=70)
ax1.loglog(df_0616['w'], df_0616['f'], c='k')                               # sdL5
ax1.scatter(df_0616_phot['w'], df_0616_phot['f'], c='k', s=70)
ax1.loglog(df_1626['w'], df_1626['f'], c='k')                               # sdL4
ax1.scatter(df_1626_phot['w'], df_1626_phot['f'], c='k', s=70)
ax1.loglog(df_0616['w'], df_0616['f'], c='k')                               # sdL3.5
ax1.scatter(df_0616_phot['w'], df_0616_phot['f'], c='k', s=70)
ax1.loglog(df_0616['w'], df_0616['f'], c='k')                               # sdL5
ax1.scatter(df_0616_phot['w'], df_0616_phot['f'], c='k', s=70)
ax1.loglog(df_0616['w'], df_0616['f'], c='k')                               # sdL5
ax1.scatter(df_0616_phot['w'], df_0616_phot['f'], c='k', s=70)
ax1.loglog(df_0616['w'], df_0616['f'], c='k')                               # sdL5
ax1.scatter(df_0616_phot['w'], df_0616_phot['f'], c='k', s=70)