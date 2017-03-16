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

# Split an array
a = w_1256[w_1256 >= 1.10]
b = a[a < 1.15]

c = f_1256[8602:9559] # I had to look this up in the txt file. HELP!!!
bad = np.amax(b)


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
