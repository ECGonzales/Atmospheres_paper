import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read all in as pandas dataframes. Jonathan's post smooth is sep= ","
df_1256 = pd.read_csv('Data/Smoothed_data/Red_optical_comp_smoothed/correctpi1256-0224 (L3.5sd) SED_smoothed.txt',
                      sep=",", comment='#', header=None, names=["w", "f", "err"])
# -------------- Comparison objects of the same Teff ----------------------------------
df_young = pd.read_csv('Data/Smoothed_data/Red_optical_comp_smoothed/teff2000-7523 (M9gamma) SED_updated_smoothed.txt',
                       sep=",", comment='#', header=None, names=["w", "f", "err"])
df_field = pd.read_csv('Data/Smoothed_data/Red_optical_comp_smoothed/teff0024-0158 (M9.5) SED_smoothed.txt', sep=",",
                       comment='#', header=None, names=["w", "f", "err"])

# ----------------------- Same SpT ----------------------------------------------------
df_fieldspt = pd.read_csv('Data/Smoothed_data/Red_optical_comp_smoothed/0036+1821 (L3.5) SED_smoothed.txt', sep=",",
                          comment='#', header=None, names=["w", "f", "err"])

# ------------------------------------------------------------------------------------
# ------------------- Fix files to read all columns as Floats-------------------------
# ------------------------------------------------------------------------------------
df_1256 = df_1256.astype(float)
df_young = df_young.astype(float)
df_field = df_field.astype(float)
df_fieldspt = df_fieldspt.astype(float)

# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_1256[(df_1256['w'] >= 0.64) & (df_1256['w'] <= 0.65)]
norm_df_1256 = df_1256['f']/(np.average(norm_region['f']))

norm_region2 = df_young[(df_young['w'] >= 0.64) & (df_young['w'] <= 0.65)]
norm_df_young = df_young['f']/(np.average(norm_region2['f']))

norm_region3 = df_field[(df_field['w'] >= 0.64) & (df_field['w'] <= 0.65)]
norm_df_field = df_field['f']/(np.average(norm_region3['f']))

norm_region4 = df_fieldspt[(df_fieldspt['w'] >= 0.64) & (df_fieldspt['w'] <= 0.65)]
norm_df_fieldspt = df_fieldspt['f']/(np.average(norm_region4['f']))

# -------------------------------------------------------------------------------------
# ------------------- Plotting: Red Optical comparison -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
ax1.tick_params(axis='both', labelsize=20, length=8, width=1.1)  # Lengthen ticks
for axis in ['top', 'bottom', 'left', 'right']:  # Thicken the frame
    ax1.spines[axis].set_linewidth(1.1)
plt.xlim([0.60, 0.90])
plt.ylim([-0.01, 58])

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_fieldspt['w'], norm_df_fieldspt, c='#7C7D70')
ax1.plot(df_1256['w'], norm_df_1256 + 15, c='blue')
ax1.plot(df_field['w'], norm_df_field + 30, c='#7C7D70')
ax1.plot(df_young['w'], norm_df_young + 45, c='#D01810')

# -------- Dividing Line ----------
divide = pd.DataFrame()
divide['x'] = [0.75, 0.75]
divide['y'] = [0, 58]
plt.plot(divide['x'], divide['y'], color='k', linestyle='dashed')


# -------- Label the Objects ---------
ax1.text(0.01, 0.1, 'J0036+1821  (L3.5)', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.05, '$T_\mathrm{eff}: 1868 \pm 68$ K ', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.4, 'J1256-0024  (sdL3.5)', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.35, '$T_\mathrm{eff}: 2307 \pm 71$ K', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.63, 'J0024-0158  (M9)', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.58, '$T_\mathrm{eff}: 2385 \pm 77$ K', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.87, 'J2000-7523  (M9$\gamma$)', transform=ax1.transAxes, color='k', fontsize=15)
ax1.text(0.01, 0.82, '$T_\mathrm{eff}: 2388 \pm 36$ K', transform=ax1.transAxes, color='k', fontsize=15)

plt.tight_layout()
plt.savefig('Plots/RedOpticalComparison.png', dpi=150)
