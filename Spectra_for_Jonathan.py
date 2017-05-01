from astrodbkit import astrodb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from SEDkit import utilities as u
import matplotlib.patches as mpatches

db = astrodb.Database('/Users/EileenGonzales/Dropbox/BDNYC/BDNYCdb_copy/BDNYCdevdb/bdnycdev.db')

# --------- SED plot for Jonathan comparing SpeX to new K band reduction --------
# 1- Get spectra
spex = db.query("SELECT spectrum from spectra where id=320", fetch='one', fmt='dict')
w_spex, f_spex, e_spex = spex['spectrum'].data

FIRE = db.query("SELECT spectrum from spectra where id=3044", fetch='one', fmt='dict')
w_fire, f_fire, e_fire = FIRE['spectrum'].data

# 2- Make a pandas data frame
df_spex = pd.DataFrame()
df_spex['w'] = w_spex
df_spex['f'] = f_spex
df_spex['e'] = e_spex

df_fire = pd.DataFrame()
df_fire['w'] = w_fire
df_fire['f'] = f_fire
df_fire['e'] = e_fire

# 3- Make wavelength arrays on same scale
df_spex['w'] = df_spex['w'] * 10000

# 4- Trim garbage and smooth FIRE
df_fire = df_fire.drop(df_fire['f'].argmax())  # Repeat until looks better
# 5- Determine where to normalize
df_fire['w'] = u.smooth(df_fire['w'], 1)
df_fire['f'] = u.smooth(df_fire['f'], 1)

# 6- Normalize and plot
# Selecting a region to normalize over and normalizing
normregion = df_fire[(df_fire['w'] >= 12750) & (df_fire['w'] <= 13250)]
norm_df_fire = df_fire['f']/(np.max(normregion['f']))

normregion2 = df_spex[(df_spex['w'] >= 12750) & (df_spex['w'] <= 13250)]
norm_df_spex = df_spex['f']/(np.max(normregion2['f']))

fig2= plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(df_fire['w'], norm_df_fire)
ax2.plot(df_spex['w'], norm_df_spex)
orange_spec = mpatches.Patch(color='#ff7f0e', label='SpeX')
blue_spec = mpatches.Patch(color='#1f77b4', label='FIRE')
ax2.legend(handles=[orange_spec, blue_spec])
plt.xlabel('wavelength')
plt.ylabel('Normalized Flux')

