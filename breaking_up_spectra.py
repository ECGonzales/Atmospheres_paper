# Procedure on breaking up FIRE spectra into J, H and K bands for SEDs.
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('1256-0224_FIRE.txt',sep="\t ", header = 1, names=["w", "f", "err"])
# df.columns = ["w", "f", "err"]

# 1- Break into bands
zj = df[(df['w'] <= 13500)]
h = df[(df['w']>=14200) & (df['w']<18000)]
k = df[(df['w']>=20000) & (df['w']<23500)]


# 2- Plot the data to check
plt.plot(zj['w'], zj['f'])

# 3- Find the max flux
zj.max()  # Shows all max point for wavelength, flux, and error
zj['f'].argmax()  # Gets the element number of the array

# 4- Drop the bad point and repeat until satisfied via plotting
zj1 = zj.drop(zj['f'].argmax())

# 5- Drop the min bad points
zj4.min()
zj4['f'].argmin()
zj5 = zj4.drop(zj4['f'].argmin())

# 6- Write band to csv file
zj6.to_csv('z_j_bands_1256-0224FIRE.txt', sep=' ', index=False)
h5.to_csv('hband_1256-0224FIRE.txt', sep=' ', index= False)
k2.to_csv('kband_1256-0224FIRE.txt', sep=' ', index= False)

