from astrodbkit import astrodb
from SEDkit import SEDs
from SEDkit import utilities as u

FILTERS = u.get_filters()

# Convert Magnitudes to Fluxes for 1308 (sdL5 missing opt phot) and 1468 (sdL4)
# 1308
J_1308 = u.mag2flux('2MASS_J', 16.403, 0.113, filter_dict=FILTERS)

# 1468
J_1468 = u.mag2flux('2MASS_J', 14.435, 0.029, filter_dict=FILTERS)
z_1468 = u.mag2flux('SDSS_z', 16.13, 0.01, filter_dict=FILTERS)

# using the output solve J_1308/J_1468 = x/z_1468
r_flux = J_1308[0]/J_1468[0]
Z_1308_flux = r_flux * z_1468[0]

r_err = J_1308[1]/J_1468[1]
Z_1308_err = r_err * z_1468[1]

# Convert results back into a magnitude to then add to the database
z_1308 = u.flux2mag('SDSS_z', Z_1308_flux, Z_1308_err, filter_dict=FILTERS)
# output: [18.097999999999999, 0.038965517241379304]
# I will round to two decimal points since that is what the largest original error was. (Correct to do?)

# Didn;t scale with just z trying SDSS_i as well
i_1468 = u.mag2flux('SDSS_i', 17.92, 0.01, filter_dict=FILTERS)

# Solve new ratio
i_1308_flux = r_flux * i_1468[0]
i_1308_err = r_flux * i_1468[1]

# convert to magnitude
i_1308 = u.flux2mag('SDSS_i', i_1308_flux, i_1308_err, filter_dict=FILTERS)
# Output: [19.888000000000002, 0.0099999999999999967]
