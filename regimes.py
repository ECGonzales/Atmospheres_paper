import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# -------------------------------------------------------------------------------------

# ------------ 1256-0224 (Poster in SED)----------------
# Read in as pandas dataframe
df = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) SED_nan.txt', sep=" ", comment='#', header=None,
                 names=["w", "f", "err"])
df2 = pd.read_csv('Data/correctpi1256-0224 (L3.5sd) phot.txt', sep=" ", header=1, names=["w", "f", "err"])
# header=1 skips the 2MASS H which is ok here but not other times, use stuff above


# -------------------------------------------------------------------------------------
# ------------------------- Plotting --------------------------------------------------
# -------------------------------------------------------------------------------------

# -------- Generate spectral regime SED plot ---------------------------
# Make subarrays for color coding
opt = df[(df['w'] <= 0.950454)]
overlap = df[(df['w'] >= 0.950328) & (df['w'] <= 1.03426)]
# nir = df[(df['w'] > 1.03426)]  # Split bands and cut out some junk
z = df[(df['w'] >= 0.950328) & (df['w'] <= 1.11474)]
j = df[(df['w'] >= 1.15308) & (df['w'] <= 1.3500)]
h = df[(df['w'] >= 1.48933) & (df['w'] <= 1.8)]
k = df[(df['w'] >= 2.0175)]
# zj = df[(df['w'] >= 0.950328) & (df['w'] <= 1.3500)]

fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 6.45)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # This makes sure that the labels aren't cut off


# ----- Plot Spectra -----------
ax1.loglog(opt['w'], opt['f'], c='#0179FF')
ax1.loglog(overlap['w'], overlap['f'], c='#009B45', lw=5, alpha=0.5)
ax1.loglog(overlap['w'], overlap['f'], c='#0179FF', alpha=0.8)  # alpha=0.3 for transparency
# ax1.loglog(zj['w'], zj['f'], c='#009B45')  #remove the combined line from the begining of the J band
ax1.loglog(z['w'], z['f'], c='#009B45')
ax1.loglog(j['w'], j['f'], c='#009B45')
ax1.loglog(h['w'], h['f'], c='#009B45')
ax1.loglog(k['w'], k['f'], c='#009B45')

# ----- Plot Photometric points -----
ax1.scatter(df2['w'][0], df2['f'][0],  c='#dd3497', s=150, zorder=6)  # 2Mass J
ax1.scatter(df2['w'][1], df2['f'][1],  c='#ae017e', s=150, zorder=6)  # MKO_H
ax1.scatter(df2['w'][2], df2['f'][2],  c='#ae017e', s=150, zorder=6)  # MKO_K
ax1.scatter(df2['w'][3], df2['f'][3],  c='#f768a1', s=150, zorder=6)  # SDSS_i
ax1.scatter(df2['w'][4], df2['f'][4],  c='#f768a1', s=150, zorder=6)  # SDSS_z
ax1.scatter(df2['w'][5], df2['f'][5],  c='#7a0177', s=150, zorder=6)  # WISE_W1
ax1.scatter(df2['w'][6], df2['f'][6],  c='#7a0177', s=150, zorder=6)  # WISE_W2

# ----- Set axes limits, reformat ticks -----------
plt.xlim([0.59, 4.8])
plt.ylim([5*10**(-19), 3*10**(-14)])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.6, 2, 3, 4]))
ax1.tick_params(axis='x', which='major', labelsize=20)
ax1.tick_params(axis='x', which='minor', labelsize=20)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu$m)', fontsize=25)
plt.ylabel('Flux ($\mathrm{erg\ s^{-1} cm^{-2} A^{-1}}$)', fontsize=25)

# ------ Labeling Spectra and Photometric points --------
ax1.text(0.3, 0.7, 'FIRE', transform=ax1.transAxes, color='#009B45', fontsize=15)
ax1.text(0.15, 0.6, 'LDSS3', transform=ax1.transAxes, color='#0179FF', fontsize=15)
ax1.text(0.77, 0.67, 'WISE $W1$', transform=ax1.transAxes, color='#7a0177', fontsize=15)
ax1.text(0.86, 0.46, 'WISE $W2$', transform=ax1.transAxes, color='#7a0177', fontsize=15)
ax1.text(0.52, 0.81, 'MKO $H$', transform=ax1.transAxes, color='#ae017e', fontsize=15)
ax1.text(0.52, 0.6, 'MKO $K$', transform=ax1.transAxes, color='#ae017e', fontsize=15)
ax1.text(0.35, 0.93, '2MASS $J$', transform=ax1.transAxes, color='#dd3497', fontsize=15)
ax1.text(0.03, 0.83, 'SDSS $i$', transform=ax1.transAxes, color='#f768a1', fontsize=15)
ax1.text(0.12, 0.94, 'SDSS $z$', transform=ax1.transAxes, color='#f768a1', fontsize=15)

# ---------- Add Bandpasses for the photometry -------------
sdss_i = pd.DataFrame()
sdss_i['x'] = [0.6430, 0.8630]
sdss_i['y'] = [7.2961*10**(-19), 7.2961*10**(-19)]
plt.plot(sdss_i['x'], sdss_i['y'], color='#f768a1', linestyle='solid')

sdss_z = pd.DataFrame()
sdss_z['x'] = [0.7730, 1.1230]
sdss_z['y'] = [1.5*10**(-18), 1.5*10**(-18)]
plt.plot(sdss_z['x'], sdss_z['y'], color='#f768a1', linestyle='solid')

twomass_j = pd.DataFrame()
twomass_j['x'] = [1.105, 1.349]
twomass_j['y'] = [7.2961*10**(-19), 7.2961*10**(-19)]
plt.plot(twomass_j['x'], twomass_j['y'], color='#dd3497', linestyle='solid')

MKO_H = pd.DataFrame()
MKO_H['x'] = [1.490, 1.780]
MKO_H['y'] = [1.5*10**(-18), 1.5*10**(-18)]
plt.plot(MKO_H['x'], MKO_H['y'], color='#ae017e', linestyle='solid')

MKO_K = pd.DataFrame()
MKO_K['x'] = [1.990, 2.310]
MKO_K['y'] = [7.2961*10**(-19), 7.2961*10**(-19)]
plt.plot(MKO_K['x'], MKO_K['y'], color='#ae017e', linestyle='solid')

W1 = pd.DataFrame()
W1['x'] = [2.75, 3.9]
W1['y'] = [1.5*10**(-18), 1.5*10**(-18)]
plt.plot(W1['x'], W1['y'], color='#7a0177', linestyle='solid')

W2 = pd.DataFrame()
W2['x'] = [4, 5.4]
W2['y'] = [7.2961*10**(-19), 7.2961*10**(-19)]
plt.plot(W2['x'], W2['y'], color='#7a0177', linestyle='solid')

plt.tight_layout()  # use to minimize whitespace on edges. May be best for figures in the paper
plt.savefig('Plots/regimes.png')

# -------- Add the bandpasses at the bottom of the plot ---------

# Error bars are too small on this scale, keep for later?
# ax1.errorbar(df2['w'][0], df2['f'][0], yerr=df2['err'][0], c='#f768a1')
# ax1.errorbar(df2['w'][1], df2['f'][1], yerr=df2['err'][1], c='#c51b8a')
# ax1.errorbar(df2['w'][2], df2['f'][2], yerr=df2['err'][2], c='#c51b8a')
# ax1.errorbar(df2['w'][3], df2['f'][3], yerr=df2['err'][3], c='#7a0177')
# ax1.errorbar(df2['w'][3], df2['f'][3], yerr=df2['err'][3], c='#7a0177')
# ax1.errorbar(df2['w'][4], df2['f'][4], yerr=df2['err'][4], c='#7a0177')
