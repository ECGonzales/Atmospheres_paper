import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_1256 = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# -------------- Comparison objects of the same Teff ----------------------------------
df_young = pd.read_csv('Data/teff2000-7523 (M9gamma) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_field = pd.read_csv('Data/teff0024-0158 (M9.5) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])

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
# ------------------- Plotting: I band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.74, 0.90])
plt.ylim([-0.01, 1.75])

# ------Tick size and Axes Labels --------
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Normalized Flux (F$_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_1256['w'], norm_df_1256, c='blue')
ax1.plot(df_field['w'], norm_df_field + 0.7, c='#7C7D70')
ax1.plot(df_young['w'], norm_df_young + 1, c='#D01810')

plt.savefig('Plots/IbandTeff.png')

# **************************************************************************************************************

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas dataframes
df_1256 = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])

# -------------- Comparison objects of the same Lbol ----------------------------------
df_young = pd.read_csv('Data/lbol0223-5815 (L0gamma) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
df_field = pd.read_csv('Data/lbol1048-3956 (M9) SED.txt', sep=" ", comment='#', header=None, names=["w", "f", "err"])


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
# ------------------- Plotting: I band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.74, 0.9])
plt.ylim([-0.01, 1.7])

# ------Tick size and Axes Labels --------
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Normalized Flux (F$_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_1256['w'], norm_df_1256, c='blue')
ax1.plot(df_field['w'], norm_df_field + 0.6, c='#7C7D70')
ax1.plot(df_young['w'], norm_df_young + 1, c='#D01810')

plt.savefig('Plots/IbandLbol.png')

# ****************************************************************************************************************

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read all in as pandas dataframes
df_1256 = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) SED.txt', sep=" ", comment='#', header=None,
                      names=["w", "f", "err"])
# -------------- Comparison objects of the same Teff ----------------------------------

df_field = pd.read_csv('Data/NotUsingAsCompariosn/0036+1821 (L3.5) SED.txt', sep=" ", comment='#', header=None,
                       names=["w", "f", "err"])
# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_1256[(df_1256['w'] >= 0.98) & (df_1256['w'] <= 0.988)]
norm_df_1256 = df_1256['f']/(np.average(norm_region['f']))

norm_region3 = df_field[(df_field['w'] >= 0.98) & (df_field['w'] <= 0.988)]
norm_df_field = df_field['f']/(np.average(norm_region3['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: I band comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([0.74, 0.9])
plt.ylim([-0.01, 1.2])

# ------Tick size and Axes Labels --------
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Normalized Flux (F$_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_1256['w'], norm_df_1256, c='blue')
ax1.plot(df_field['w'], norm_df_field - 1, c='#7C7D70')

plt.savefig('Plots/Ibandsamespectraltype.png')