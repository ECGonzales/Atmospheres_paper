import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import matplotlib.patches as mpatches

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes

df_HD = pd.read_csv('Data/HD114762B (M9sd) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])
df_HD_phot = pd.read_csv('Data/HD114762B (M9sd) phot.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])


# -------------------------------------------------------------------------------------
# ------------------------------ Normalize to 1256 -----------------------------------
# -------------------------------------------------------------------------------------
norm_region_HD = df_HD[(df_HD['w'] >= 0.98) & (df_HD['w'] <= 0.988)]
df_HD_phot['f'] = df_HD_phot['f']/(np.average(norm_region_HD['f']))
norm_df_HD = df_HD['f']/(np.average(norm_region_HD['f']))

# Split into regions to plot
df_HD_SED = df_HD[(df_HD['w'] > 0.91) & (df_HD['w'] <= 3)]
df_HD_long = df_HD[(df_HD['w'] >= 2.482180)]
df_HD_short = df_HD[(df_HD['w'] <= 0.92)]

# ------- Plotting -----------
# Figure Layout
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(11.71, 7.43)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

# Add Data
ax1.loglog(df_HD_SED['w'], df_HD_SED['f'], c='#09D67E')
ax1.scatter(df_HD_phot['w'], df_HD_phot['f'], c='k', s=70)
ax1.scatter(df_HD_phot['w'], df_HD_phot['f'], c='#09D67E', s=50)
ax1.loglog(df_HD_short['w'], df_HD_short['f'], c='#09D67E', ls='dashed')
ax1.loglog(df_HD_long['w'], df_HD_long['f'], c='#09D67E', ls='dashed')

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.33, 15])
plt.ylim([0.01, 2.5])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.yaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.35, 0.6, 2, 3]))
ax1.tick_params(axis='x', which='major', labelsize=20)
ax1.tick_params(axis='x', which='minor', labelsize=20)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Normalized Flux  ($F_\lambda$)', fontsize=25)

plt.savefig('Plots/normHD_with_tails.png')