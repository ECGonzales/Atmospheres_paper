# ------Not Using anymore------
# data = pd.read_csv('Redone/optsmoothed1256-0224 (L3.5sd) SED.txt',sep=" ", header = 1)
# data.columns = ["w", "f", "err"]
# phot = pd.read_csv('Redone/optsmoothed1256-0224 (L3.5sd) phot.txt',sep=" ", header = 1)
# phot.columns = ['filter', "wav", "flux", 'unc']
# ----------------------------------------------------------------------------------------
# ------------------ Remove bad visual spikes form 1256-0224 -----------------------------
# ----------------------------------------------------------------------------------------

# data.max()
# data['f'].argmax()
# df =data.drop(data['f'].argmax())
# df.max()
# df1 = df.drop(df['f'].argmax())
# df1.max()
# df2 = df1.drop(df1['f'].argmax())
#
# df3 = df2.drop(df2['f'].argmax())
# # TODO: How to do this task more effectively
#
# # continue on removing maxes
#
# # ---- Using numpy.delete
# f_1256n.max()
# Out[87]: 1.4832570122223082e-13
# f_1256n.argmax()
# Out[88]: 9335
# f_1256n = np.delete(f_1256n, 9335)
# w_1256n = np.delete(w_1256n, 9335)
#
#
# # To slice by wavelength
# df=data[(data['w'] >= 1.10) & (data['w']< 1.15)]
# df1 = df.loc[df['f']!=df['f'].max()] # finds values that aren't the flux max
#
# # ----To Plot
# df1.plot(x='w', y='f', loglog = True)
#
# ax = phot.plot(x='wav', y='flux', loglog = True, legend = False, kind = 'scatter',yerr='unc', color = 'black', s = 50)
# df4.plot(x='w', y='f', loglog = True, legend = False, ax=ax)