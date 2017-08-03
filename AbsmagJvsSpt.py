



df_sub = pd.read_csv('Data/Subdwarf_Spt_v_Teff.txt', sep=" ", comment='#', header=None,
                      names=["name", "SpT", "Teff", 'Teff_err', 'lbol', 'lbol_err', 'mass', 'mass_unc', 'MJ','MJ_unc',
                             'MH', 'MH_unc','MK','MK_unc','MW1','MW1_unc','MW2','MW2_unc'])
df_field = pd.read_csv('Data/Parallaxes-Normal.txt', sep=" ", comment='#', header=None,
                      names=['name', 'SPT', 'Pi', 'Pi_er', 'Jmagn_MKO', 'Jerr_MKO', 'Hmagn_MKO', 'Herr_MKO', 'Kmagn_MKO',
                             'Kerr_MKO', 'W1magn', 'W1err', 'W2magn', 'W2err', 'W3magn', 'W3err', 'W4magn', 'W4err',
                             'Jmagn', 'Jerr', 'Hmagn', 'Herr', 'Kmagn', 'Kerr', 'Lmag', 'Lerr'])