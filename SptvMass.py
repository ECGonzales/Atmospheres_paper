import pandas as pd
import matplotlib.pyplot as plt

df_sub = pd.read_csv('Data/Subdwarf_Spt_v_Teff.txt', sep=" ", comment='#', header=None,
                     names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ', 'MJ_unc',
                            'MH', 'MH_unc', 'MK', 'MK_unc', 'MW1', 'MW1_unc', 'MW2', 'MW2_unc'])
df_young = pd.read_csv('Data/young_masses.txt', sep="\s+", comment='#', header=None,
                       names=['name', 'spt', 'mass', 'mass_unc', 'Teff', 'Teff_unc'])
df_field = pd.read_csv('Data/field_masses.txt', sep="\t", comment='#', header=None,
                       names=['name', 'spt', 'mass', 'mass_unc', 'Teff', 'Teff_unc'])
# -------------------------------------------------------------------------------------
# ------------------------- Make Plot: Spt v mass ------------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([5, 30])
#plt.ylim([500, 3200])

# ------ Axes Labels --------
plt.xticks([5, 10, 15, 20, 25, 30], ['M5', 'L0', 'L5', 'T0', 'T5', 'Y0'], fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Spectral Type', fontsize=25)
plt.ylabel('Mass (M$_\mathrm{J}$)', fontsize=25)

# ----- Add data -----
plt.scatter(df_field['spt'], df_field['mass'], color='#7C7D70')
ax1.errorbar(df_field['spt'], df_field['mass'], yerr=df_field['mass_unc'], c='#7C7D70', fmt='o')
plt.scatter(df_young['spt'], df_young['mass'], color='#D01810')
ax1.errorbar(df_young['spt'], df_young['mass'], yerr=df_young['mass_unc'], c='#D01810', fmt='o')
plt.scatter(df_sub['SpT'], df_sub['mass'], color='blue', s=65, zorder=5)
ax1.errorbar(df_sub['SpT'], df_sub['mass'], yerr=df_sub['mass_unc'], c='blue', fmt='o', zorder=6)

# Make 1256-0224 stand out
plt.scatter(df_sub['SpT'][0], df_sub['mass'][0], color='blue', s=300, zorder=7, marker="*")
ax1.annotate('1256-0224', xy=(12, 95), color='k', fontsize=12)

plt.savefig('Plots/SptVmass.png')

# -------------------------------------------------------------------------------------
# ------------------------- Make Plot: Teff v mass ------------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
#plt.xlim([5, 30])
#plt.ylim([500, 3200])

# ------ Axes Labels --------
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Mass (M$_\mathrm{J}$)', fontsize=25)
plt.ylabel('T$_\mathrm{eff}$ (K)', fontsize=25)

# ----- Add data -----
plt.scatter(df_field['mass'], df_field['Teff'], color='#7C7D70')
ax1.errorbar(df_field['mass'], df_field['Teff'], yerr=df_field['Teff_unc'], c='#7C7D70', fmt='o')
plt.scatter(df_young['mass'], df_young['Teff'], color='#D01810')
ax1.errorbar(df_young['mass'], df_young['Teff'], yerr=df_young['Teff_unc'], c='#D01810', fmt='o')
plt.scatter(df_sub['mass'], df_sub['Teff'], color='blue', s=65, zorder=5)
ax1.errorbar(df_sub['mass'], df_sub['Teff'], yerr=df_sub['Teff_err'], c='blue', fmt='o', zorder=6)
plt.scatter(df_sub['mass'][0], df_sub['Teff'][0], color='blue', s=300, zorder=7, marker="*")

plt.savefig('Plots/TeffVmass.png')
