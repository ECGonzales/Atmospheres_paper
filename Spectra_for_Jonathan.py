from astrodbkit import astrodb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


db = astrodb.Database('/Users/EileenGonzales/Dropbox/BDNYC/BDNYCdb_copy/BDNYCdevdb/bdnycdev.db')

# --------- SED plot for Jonathan comparing SpeX to new K band reduction --------
# 1- Get spectra
spex = db.query("SELECT spectrum from spectra where id=320", fetch='one', fmt='dict')
w_spex, f_spex, e_spex = spex['spectrum'].data

FIRE = db.query("SELECT spectrum from spectra where id=3044", fetch='one', fmt='dict')
w_fire, f_fire, e_fire = FIRE['spectrum'].data

# 2- Make a pandas data frame
df_spex= pd.DataFrame()
df_spex['w'] = w_spex
df_spex['f'] = f_spex
df_spex['e'] = e_spex

df_fire= pd.DataFrame()
df_fire['w'] = w_fire
df_fire['f'] = f_fire
df_fire['e'] = e_fire

# 3- Trim garbage and smooth FIRE
# 4- Determine where to normalize
# 5- Normalize and plot
# Selecting a region to normalize over and normalizing
normregion=df1[(df1['w'] >= 12550) & (df1['w'] <= 12600)]
normf1= df1['f']/(np.max(normregion['f']))

