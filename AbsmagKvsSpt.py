import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_sub = pd.read_csv('Data/Subdwarf_Spt_v_Teff.txt', sep=" ", comment='#', header=None,
                     names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ', 'MJ_unc',
                            'MH', 'MH_unc', 'MK', 'MK_unc', 'MW1', 'MW1_unc', 'MW2', 'MW2_unc'])
df_field = pd.read_csv('Data/Parallaxes-Normal_modified.txt', sep="\t", comment='#', header=1,
                       names=['name', 'spt', 'Pi', 'Pi_er', 'Jmagn_MKO', 'Jerr_MKO', 'Hmagn_MKO', 'Herr_MKO',
                              'Kmagn_MKO', 'Kerr_MKO', 'W1magn', 'W1err', 'W2magn', 'W2err', 'W3magn', 'W3err',
                              'W4magn', 'W4err', 'Jmagn', 'Jerr', 'Hmagn', 'Herr', 'Kmagn', 'Kerr', 'Lmag', 'Lerr'])

# ------------ remove -100s from Dataframe ---------
df_field = df_field[df_field['Kmagn'] > -100]

# -------------------------------------------------------------------------------------
# ------------------- Get abs Mag from relative mag -----------------------------------
# -------------------------------------------------------------------------------------
# --- Get Distance---
d = np.round(1000/(df_field['Pi']), 2)  # 1000/mas or 1/arcsec round to 2 decimal points
d_err = np.round((df_field['Pi_er']/(df_field['Pi']**2))*1000, 2)  # convert to arcsec from mas

# ------ Convert apparent mag to Abs Mag -------
AbsK = np.round(df_field['Kmagn']-(5*np.log10(d)-5), 3)
AbsK_err = np.round(np.sqrt(df_field['Kerr'] ** 2 + 25 * (d_err/(d * np.log(10))) ** 2), 3)
df_field['AbsK'] = AbsK
df_field['AbsK_err'] = AbsK_err

# -------------------------------------------------------------------------------------
# ------------------------- Make Plot: Spt v Abs Mags K---------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([5, 30])
plt.ylim([20, 6])

# ------ Axes Labels --------
plt.xticks([5, 10, 15, 20, 25, 30], ['M5', 'L0', 'L5', 'T0', 'T5', 'Y0'], fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Spectral Type', fontsize=25)
plt.ylabel('M$_\mathrm{K}$ (2MASS)', fontsize=25)

# ----- Add data -----
plt.scatter(df_field['spt'], df_field['AbsK'], color='#7C7D70')
ax1.errorbar(df_field['spt'], df_field['AbsK'], yerr=df_field['AbsK_err'], c='#7C7D70', fmt='o')
# plt.scatter(df_young['spt'], df_young['mass'], color='#D01810')
# ax1.errorbar(df_young['spt'], df_young['mass'], yerr=df_young['mass_unc'], c='#D01810', fmt='o')
plt.scatter(df_sub['SpT'], df_sub['MK'], color='blue',s=100, zorder=5)
ax1.errorbar(df_sub['SpT'], df_sub['MK'], yerr=df_sub['MK_unc'], c='blue', fmt='o', zorder=6)

# ---- Fit polynomial for subdwarfs -------
# Need to drop nans
df_sub2 =df_sub.drop(df_sub.index[2])
coeffs = np.polyfit(df_sub2['SpT'], df_sub2['MK'], 5)
line = np.poly1d(coeffs)
xp = np.linspace(5, 30, 100)
plt.plot( xp, line(xp), '-', color='#ff7f0e')
# still need to figure out how to get the uncertainies for the fit

plt.savefig('Plots/MKvspt.png')
