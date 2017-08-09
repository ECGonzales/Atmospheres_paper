import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_sub = pd.read_csv('Data/Subdwarf_Spt_v_Teff.txt', sep=" ", comment='#', header=None,
                     names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ', 'MJ_unc',
                            'MH', 'MH_unc', 'MK', 'MK_unc', 'MW1', 'MW1_unc', 'MW2', 'MW2_unc'])
df_comb = pd.read_csv('Data/Lbol+Teff-February2017_updated.txt', sep="\s+", comment='#', header=None,
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
plt.xlim([5.5, 18.5])
plt.ylim([-6, -2.3])

# ------ Axes Labels --------
plt.xticks([6, 8, 10, 12, 14, 16, 18], ['M6','M8', 'L0', 'L2', 'L4', 'L6', 'L8'], fontsize=20)
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

# --- Designate 1256-0224 -----
plt.scatter(df_sub['SpT'][0], df_sub['lbol'][0], color='blue', s=500, zorder=7, marker="*")
ax1.annotate('1256-0224', xy=(12.7, -3.25), color='k', fontsize=12)

# -------------------------------------------------------------------------------------
# ------------------------- Polynomial fits  -----------------------------------------
# -------------------------------------------------------------------------------------
# ------ Fit polynomial for subdwarfs ------
# drop nan from column need to get polynomial
df_subpoly = df_sub[pd.notnull(df_sub['lbol'])]

# --- Get uncertainites for upper and lower teff limits ----
df_subpoly['Lbol_up'] = df_subpoly['lbol'] + df_subpoly['lbol_err']
df_subpoly['Lbol_d'] = df_subpoly['lbol'] - df_subpoly['lbol_err']

# ------ Fit the values --------
coeffs = np.polyfit(df_subpoly['SpT'], df_subpoly['lbol'], 1)
line = np.poly1d(coeffs)

coeffs_up = np.polyfit(df_subpoly['SpT'], df_subpoly['Lbol_up'], 1)
line_up = np.poly1d(coeffs_up)

coeffs_d = np.polyfit(df_subpoly['SpT'], df_subpoly['Lbol_d'], 1)
line_d = np.poly1d(coeffs_d)

# ---- Plot the fit lines -----
xp = np.linspace(5, 30, 100)
plt.plot(xp, line(xp), '-', color='k')
plt.plot(xp, line_up(xp), '-', color='#17becf', alpha=.25)
plt.plot(xp, line_d(xp), '-', color='#17becf', alpha=.25)
ax1.fill_between(xp, line_up(xp), line_d(xp), alpha=.25, color='#17becf')

plt.savefig('Plots/SptvLbol.png')
