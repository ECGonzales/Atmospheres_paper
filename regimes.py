import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# -------------------------------------------------------------------------------------

# ------------ 1256-0224 (Poster in SED)----------------
# Read in as pandas dataframe
df = pd.read_csv('Redone/best1256-0224 (L3.5sd) SED.txt', sep=" ", header=1, names=["w", "f", "err"])
df2 = pd.read_csv('Redone/best1256-0224 (L3.5sd) phot.txt', sep=" ", header=1, names=["w", "f", "err"])


# -------------------------------------------------------------------------------------
# ------------------------- Plotting --------------------------------------------------
# -------------------------------------------------------------------------------------

# -------- Generate spectral regime SED plot ---------------------------
# Make subarrays for color coding
opt = df[(df['w'] <= 0.950454)]
overlap = df[(df['w'] >= 0.950328) & (df['w'] <= 1.03426)]
# nir = df[(df['w'] > 1.03426)]  # Split bands and cut out some junk
h = df[(df['w'] >= 1.48933) & (df['w'] <= 1.8)]
k = df[(df['w'] >= 2.0175)]
zj = df[(df['w'] >= 0.950328) & (df['w'] <= 1.3500)]

fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)  # This makes sure that the labels aren't cut off

# ----- Plot Spectra -----------
ax1.loglog(opt['w'], opt['f'], c='#0179FF')
ax1.loglog(overlap['w'], overlap['f'], c='#009B45', lw=5, alpha=0.5)
ax1.loglog(overlap['w'], overlap['f'], c='#0179FF', alpha=0.8)  # alpha=0.3 for transparency
ax1.loglog(zj['w'], zj['f'], c='#009B45')
ax1.loglog(h['w'], h['f'], c='#009B45')
ax1.loglog(k['w'], k['f'], c='#009B45')

# ----- Plot Photometric points -----
ax1.scatter(df2['w'][0], df2['f'][0],  c='#f768a1', s=100)
ax1.scatter(df2['w'][1], df2['f'][1],  c='#c51b8a', s=100)
ax1.scatter(df2['w'][2], df2['f'][2],  c='#c51b8a', s=100)
ax1.scatter(df2['w'][3], df2['f'][3],  c='#7a0177', s=100)
ax1.scatter(df2['w'][4], df2['f'][4],  c='#7a0177', s=100)

# ----- Set X axis limit, reformat ticks -----------
plt.xlim([0.59, 4.8])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.6, 2, 3, 4]))
ax1.tick_params(axis='x', which='major', labelsize=20)
ax1.tick_params(axis='x', which='minor', labelsize=20)
plt.yticks(fontsize=20)

# ------ Axes Labels --------
plt.xlabel('Wavelength ($\mu m$)', fontsize=25)
plt.ylabel('Flux  ($F_\lambda$)', fontsize=25)

# ------ Labeling Spectra and Photometric points --------
ax1.text(0.3, 0.7, 'FIRE', transform=ax1.transAxes, color='#009B45', fontsize=15)
ax1.text(0.01, 0.8, 'LDSS3', transform=ax1.transAxes, color='#0179FF', fontsize=15)
ax1.text(0.77, 0.65, 'WISE W1', transform=ax1.transAxes, color='#7a0177', fontsize=15)
ax1.text(0.85, 0.45, 'WISE W2', transform=ax1.transAxes, color='#7a0177', fontsize=15)
ax1.text(0.5, 0.8, 'MKO H', transform=ax1.transAxes, color='#c51b8a', fontsize=15)
ax1.text(0.52, 0.59, 'MKO K', transform=ax1.transAxes, color='#c51b8a', fontsize=15)
ax1.text(0.35, 0.9, '2MASS J', transform=ax1.transAxes, color='#f768a1', fontsize=15)

plt.savefig('Plots/regimes.png')


# Error bars are too small on this scale, keep for later?
# ax1.errorbar(df2['w'][0], df2['f'][0], yerr=df2['err'][0], c='#f768a1')
# ax1.errorbar(df2['w'][1], df2['f'][1], yerr=df2['err'][1], c='#c51b8a')
# ax1.errorbar(df2['w'][2], df2['f'][2], yerr=df2['err'][2], c='#c51b8a')
# ax1.errorbar(df2['w'][3], df2['f'][3], yerr=df2['err'][3], c='#7a0177')
# ax1.errorbar(df2['w'][3], df2['f'][3], yerr=df2['err'][3], c='#7a0177')
# ax1.errorbar(df2['w'][4], df2['f'][4], yerr=df2['err'][4], c='#7a0177')
