import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------------------------------
# ------------------- Read in Spectra and Photometry files ---------------------------
# ------------------------------------------------------------------------------------
# Read  all in as pandas Dataframes

df_1256 = pd.read_csv('Data/FIRE_rereduced1256-0224 (L3.5sd) SED.txt', sep=" ", header=1, names=["w", "f", "err"])
df_1256_phot = pd.read_csv('Data/FIRE_rereduced1256-0224 (L3.5sd) phot.txt', sep=" ", header=1, names=["w", "f", "err"])

# -------------- Comparison objects of the same Lbol ----------------------------------
df_young = pd.read_csv('Data/0501-0010 (L4gamma) SED.txt', sep=" ", header=1, names=["w", "f", "err"])
df_young_phot = pd.read_csv('Data/0501-0010 (L4gamma) phot.txt', sep=" ", header=1, names=["w", "f", "err"])
df_field = pd.read_csv('Data/lbol0342-6817 (L2/) SED.txt', sep=" ", header=1, names=["w", "f", "err"])
df_field_phot = pd.read_csv('Data/lbol0342-6817 (L2/) phot.txt', sep=" ", header=1, names=["w", "f", "err"])


# -------------------------------------------------------------------------------------
# ------------------- Plotting: Comparison of same Lbol -------------------------------
# -------------------------------------------------------------------------------------
# ------ Set up figure layout --------
fig = plt.figure()
ax1 = fig.add_subplot(111)
fig.set_size_inches(10, 8)
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

# -------- Add data -----------
ax1.loglog(df_young['w'], df_young['f'], c='#D01810')
ax1.scatter(df_young_phot['w'], df_young_phot['f'], c='k', s=70)  # The ones with size 70 are to give the circles a
ax1.scatter(df_young_phot['w'], df_young_phot['f'], c='#D01810', s=50)        # black border
ax1.loglog(df_field['w'], df_field['f'], c='#7C7D70')
ax1.scatter(df_field_phot['w'], df_field_phot['f'], c='k', s=70)
ax1.scatter(df_field_phot['w'], df_field_phot['f'], c='#7C7D70', s=50)
ax1.loglog(df_1256['w'], df_1256['f'], c='blue')
ax1.scatter(df_1256_phot['w'], df_1256_phot['f'], c='k', s=70)
ax1.scatter(df_1256_phot['w'], df_1256_phot['f'], c='blue', s=50)
