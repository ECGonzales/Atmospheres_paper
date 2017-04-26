import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# -------------------------------------------------------------------------------------

# ------------ 1256-0224 (Poster in SED)----------------
# Read in as pandas dataframe
df = pd.read_csv('Redone/best1256-0224 (L3.5sd) SED.txt', sep=" ", header=1, names=["w", "f", "err"])
df2 = pd.read_csv('Redone/best1256-0224 (L3.5sd) phot.txt', sep=" ", header=1, names=["w", "f", "err"])

# TODO: Add in comparison objects and plot
# ------------- Comparison Objects -------------------
# No problem spectra for 1626+3925
w_1626, f_1626, unc_1626 = np.loadtxt('Redone/MIR(2)1626+3925 (L4sd) SED.txt', delimiter=' ', unpack=True)
phot1626_w, phot1626_f, phot1626_err = np.loadtxt('Redone/MIR(2)1626+3925 (L4sd) phot.txt', delimiter=' ',
                                                  usecols=(1, 2, 3), unpack=True)
# ---------------------- Same Teff ----------------------------------

w_0036, f_0036, u_0036 = np.loadtxt('Redone/0036+1821 (L3.5) SED.txt', delimiter=' ', unpack=True)
wp_0036, fp_0036, up_0036 = np.loadtxt('Redone/0036+1821 (L3.5) phot.txt', delimiter=' ',
                                       usecols=(1, 2, 3), unpack=True)
# 1207

# ---------------- Same Lbol -------------------------------------
# 0501
# 0153


# -------- Generate labeled spectra plot ---------------------------
# Make subarrays for color coding
opt = df[(df['w'] <= 0.950454)]
overlap = df[(df['w'] >= 0.950328) & (df['w'] <= 1.03426)]
# nir = df[(df['w'] > 1.03426)]  # Split bands and cut out some junk
h = df[(df['w'] >= 1.48933) & (df['w'] <= 1.8)]
k = df[(df['w'] >= 2.0175)]
zj = df[(df['w'] >= 0.950328) & (df['w'] <= 1.3500)]

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.loglog(opt['w'], opt['f'], c='#0179FF')
ax1.loglog(overlap['w'], overlap['f'], c='#009B45', lw=5, alpha=0.5)
ax1.loglog(overlap['w'], overlap['f'], c='#0179FF', alpha=0.8)  # alpha=0.3 for transparency
ax1.loglog(zj['w'], zj['f'], c='#009B45')
ax1.loglog(h['w'], h['f'], c='#009B45')
ax1.loglog(k['w'], k['f'], c='#009B45')
ax1.scatter(df2['w'][0], df2['f'][0],  c='#f768a1', s=100)
ax1.scatter(df2['w'][1], df2['f'][1],  c='#c51b8a', s=100)
ax1.scatter(df2['w'][2], df2['f'][2],  c='#c51b8a', s=100)
ax1.scatter(df2['w'][3], df2['f'][3],  c='#7a0177', s=100)
ax1.scatter(df2['w'][4], df2['f'][4],  c='#7a0177', s=100)
plt.xlim([0.59, 4.8])
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
# plt.xticks(fontsize=15)  # TODO: Look into how to change size of minor ticks, but only show some
# plt.yticks(fontsize=15)
plt.xlabel('$\lambda$ ($\mu m$)', fontsize=15)

# plt.xticks([0.6, 1, 2, 3, 4], fontsize=15)







# Error bars are too small on this scale, keep for later?
# ax1.errorbar(df2['w'][0], df2['f'][0], yerr=df2['err'][0], c='#f768a1')
# ax1.errorbar(df2['w'][1], df2['f'][1], yerr=df2['err'][1], c='#c51b8a')
# ax1.errorbar(df2['w'][2], df2['f'][2], yerr=df2['err'][2], c='#c51b8a')
# ax1.errorbar(df2['w'][3], df2['f'][3], yerr=df2['err'][3], c='#7a0177')
# ax1.errorbar(df2['w'][3], df2['f'][3], yerr=df2['err'][3], c='#7a0177')
# ax1.errorbar(df2['w'][4], df2['f'][4], yerr=df2['err'][4], c='#7a0177')

# -------- Generate plots ---------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)  # 111 tells you how many rows, how many columns, and which subplot talking about

ax1.loglog(w_1256, f_1256, c='blue')
ax1.scatter(phot1256_w, phot1256_f,  c='blue')
ax1.loglog(w_1626, f_1626, c='black')
ax1.scatter(phot1626_w, phot1626_f, c='black')


plt.xlabel('$\lambda$ ($\mu m$)', fontsize=18)
plt.ylabel('$F_\lambda (erg\ s^{-1} cm^{-2} A^{-1})$', fontsize=18)  # slash\ in mathrm is a space!
plt.title('$Subdwarfs$', fontsize=18)

plt.savefig('/Plots/Subdwarf_comaprison.png')

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)  # 111 tells you how many rows, how many columns, and which subplot talking about

ax2.loglog(nw, nf, c='blue')
ax2.scatter(phot1256_w, phot1256_f,  c='blue')


# ------Not Using anymore------
# data = pd.read_csv('Redone/optsmoothed1256-0224 (L3.5sd) SED.txt',sep=" ", header = 1)
# data.columns = ["w", "f", "err"]
# phot = pd.read_csv('Redone/optsmoothed1256-0224 (L3.5sd) phot.txt',sep=" ", header = 1)
# phot.columns = ['filter', "wav", "flux", 'unc']
# ----------------------------------------------------------------------------------------
# ------------------ Remove bad visual spikes form 1256-0224 -----------------------------
# ----------------------------------------------------------------------------------------

# data.max()
# data['f'].argmax()
# df =data.drop(data['f'].argmax())
# df.max()
# df1 = df.drop(df['f'].argmax())
# df1.max()
# df2 = df1.drop(df1['f'].argmax())
#
# df3 = df2.drop(df2['f'].argmax())
# # TODO: How to do this task more effectively
#
# # continue on removing maxes
#
# # ---- Using numpy.delete
# f_1256n.max()
# Out[87]: 1.4832570122223082e-13
# f_1256n.argmax()
# Out[88]: 9335
# f_1256n = np.delete(f_1256n, 9335)
# w_1256n = np.delete(w_1256n, 9335)
#
#
# # To slice by wavelength
# df=data[(data['w'] >= 1.10) & (data['w']< 1.15)]
# df1 = df.loc[df['f']!=df['f'].max()] # finds values that aren't the flux max
#
# # ----To Plot
# df1.plot(x='w', y='f', loglog = True)
#
# ax = phot.plot(x='wav', y='flux', loglog = True, legend = False, kind = 'scatter',yerr='unc', color = 'black', s = 50)
# df4.plot(x='w', y='f', loglog = True, legend = False, ax=ax)
