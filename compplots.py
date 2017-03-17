import numpy as np
import matplotlib.pyplot as plt
import scipy


# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# -------------------------------------------------------------------------------------

# ------------ 1256-0224 (Proper- spikes kept in SED)----------------
w_1256, f_1256, unc_1256 = np.loadtxt('Redone/FIRE1256-0224 (L3.5sd) SED.txt', delimiter=' ', unpack=True)
phot1256_w, phot1256_f , phot1256_err = np.loadtxt('Redone/FIRE1256-0224 (L3.5sd) phot.txt', delimiter=' ',
                                                   usecols=(1,2,3), unpack=True)

# ------------- Comparison Objects -------------------
# No problem spectra for 1626+3925
w_1626, f_1626, unc_1626 = np.loadtxt('Redone/MIR(2)1626+3925 (L4sd) SED.txt', delimiter=' ', unpack=True)
phot1626_w, phot1626_f, phot1626_err = np.loadtxt('Redone/MIR(2)1626+3925 (L4sd) phot.txt', delimiter=' ',
                                                  usecols=(1,2,3), unpack=True)

# ----------------------------------------------------------------------------------------
# ------------------ Remove bad visual spikes form 1256-0224 -----------------------------
# ----------------------------------------------------------------------------------------

# Use dem pandas
import pandas as pd
data = pd.read_csv('Redone/FIRE1256-0224 (L3.5sd) SED.txt',sep=" ", header = 1)
data.columns = ["w", "f", "err"]

data.max()
data['f'].argmax()
df =data.drop(data['f'].argxmax())
df.max()
df1 = df.drop(df['f'].argmax())
df1.max()
df2 = df1.drop(df1['f'].argmax())

df3 = df2.drop(df2['f'].argmax())
# TODO: How to do this task more effectively

# continue on removing maxes

# To slice by wavelength
df=data[(data['w'] >= 1.10) & (data['w']< 1.15)]
df1 = df.loc[df['f']!=df['f'].max()] # finds values that aren't the flux max

# ----To Plot
df1.plot(x='w', y='f', loglog = True)


# -------- Generate plot ---------------------------
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
