import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import ScalarFormatter


# Read in SED
df = pd.read_csv('Redone/Jonathan1256-0224 (L3.5sd) SED.txt', sep=" ", header=1, names=["w", "f", "err"])
df2 = pd.read_csv('Redone/Jonathan1256-0224 (L3.5sd) phot.txt', sep=" ", header=1, names=["w", "f", "err"])

split_spec = pd.read_csv('Redone/Jonathan_split1256-0224 (L3.5sd) SED.txt', sep=" ", header=1, names=["w", "f", "err"])
split_phot = pd.read_csv('Redone/Jonathan_split1256-0224 (L3.5sd) phot.txt', sep=" ", header=1, names=["w", "f", "err"])

spexk = pd.read_csv('Redone/SpexK1256-0224 (L3.5sd) SED.txt', sep=" ", header=1, names=["w", "f", "err"])
spex_photk = pd.read_csv('Redone/SpexK1256-0224 (L3.5sd) phot.txt', sep=" ", header=1, names=["w", "f", "err"])

# Break up JHK to remove connecting line
# opt = df[(df['w'] <= 1.115)]
# j = df[(df['w'] >= 1.15314) & (df['w'] <= 1.350)]
# h = df[(df['w'] >= 1.4987) & (df['w'] <= 1.79588)]
# k = df[(df['w'] >= 2.01515)]

# ------ Creating the figure --------

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.loglog(split_spec['w'], split_spec['f'], c='black')
ax1.scatter(split_phot['w'], split_phot['f'], c='blue', s=175)
ax1.loglog(df['w'], df['f'], c='green')
# plt.scatter(df2['w'], df2['f'], c='green', s=175)  # The photometric points are the same so only need them once
ax1.loglog(spexk['w'], spexk['f'], c='red')
# plt.scatter(spex_photk['w'], spex_photk['f'], c='red', s=175)

# -----Axes labels and reformatting
plt.ylabel('Flux $(erg\ s^{-1} cm^{-2} A^{-1})$', fontsize= 12)
plt.yticks(fontsize=12)
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_minor_formatter(ScalarFormatter())
ax1.xaxis.set_minor_locator(plt.FixedLocator([0.6,2, 3, 4]))
ax1.tick_params(axis='x', which='major',labelsize=12)
ax1.tick_params(axis='x', which='minor',labelsize=12)
plt.xlabel('Wavelength ($\mu m$)', fontsize=12)

# ------- Labeling the Spectra -----------
red_spec = mpatches.Patch(color='red',label='SpeX')
black_spec = mpatches.Patch(color='black',label='FIRE Split')
green_spec = mpatches.Patch(color='green',label='FIRE new spectra')
plt.legend(handles=[red_spec, black_spec, green_spec])

# ------ Before saving make sure that the axes labels can be seen, resize as necessary -----
plt.savefig('Plots/Comparison_SpeX_FIRE_new.png')
