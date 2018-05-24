# The equations come from Stephens 2004 (in BDNYC_Research folder)
import numpy as np

# band  m       m_unc   M   M_unc
# MKO_H 16.078 0.016 11.572 0.126
# MKO_K 16.605 0.099 12.099 0.159

# Convert MKO photometry into 2MASS using the following equations
m_H = 16.078
m_H_unc = 0.016
m_K = 16.605
m_K_unc = 0.018
dist = 79.67
dist_err = 4.57

TwoMASS_H = -0.034 + (-6.88e-3 * 3.5) + (6.27e-4 * 3.5 ** 2) + (-1.43e-5 * 3.5 ** 3) + m_H
TwoMASS_K = -0.004 + (2.04e-2 * 3.5) + (-2.80e-3 * 3.5**2) + (6.75e-5 * 3.5**3) + m_K

AbsmagH = -(5*np.log10(dist)-5) + TwoMASS_H
AbsmagH_unc = np.sqrt(m_H_unc ** 2 + 25 * (dist_err / (dist * np.log(10)))**2)

AbsmagK = -(5*np.log10(dist)-5) + TwoMASS_K
AbsmagK_unc = np.sqrt(m_K_unc ** 2 + 25 * (dist_err / (dist * np.log(10)))**2)

print(AbsmagH, AbsmagH_unc)
print(AbsmagK, AbsmagK_unc)

# Calculate Abs Maf for 1256-1408
MASS_J = 14.011
MASS_Jerr = 0.027
MASS_H = 13.618
MASS_H_err = 0.033
MASS_Ks = 13.444
MASS_Kserr = 0.037
WISE_W1 = 13.118
WISE_W1err = 0.026
WISE_W2 = 12.896
WISE_W2err = 0.028

dist_1408 = 44.4
dist_err_1408 = 0.39

AbsJ = -(5*np.log10(dist_1408)-5) + MASS_J
AbsJ_unc = np.sqrt(MASS_Jerr ** 2 + 25 * (dist_err_1408 / (dist * np.log(10)))**2)
AbsH = -(5*np.log10(dist_1408)-5) + MASS_H
AbsH_unc = np.sqrt(MASS_H_err ** 2 + 25 * (dist_err_1408 / (dist * np.log(10)))**2)
AbsK = -(5*np.log10(dist_1408)-5) + MASS_Ks
AbsK_unc = np.sqrt(MASS_Kserr ** 2 + 25 * (dist_err_1408 / (dist * np.log(10)))**2)
AbsW1 = -(5*np.log10(dist_1408)-5) + WISE_W1
AbsW1_unc = np.sqrt(WISE_W1err ** 2 + 25 * (dist_err_1408 / (dist * np.log(10)))**2)
AbsW2 = -(5*np.log10(dist_1408)-5) + WISE_W2
AbsW2_unc = np.sqrt(WISE_W2err ** 2 + 25 * (dist_err_1408 / (dist * np.log(10)))**2)

print(AbsJ , AbsJ_unc)
print(AbsH , AbsH_unc)
print(AbsK , AbsK_unc)
print(AbsW1 , AbsW1_unc)
print(AbsW2 , AbsW2_unc)