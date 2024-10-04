import numpy as np

# Given values
Av_dB = 10          # passband gain in dB
fc = 2500           # cutoff frequency in Hz
C = 4e-9            # capacitance in Farads (2 nF)

# Calculating the actual voltage gain A from the given passband gain Av (in dB)
A = 10**(Av_dB / 20)

# Calculate R2 using the cutoff frequency formula fc = 1/(2*pi*R2*C)
R2 = 1 / (2 * np.pi * fc * C)

# Calculate R1 using the voltage gain formula A = R2/R1
R1 = R2 / A

# Convert R1 and R2 to kilohms
R1_kohms = R1 / 1000
R2_kohms = R2 / 1000

# Round the values to three significant figures
R1_kohms_rounded = round(R1_kohms, 3 - int(np.floor(np.log10(abs(R1_kohms)))) - 1)
R2_kohms_rounded = round(R2_kohms, 3 - int(np.floor(np.log10(abs(R2_kohms)))) - 1)

print(R1_kohms_rounded) 
print(R2_kohms_rounded)
