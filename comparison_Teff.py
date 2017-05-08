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

# -------- Comparison Plot: Teff ---------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)  # 111 tells you how many rows, how many columns, and which subplot talking about

ax1.loglog(df['w'], df['f'], c='blue')
ax1.scatter(df2['w'],df2['f'],  c='blue')
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



