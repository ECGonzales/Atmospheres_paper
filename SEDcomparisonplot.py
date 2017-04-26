import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


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

plt.loglog(split_spec['w'], split_spec['f'], c='black')
plt.scatter(split_phot['w'], split_phot['f'], c='blue', s=175)
plt.loglog(df['w'], df['f'], c='green')
plt.scatter(df2['w'], df2['f'], c='green', s=100)
plt.loglog(spexk['w'], spexk['f'], c='red')
plt.scatter(spex_photk['w'], spex_photk['f'], c='red', s=100)
red_spec = mpatches.Patch(color='red',label='SpeX')
black_spec = mpatches.Patch(color='black',label='FIRE Split')
green_spec = mpatches.Patch(color='green',label='FIRE new spectra')
plt.legend(handles=[red_spec, black_spec, green_spec])
plt.savefig('Plots/Comparison_SpeX_FIRE_new.png')
