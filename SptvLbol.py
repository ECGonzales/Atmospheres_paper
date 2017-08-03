import pandas as pd
import matplotlib.pyplot as plt

df_sub = pd.read_csv('Data/Subdwarf_Spt_v_Teff.txt', sep=" ", comment='#', header=None,
                     names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ', 'MJ_unc',
                            'MH', 'MH_unc', 'MK', 'MK_unc', 'MW1', 'MW1_unc', 'MW2', 'MW2_unc'])
df_comb = pd.read_csv('Data/Lbol+Teff-February2017.txt', sep="\t", comment='#', header=None,
                      names=["name", "Lbol", "Lbol_err", 'Teff', 'Teff_err', 'spt', 'spt_unc', 'group', 'grav'])

# ----- Remove the -100 -----------------
# df_comb.loc[df_comb['grav'] == -100]
df_comb.set_value(174, 'grav', 3)

# ---- Split combined dataframe into field (group 3) and low g groups 1,2) ----------
df_fld = df_comb[(df_comb['grav'] == 3)]
df_young = df_comb[(df_comb['grav'] >= 1) & (df_comb['grav'] <= 2)]

# -------------------------------------------------------------------------------------
# ------------------------- Make Plot: Spt v Teff ------------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([5, 30])
plt.ylim([-6, -2.3])

# ------ Axes Labels --------
plt.xticks([5, 10, 15, 20, 25, 30], ['M5', 'L0', 'L5', 'T0', 'T5', 'Y0'], fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Spectral Type', fontsize=25)
plt.ylabel('log(L$_\mathrm{bol}$/L$_\odot$)', fontsize=25)

# ------- Add Data ------
plt.scatter(df_fld['spt'], df_fld['Lbol'], color='#7C7D70')
ax1.errorbar(df_fld['spt'], df_fld['Lbol'], yerr=df_fld['Lbol_err'], c='#7C7D70', fmt='o')
plt.scatter(df_young['spt'], df_young['Lbol'], color='#D01810')
ax1.errorbar(df_young['spt'], df_young['Lbol'], yerr=df_young['Lbol_err'], c='#D01810', fmt='o')
plt.scatter(df_sub['SpT'], df_sub['lbol'], color='blue', s=100, zorder=5)
ax1.errorbar(df_sub['SpT'], df_sub['lbol'], yerr=df_sub['lbol_err'], c='blue', fmt='o', zorder=6)

plt.savefig('Plots/SptvLbol.png')
