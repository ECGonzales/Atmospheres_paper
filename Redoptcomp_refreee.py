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


# ------------------------------------------------------------------------------------
# ------------------- Fix files to read all columns as Floats-------------------------
# ------------------------------------------------------------------------------------
df_1256 = df_1256.astype(float)
df_young = df_young.astype(float)
df_field = df_field.astype(float)


# -------------------------------------------------------------------------------------
# ------------------------- Normalize the spectra -------------------------------------
# -------------------------------------------------------------------------------------
# Determine region good for all spectra to take the average flux over
norm_region = df_1256[(df_1256['w'] >= 0.825) & (df_1256['w'] <= 0.840)]
norm_df_1256 = df_1256['f']/(np.average(norm_region['f']))

norm_region2 = df_young[(df_young['w'] >= 0.825) & (df_young['w'] <= 0.840)]
norm_df_young = df_young['f']/(np.average(norm_region2['f']))

norm_region3 = df_field[(df_field['w'] >= 0.825) & (df_field['w'] <= 0.840)]
norm_df_field = df_field['f']/(np.average(norm_region3['f']))


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
plt.xlim([0.64, 0.95])
plt.ylim([-0.01, 4.3])

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Normalized Flux ($F_\lambda$)', fontsize=25)

# -------- Add data -----------
ax1.plot(df_1256['w'], norm_df_1256, c='blue')
ax1.plot(df_field['w'], norm_df_field + 1, c='#7C7D70')
ax1.plot(df_young['w'], norm_df_young + 2, c='#D01810')

# ---- Label Features ------
CaI = pd.DataFrame()
CaI['x'] = [0.65711, 0.65711]
CaI['y'] = [2.4, 2.55]
ax1.plot(CaI['x'], CaI['y'], color='k')
ax1.annotate('Ca$\,$I', xy=(0.651, 2.6), color='k', fontsize=12)

TiO2 = pd.DataFrame()
TiO2['x'] = [0.658, 0.685]
TiO2['y'] = [3, 3]
ax1.plot(TiO2['x'], TiO2['y'], color='k')
ax1.annotate('TiO', xy=(0.665, 3.05), color='k', fontsize=12)

CaH = pd.DataFrame()
CaH['x'] = [0.675, 0.705]
CaH['y'] = [2.55, 2.55]
ax1.plot(CaH['x'], CaH['y'], color='k')
CaHd = pd.DataFrame()
CaHd['x'] = [0.675, 0.675]
CaHd['y'] = [2.3, 2.55]
ax1.plot(CaHd['x'], CaHd['y'], color='k')
ax1.annotate('CaH', xy=(0.675, 2.56), color='k', fontsize=12)

TiO = pd.DataFrame()
TiO['x'] = [0.7053, 0.72]
TiO['y'] = [2.75, 2.755]
ax1.plot(TiO['x'], TiO['y'], color='k')
TiOd = pd.DataFrame()
TiOd['x'] = [0.7053, 0.705]
TiOd['y'] = [2.61, 2.75]
ax1.plot(TiOd['x'], TiOd['y'], color='k')
ax1.annotate('TiO', xy=(0.704, 2.8), color='k', fontsize=12)

KII = pd.DataFrame()
KII['x'] = [0.7665, 0.7665]
KII['y'] = [2.7, 3]
ax1.plot(KII['x'], KII['y'], color='k')
KII2 = pd.DataFrame()
KII2['x'] = [0.7699, 0.7699]
KII2['y'] = [2.7, 3]
ax1.plot(KII2['x'], KII2['y'], color='k')
ax1.annotate('K$\,$I', xy=(0.764, 3.065), color='k', fontsize=12)

Rb1 = pd.DataFrame()
Rb1['x'] = [0.78, 0.78]
Rb1['y'] = [0.4, 0.7]
ax1.plot(Rb1['x'], Rb1['y'], color='k')
ax1.annotate('Rb$\,$I', xy=(0.77, 0.75), color='k', fontsize=12)

VO = pd.DataFrame()
VO['x'] = [0.7851, 0.7973]
VO['y'] = [3.4, 3.4]
ax1.plot(VO['x'], VO['y'], color='k')
ax1.annotate('VO', xy=(0.786, 3.45), color='k', fontsize=12)

Rb = pd.DataFrame()
Rb['x'] = [0.7948, 0.7948]
Rb['y'] = [0.65, 0.8]
ax1.plot(Rb['x'], Rb['y'], color='k')
ax1.annotate('Rb$\,$I', xy=(0.785, 0.85), color='k', fontsize=12)

NaI = pd.DataFrame()
NaI['x'] = [0.8183, 0.8183]
NaI['y'] = [3.4, 3.6]
ax1.plot(NaI['x'], NaI['y'], color='k', linewidth=0.5)
NaI2 = pd.DataFrame()
NaI2['x'] = [0.8195, 0.8195]
NaI2['y'] = [3.4, 3.6]
ax1.plot(NaI2['x'], NaI2['y'], color='k', linewidth=0.5)
ax1.annotate('NaI', xy=(0.813, 3.65), color='k', fontsize=12)

TiO3 = pd.DataFrame()
TiO3['x'] = [0.8432, 0.85]
TiO3['y'] = [3.5, 3.5]
ax1.plot(TiO3['x'], TiO3['y'], color='k')
TiOd = pd.DataFrame()
TiOd['x'] = [0.8432, 0.8432]
TiOd['y'] = [3.3, 3.5]
ax1.plot(TiOd['x'], TiOd['y'], color='k')
ax1.annotate('TiO', xy=(0.8432, 3.55), color='k', fontsize=12)

TiI = pd.DataFrame()
TiI['x'] = [0.844, 0.844]
TiI['y'] = [0.45, 0.3]
ax1.plot(TiI['x'], TiI['y'], color='k')
ax1.annotate('Ti$\,$I', xy=(0.836, 0.1), color='k', fontsize=12)

CsI = pd.DataFrame()
CsI['x'] = [0.8521, 0.8521]
CsI['y'] = [0.55, 0.7]
ax1.plot(CsI['x'], CsI['y'], color='k')
ax1.annotate('Cs$\,$I', xy=(0.846, 0.42), color='k', fontsize=12)

CrH = pd.DataFrame()
CrH['x'] = [0.8611, 0.865]
CrH['y'] = [1.3, 1.3]
ax1.plot(CrH['x'], CrH['y'], color='k')
CrHd = pd.DataFrame()
CrHd['x'] = [0.8611, 0.8611]
CrHd['y'] = [1.22, 1.3]
ax1.plot(CrHd['x'], CrHd['y'], color='k')
ax1.annotate('CrH', xy=(0.86, 1.35), color='k', fontsize=12)

FeH = pd.DataFrame()
FeH['x'] = [0.8692, 0.875]
FeH['y'] = [1, 1]
ax1.plot(FeH['x'], FeH['y'], color='k')
FeH = pd.DataFrame()
FeH['x'] = [0.8692, 0.8692]
FeH['y'] = [0.95, 1]
ax1.plot(FeH['x'], FeH['y'], color='k')
ax1.annotate('FeH', xy=(0.865, 1.05), color='k', fontsize=12)

H2O = pd.DataFrame()
H2O['x'] = [0.9300, 0.95]
H2O['y'] = [4, 4]
ax1.plot(H2O['x'], H2O['y'], color='k')
ax1.annotate('H$_\mathrm{2}$O', xy=(0.93, 4.05), color='k', fontsize=12)

# -------- Label the Objects ---------
ax1.text(0.01, 0.1, 'J1256-0024', transform=ax1.transAxes, color='blue', fontsize=15)
ax1.text(0.01, 0.3, 'J0024-0158', transform=ax1.transAxes, color='#7C7D70', fontsize=15)
ax1.text(0.01, 0.42, 'J2000-7523', transform=ax1.transAxes, color='#D01810', fontsize=15)

plt.tight_layout()
plt.savefig('Plots/RedOpticalComparison_referee.png', dpi=150)
