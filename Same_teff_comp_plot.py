import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
df_1256 = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# -------------- Comparison objects of the same Teff ----------------------------------

df_field = pd.read_csv('Data/NotUsingAsCompariosn/0036+1821 (L3.5) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
b = np.loadtxt('Talks/2126-8140_forsameSptfigure_L3gamma.txt')

# create df for young source of same spt
df_young = pd.DataFrame()
df_young['w'] = b[0]
df_young['f'] = b[1]

# Get ride of lines from tails
df_young=df_young[df_young['w']>= 0.61]

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_1256[(df_1256['w'] >= 0.64) & (df_1256['w'] <= 0.65)]
norm_df_1256 = df_1256['f']/(np.average(norm_region['f']))

norm_region3 = df_field[(df_field['w'] >= 0.64) & (df_field['w'] <= 0.65)]
norm_df_field = df_field['f']/(np.average(norm_region3['f']))

norm_region4 = df_young[(df_young['w'] >= 0.64) & (df_young['w'] <= 0.65)]
norm_df_young = df_young['f']/(np.average(norm_region4['f']))
# -------------------------------------------------------------------------------------
# ------------------- Plotting: I band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.6, 0.9])
plt.ylim([-0.01, 52])

# ------Tick size and Axes Labels --------
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_1256['w'], norm_df_1256, c='blue')
ax1.plot(df_field['w'], norm_df_field + 15, c='#7C7D70')
ax1.plot(df_young['w'], norm_df_young + 25, c='#D01810')

# --------- Labels -------------
ax1.annotate('Young', xy=(0.61, 30), color='#D01810', fontsize=25)
ax1.annotate('Field', xy=(0.61, 19), color='#7C7D70', fontsize=25)
ax1.annotate('Old', xy=(0.61, 5), color='blue', fontsize=25)

plt.savefig('Talks/Same_Spt_comp.png')
