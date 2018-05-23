# The equations come from Stephens 2004 (in BDNYC_Research folder)
import numpy as np

# band  m       m_unc   M   M_unc
# MKO_H 16.078 0.016 11.572 0.126
# MKO_K 16.605 0.099 12.099 0.159

# Convert MKO photometry into 2MASS using the following equations
m_H = 16.078
m_H_unc = 0.016
m_K = 16.605
m_K_unc = 0.099
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

