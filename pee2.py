import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# Constants
cutoff_freq = 700  # in Hz
passband_gain = 8  # in linear scale (not dB)

# Capacitance in Farads
C = 75e-9  # 75 nF

# Passband gain of the filter is given by -R2/R1
# We also know the cut-off frequency of the filter is determined by 1/(2*pi*R2*C)
# We have two equations:
# 1) R2/R1 = -passband_gain (since the gain is 12, we take the magnitude as op-amps inverting configuration)
# 2) 1/(2*pi*R2*C) = cutoff_freq

# To solve these equations we rearrange them:
# R1 = R2/passband_gain
# R2 = 1 / (2 * pi * C * cutoff_freq)

# Calculate R2
R2 = 1 / (2 * np.pi * C * cutoff_freq)

# Calculate R1 using the relationship between R1 and R2
R1 = R2 / passband_gain

R1_kOhm = R1 / 1e3  # Convert ohms to kilohms
R2_kOhm = R2 / 1e3  # Convert ohms to kilohms

print(R1_kOhm)
print(R2_kOhm)
