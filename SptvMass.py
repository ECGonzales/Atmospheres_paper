import pandas as pd
import matplotlib.pyplot as plt

df_sub = pd.read_csv('Data/Subdwarf_Spt_v_Teff.txt', sep=" ", comment='#', header=None,
                     names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ', 'MJ_unc',
                            'MH', 'MH_unc', 'MK', 'MK_unc', 'MW1', 'MW1_unc', 'MW2', 'MW2_unc'])

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
plt.scatter(df_sub['SpT'], df_sub['mass'], color='blue', s=100)
ax1.errorbar(df_sub['SpT'], df_sub['mass'], yerr=df_sub['mass_unc'], c='blue', fmt='o')

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
plt.scatter(df_sub['Teff'], df_sub['mass'], color='blue', s=100)
ax1.errorbar(df_sub['Teff'], df_sub['mass'], yerr=df_sub['mass_unc'], c='blue', fmt='o')

plt.savefig('Plots/TeffVmass.png')
