#must do this all line by line in ipython to work. maybe try in terminal?
#Run when in NSBP poster folder.
ipython --pylab

import numpy as np

#Read in text files
w,f,u = np.loadtxt('FIREfp1256-0224 (L3.5sd) SED.txt', delimiter=' ', unpack=True) #smoothed
wp,fp,up = np.loadtxt('FIRE1256-0224 (L3.5sd) phot.txt', delimiter= ' ',usecols=(1,2,3), unpack=True)
w1, f1, u1 = np.loadtxt('FIREextras1256-0224 (L3.5sd) SED.txt', delimiter=' ', unpack=True) 
w1s, f1s, u1s = np.loadtxt('FIREextrassmooth1256-0224 (L3.5sd) SED.txt', delimiter=' ', unpack=True) 
w1t, f1t, u1t = np.loadtxt('FIREextrastrim1256-0224 (L3.5sd) SED.txt', delimiter=' ', unpack=True) 
w1st, f1st, u1st = np.loadtxt('FIREextrassmoothtrim1256-0224 (L3.5sd) SED.txt', delimiter=' ', unpack=True) 
#------------Ones with same Teff------------
w2, f2, u2 = np.loadtxt('FIRE1207-3900 (L0gamma) SED.txt', delimiter=' ', unpack=True)
wp2, fp2, up2 = np.loadtxt('FIRE1207-3900 (L0gamma) phot.txt', delimiter= ' ',usecols=(1,2,3), unpack=True)

w3, f3, u3 = np.loadtxt('FIRE0223-5815 (L0gamma) SED.txt', delimiter=' ', unpack=True)
wp3, fp3, up3 = np.loadtxt('FIRE0223-5815 (L0gamma) phot.txt', delimiter= ' ', usecols=(1,2,3), unpack=True)

w4, f4, u4 = np.loadtxt('0033-1521 (L2.5beta) SED.txt', delimiter=' ', unpack=True)
wp4, fp4, up4 = np.loadtxt('0033-1521 (L2.5beta) phot.txt', delimiter= ' ', usecols=(1,2,3),unpack=True)

w5, f5, u5 = np.loadtxt('0036+1821 (L3.5) SED.txt', delimiter=' ', unpack=True)
wp5, fp5, up5 = np.loadtxt('0036+1821 (L3.5) phot.txt', delimiter= ' ', usecols=(1,2,3),unpack=True)

w6, f6, u6 = np.loadtxt('2208+2921 (L3gamma) SED.txt', delimiter=' ', unpack=True)
wp6, fp6, up6 = np.loadtxt('2208+2921 (L3gamma) phot.txt', delimiter= ' ', usecols=(1,2,3),unpack=True)

#--------ones of same Lbol---------------
w7, f7, u7 = np.loadtxt('FIRE2206-4217 (L4gamma) SED.txt', delimiter=' ', unpack=True)
wp7, fp7, up7 = np.loadtxt('FIRE2206-4217 (L4gamma) phot.txt', delimiter= ' ', usecols=(1,2,3),unpack=True)

w8, f8, u8 = np.loadtxt('0445-3048 (L2) SED.txt', delimiter=' ', unpack=True)
wp8, fp8, up8 = np.loadtxt('0445-3048 (L2) phot.txt', delimiter= ' ',usecols=(1,2,3), unpack=True)

w9, f9, u9 = np.loadtxt('opt1320+0409 (L3) SED.txt', delimiter=' ', unpack=True)
wp9, fp9, up9 = np.loadtxt('opt1320+0409 (L3) phot.txt', delimiter= ' ',usecols=(1,2,3), unpack=True)

w10, f10, u10 = np.loadtxt('1841+3117 (L4p) SED.txt', delimiter=' ', unpack=True)
wp10, fp10, up10 = np.loadtxt('1841+3117 (L4p) phot.txt', delimiter= ' ',usecols=(1,2,3), unpack=True)

#--------Generate plot with all of same Teff---------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111) #111 tells you how many rows, how many columns, and which subplot talking about

ax1.loglog(w,f,c='blue')
ax1.scatter(wp,fp, c='blue')
ax1.loglog(w2,f2,c='red')
ax1.scatter(wp2,fp2, c='red')
ax1.loglog(w3,f3,c='green')
ax1.scatter(wp3,fp3, c='green')
ax1.loglog(w4,f4,c='orange')
ax1.scatter(wp4,fp4, c='orange')
ax1.loglog(w5,f5,c='slategray')
ax1.scatter(wp5,fp5, c='slategray')
ax1.loglog(w6,f6,c='purple')
ax1.scatter(wp6,fp6, c='purple')

plt.xlabel('$\lambda$ ($\mu m$)',fontsize=18)
plt.ylabel('$F_\lambda (erg\ s^{-1} cm^{-2} A^{-1})$ ',fontsize=18) #slash\ in mathrm is a space!
plt.title('$Same\ T_{eff}$',fontsize=18)

plt.savefig('/Users/EileenGonzales/Dropbox/BDNYC/BDNYC_Research/Jackie_SEDs/NSBP_poster_SEDs/Teff.png')

#------------Make same Lbol plot----------------
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

ax2.loglog(w,f,c='blue')
ax2.scatter(wp,fp, c='blue')
ax2.loglog(w7,f7,c='red')
ax2.scatter(wp7,fp7, c='red')
ax2.loglog(w8,f8,c='green')
ax2.scatter(wp8,fp8, c='green')
ax2.loglog(w9,f9,c='slategray')
ax2.scatter(wp9,fp9, c='slategray')
ax2.loglog(w10,f10,c='teal')
ax2.scatter(wp10,fp10, c='teal')

plt.savefig('/Users/EileenGonzales/Dropbox/BDNYC/BDNYC_Research/Jackie_SEDs/NSBP_poster_SEDs/Lbol.png')
#----------------------------------------------------------------------------------------
#--------------------------FINAL POSTER PLOTS--------------------------------------------
#----------------------------------------------------------------------------------------
#1256 alone to used as explaination plot
#these are the array line number btwn opt and IR
opt = w[:8019] 
optf= f[:8019]
nirw= w[8019:]
nirf =f[8019:]

fig3, ax3 =plt.subplots()
ax3.loglog(opt,optf, c='darkgreen')
ax3.scatter(wp,fp, c='purple', s=100)
ax3.loglog(nirw,nirf,c='darkorange')
plt.xticks([0.1,1,10],fontsize=20)
plt.yticks([1e-19,1e-18,1e-17,1e-16,1e-15,1e-14,1e-13],fontsize=20)
plt.xlabel('$\lambda$ ($\mu m$)', fontsize=30)
plt.ylabel('$F_\lambda (erg\ s^{-1} cm^{-2} A^{-1})$ ',fontsize=30)
plt.title('$1256-0224$',fontsize=30)

#TEff with 0223
fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
ax4.loglog(w3,f3,c='red')
ax4.scatter(wp3,fp3, c='red', s=25)
ax4.loglog(w5,f5,c='slategray')
ax4.scatter(wp5,fp5, c='slategray', s=25)
ax4.loglog(w,f,c='blue')
ax4.scatter(wp,fp, c='blue', s=25)
plt.xticks([0.1,1,10,100],fontsize=20)
plt.yticks([1e-19,1e-18,1e-17,1e-16,1e-15,1e-14],fontsize=20)
plt.xlabel('$\lambda$ ($\mu m$)', fontsize=30)
plt.ylabel('$F_\lambda (erg\ s^{-1} cm^{-2} A^{-1})$ ',fontsize=30)

#------------Make same Lbol plot----------------
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

ax2.loglog(w7,f7,c='red')
ax2.scatter(wp7,fp7, c='red' ,s=25)
ax2.loglog(w5,f5,c='slategray') #trying 0036 instead of w9
ax2.scatter(wp5,fp5, c='slategray',s=25)
ax2.loglog(w,f,c='blue')
ax2.scatter(wp,fp, c='blue',s=25)
plt.xticks([0.1,1,10,100],fontsize=20)
plt.yticks([1e-19,1e-18,1e-17,1e-16,1e-15,1e-14],fontsize=20)
plt.xlabel('$\lambda$ ($\mu m$)', fontsize=30)
plt.ylabel('$F_\lambda (erg\ s^{-1} cm^{-2} A^{-1})$ ',fontsize=30)


#Mulitpanel plots
#normalize each of the spectra by the max point overall
nf1s=f1s/max(f1s)
nf1st=f1st/max(f1st)
nf1t=f1t/max(f1t)
nf2=f2/max(f2)
nf3=f3/max(f3)
nf5=f5/max(f5)
nf7=f7/max(f7)
nf8=f8/max(f8)
nf9=f9/max(f9)
nf1=f1/max(f1)

#0.95-1.10
#Normalize for this region
f1stZ= f1st[:] 
w1stZ= w1st[:]
nf1stZ=f1stZ/max(f1stZ)
f5Z= f5[:] 
w5Z= w5[:]
nf5Z=f5Z/max(f5Z)
f2Z= f2[:] 
w2Z= w2[:]
nf2Z=f2Z/max(f2Z)
#teff
fig5 = plt.figure()
ax5 = fig5.add_subplot(111)
ax5.plot(w1st,nf1st, c="blue")
ax5.plot(w5,nf5 + 0.5, c="slategray")
ax5.plot(w2,nf2 + 1, c="red")
plt.xlim([0.95,1.10])
plt.ylim([-0.2,1.6])
plt.xticks([0.96,0.98,1.00,1.02,1.04,1.06,1.08,1.10],fontsize=20)
plt.yticks([-0.2,0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6],fontsize=20)
plt.xlabel('$\lambda$ ($\mu m$)', fontsize=30)
plt.ylabel('$Normalized\ Flux (F_\lambda)$ ',fontsize=30)

#lbol
fig5 = plt.figure()
ax5 = fig5.add_subplot(111)
ax5.plot(w1st,nf1st, c="blue")
ax5.plot(w5,nf5 +0.5, c="slategray")
ax5.plot(w7,nf7 + 1, c="red")
plt.xlim([0.95,1.10])
plt.ylim([-0.2,1.6])
plt.xticks([0.96,0.98,1.00,1.02,1.04,1.06,1.08,1.10],fontsize=20)
plt.yticks([-0.2,0.0,0.2,0.4,0.6,0.8,1.0,1.2,],fontsize=20)
plt.xlabel('$\lambda$ ($\mu m$)', fontsize=30)
plt.ylabel('$Normalized\ Flux (F_\lambda)$ ',fontsize=30)

#1.12-1.35
#teff
fig6 = plt.figure()
ax6 = fig6.add_subplot(111)
ax6.plot(w1st,nf1st, c="blue")
ax6.plot(w5,nf5 + 0.5, c="slategray")
ax6.plot(w2,nf2 + 1.2, c="red")
plt.xlim([1.12,1.35])
plt.ylim([-0.2,2.5])
plt.xticks([1.15,1.20,1.25,1.30,1.35],fontsize=20)
plt.yticks([0.0,0.5,1.0,1.5,2.0,2.5],fontsize=20)
plt.xlabel('$\lambda$ ($\mu m$)', fontsize=30)
plt.ylabel('$Normalized\ Flux (F_\lambda)$ ',fontsize=30)

#lbol
fig6 = plt.figure()
ax6 = fig6.add_subplot(111)
ax6.plot(w1st,nf1st, c="blue")
ax6.plot(w9,nf9 + 0.5, c="slategray")
ax6.plot(w7,nf7 + 1.2, c="red")
plt.xlim([1.12,1.35])
plt.ylim([-0.2,2.5])
plt.xticks([1.15,1.20,1.25,1.30,1.35],fontsize=20)
plt.yticks([0.0,0.5,1.0,1.5,2.0,2.5],fontsize=20)
plt.xlabel('$\lambda$ ($\mu m$)', fontsize=30)
plt.ylabel('$Normalized\ Flux (F_\lambda)$ ',fontsize=30)

#1.42-1.80
normalize for this region
f1tH= f1t[13223:17583] 
w1tH= w1t[13223:17583]
nf1tH=f1tH/max(f1tH)
f1stH= f1st[13122:17593] 
w1stH= w1st[13122:17593]
nf1stH=f1stH/max(f1stH)

#teff
fig7 = plt.figure()
ax7 = fig7.add_subplot(111)
ax7.plot(w1stH,nf1stH, c="blue")
ax7.plot(w5,nf5 + 0.7, c="slategray")
ax7.plot(w2,nf2 + 1.2, c="red")
plt.xlim([1.42,1.80])
plt.ylim([0.0,2.5])
plt.xticks([1.45,1.50,1.55,1.60,1.65,1.70,1.75,1.80],fontsize=20)
plt.yticks([0.0,0.5,1.0,1.5,2.0,2.5],fontsize=20)
plt.xlabel('$\lambda$ ($\mu m$)', fontsize=30)
plt.ylabel('$Normalized\ Flux (F_\lambda)$ ',fontsize=30)

#lbol
fig7 = plt.figure()
ax7 = fig7.add_subplot(111)
ax7.plot(w1stH,nf1stH, c="blue")
ax7.plot(w9,nf9 + 0.7, c="slategray")
ax7.plot(w7,nf7 + 1.2, c="red")
plt.xlim([1.42,1.80])
plt.ylim([0.0,2.5])
plt.xticks([1.45,1.50,1.55,1.60,1.65,1.70,1.75,1.80],fontsize=20)
plt.yticks([0.0,0.5,1.0,1.5,2.0,2.5],fontsize=20)
plt.xlabel('$\lambda$ ($\mu m$)', fontsize=30)
plt.ylabel('$Normalized\ Flux (F_\lambda)$ ',fontsize=30)

#2.0-2.35
normalize for this region
f1tK= f1t[17584:21314] 
w1tK= w1t[17584:21314]
nf1tK=f1tK/max(f1tK)
f1stK= f1st[17764:21551] 
w1stK= w1st[17764:21551]
nf1K=f1stK/max(f1stK)

#teff
fig6 = plt.figure()
ax6 = fig6.add_subplot(111)
ax6.plot(w1stK,nf1K, c="blue")
ax6.plot(w5,nf5 + 1, c="slategray")
ax6.plot(w2,nf2 + 1.5, c="red")
plt.xlim([2.0,2.35])
plt.ylim([-0.2,2.5])
plt.xticks([2.0,2.05,2.10,2.15,2.20,2.25,2.30,2.35],fontsize=20)
plt.yticks([0.0,0.5,1.0,1.5,2.0,2.5],fontsize=20)
plt.xlabel('$\lambda$ ($\mu m$)', fontsize=30)
plt.ylabel('$Normalized\ Flux (F_\lambda)$ ',fontsize=30)

#Lbol
fig6 = plt.figure()
ax6 = fig6.add_subplot(111)
ax6.plot(w1tK,nf1tK, c="blue")
ax6.plot(w9,nf9 + 1, c="slategray")
ax6.plot(w7,nf7 + 1.5, c="red")
plt.xlim([2.0,2.35])
plt.ylim([-0.2,2.5])
plt.xticks([2.0,2.05,2.10,2.15,2.20,2.25,2.30,2.35],fontsize=20)
plt.yticks([0.0,0.5,1.0,1.5,2.0,2.5],fontsize=20)
plt.xlabel('$\lambda$ ($\mu m$)', fontsize=30)
plt.ylabel('$Normalized\ Flux (F_\lambda)$ ',fontsize=30)

#not needed
ax3.set_xticks([0.1, 1, 10])
ax3.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
#Trying to get bold in mathmode
In [126]: plt.title('$\mathbf{Same\ T_{eff}}$',fontsize=18)
In [127]: plt.ylabel('\mathbf{F_\lambda (erg\ s^{-1} cm^{-2} A^{-1})} ',fontsize=18, fontweight='bold')
In [128]: plt.ylabel('$\mathbf{F_\lambda (erg\ s^{-1} cm^{-2} A^{-1})}$ ',fontsize=18, fontweight='bold')
In [129]: plt.xlabel('$\mathbf{\lambda (\mu m)}$',fontsize=18)