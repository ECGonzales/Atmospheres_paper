import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_sub = pd.read_csv('Data/Subdwarf_Spt_v_Teff.txt', sep=" ", comment='#', header=None,
                     names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ', 'MJ_unc',
                            'MH', 'MH_unc', 'MK', 'MK_unc', 'MW1', 'MW1_unc', 'MW2', 'MW2_unc'])

df_field = pd.read_csv('Data/Parallaxes-Normal_modified.txt', sep="\t", comment='#', header=0,
                       names=['name', 'spt', 'Pi', 'Pi_er', 'Jmagn_MKO', 'Jerr_MKO', 'Hmagn_MKO', 'Herr_MKO',
                              'Kmagn_MKO', 'Kerr_MKO', 'W1magn', 'W1err', 'W2magn', 'W2err', 'W3magn', 'W3err',
                              'W4magn', 'W4err', 'Jmagn', 'Jerr', 'Hmagn', 'Herr', 'Kmagn', 'Kerr', 'Lmag', 'Lerr'])

df_young = pd.read_csv('Data/For-CMD-NEW-NEW.txt', sep='\t', comment="#", header=0,
                       names=['Grp', 'ID', 'SpT', 'lowg', 'Jmag', 'Jerr', 'H', 'Herr', 'K', 'Kerr', 'W1', 'W1er', 'W2',
                              'W2er', 'W3', 'W3er', 'W4', 'W4er', 'PI', 'Pier', 'MKOJ', 'MKOJer', 'MKOH', 'MKOHer',
                              'MKOK', 'MKOKer', 'Lband', 'Lbander'])

# ------------ remove -100s from Dataframe ---------
df_field = df_field[df_field['W2magn'] > -100]
df_young = df_young[df_young['W2er'] > -100]

# -------------------------------------------------------------------------------------
# ------------------- Get abs Mag from relative mag -----------------------------------
# -------------------------------------------------------------------------------------
# --- Get Distance: Field ---
d = np.round(1000/(df_field['Pi']), 2)  # 1000/mas or 1/arcsec round to 2 decimal points
d_err = np.round((df_field['Pi_er']/(df_field['Pi']**2))*1000, 2)  # convert to arcsec from mas

# ------ Convert apparent mag to Abs Mag: Field -------
AbsW2 = np.round(df_field['W2magn']-(5*np.log10(d)-5), 3)
AbsW2_err = np.round(np.sqrt(df_field['W2err'] ** 2 + 25 * (d_err/(d * np.log(10))) ** 2), 3)
df_field['AbsW2'] = AbsW2
df_field['AbsW2_err'] = AbsW2_err

# --- Get Distance: Young ---
dy = np.round(1000/(df_young['PI']), 2)  # 1000/mas or 1/arcsec round to 2 decimal points
dy_err = np.round((df_young['Pier']/(df_young['PI']**2))*1000, 2)  # convert to arcsec from mas

# ------ Convert apparent mag to Abs Mag: Young -------
AbsW2y = np.round(df_young['W2']-(5*np.log10(dy)-5), 3)
AbsW2y_err = np.round(np.sqrt(df_young['W2er'] ** 2 + 25 * (dy_err/(dy * np.log(10))) ** 2), 3)
df_young['AbsW2'] = AbsW2y
df_young['AbsW2_err'] = AbsW2y_err


# -------------------------------------------------------------------------------------
# ------------------------- Make Plot: Spt v Abs Mags W2---------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)  # to make sure proper size run entire code at once and change 8 to 6.45 to
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)
plt.xlim([5, 18.5])
plt.ylim([13.75, 7])

# ------ Axes Labels --------
plt.xticks([6, 8, 10, 12, 14, 16, 18], ['M6', 'M8', 'L0', 'L2', 'L4', 'L6', 'L8'], fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Spectral Type', fontsize=25)
plt.ylabel('M$_\mathrm{W2}$', fontsize=25)

# ----- Add data -----
fld = plt.scatter(df_field['spt'], df_field['AbsW2'], color='#7C7D70')
ax1.errorbar(df_field['spt'], df_field['AbsW2'], yerr=df_field['AbsW2_err'], c='#7C7D70', fmt='o')
young = plt.scatter(df_young['SpT'], df_young['AbsW2'], color='#D01810')
ax1.errorbar(df_young['SpT'], df_young['AbsW2'], yerr=df_young['AbsW2_err'], c='#D01810', fmt='o')
sub = plt.scatter(df_sub['SpT'], df_sub['MW2'], color='blue', s=100, zorder=5)
ax1.errorbar(df_sub['SpT'], df_sub['MW2'], yerr=df_sub['MW2_unc'], c='blue', fmt='o', zorder=6)

# --- Designate 1256-0224 -----
plt.scatter(df_sub['SpT'][0], df_sub['MW2'][0], color='blue', s=500, zorder=7, marker="*")
ax1.annotate('1256-0224', xy=(12.7, 13), color='k', fontsize=12)
pointer = pd.DataFrame()
pointer['x'] = [13.5, 13.5]
pointer['y'] = [12.5, 11]
ax1.plot(pointer['x'], pointer['y'], color='k')

# ---- Add Legend ----
plt.legend([fld, young, sub], ["Field", "Young", 'Subdwarf'], frameon=False, fontsize=12)

# -------------------------------------------------------------------------------------
# ------------------------- Polynomial fits  -----------------------------------------
# -------------------------------------------------------------------------------------
# ------ Fit polynomial for subdwarfs ------
# Need to drop nans
df_sub2 = df_sub.drop(df_sub.index[[1, 5, 11]])

# --- Get uncertainites for upper and lower teff limits ----
df_sub2['AbsW2_up'] = df_sub2['MW2'] + df_sub2['MW2_unc']
df_sub2['AbsW2_d'] = df_sub2['MW2'] - df_sub2['MW2_unc']

# ------ Fit the values --------
coeffs = np.polyfit(df_sub2['SpT'], df_sub2['MW2'], 1)
line = np.poly1d(coeffs)

coeffs_up = np.polyfit(df_sub2['SpT'], df_sub2['AbsW2_up'], 1)
line_up = np.poly1d(coeffs_up)

coeffs_d = np.polyfit(df_sub2['SpT'], df_sub2['AbsW2_d'], 1)
line_d = np.poly1d(coeffs_d)

# ---- print values to screen -------
print coeffs
print coeffs_up
print coeffs_d

# ---- Plot the fit lines -----
xp = np.linspace(5, 30, 100)
plt.plot(xp, line(xp), '-', color='k')
plt.plot(xp, line_up(xp), '-', color='#17becf', alpha=.25)
plt.plot(xp, line_d(xp), '-', color='#17becf', alpha=.25)
ax1.fill_between(xp, line_up(xp), line_d(xp), alpha=.25, color='#17becf')

plt.savefig('Plots/W2vspt.png')
