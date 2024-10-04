import math

# Original inductance and capacitance values
L_orig = 625e-6  # in henrys
C_orig = 25e-12  # in farads
R = 80e3  # in ohms

# New inductance value
L_new = 75e-6  # in henrys

# Center frequency for the scaled filter
f0 = 700e3  # in radians per second (500 krad/s)

# Calculate the resonant frequency with the original inductance and capacitance
f0_orig = 1 / (2 * math.pi * math.sqrt(L_orig * C_orig))

# Calculate the quality factor Q using the original resonant frequency
Q = R / (2 * math.pi * f0_orig * L_orig)

# Now we use the Q and the new f0 to calculate the new bandwidth beta
beta_new = f0 / Q

# Calculate the new capacitance value to maintain the original resonant frequency with the new inductor
C_new = (L_orig / L_new) * C_orig

# Output the quality factor, new bandwidth in rad/s, and new capacitance in picofarads
Q, beta_new, C_new * 1e12  # Convert capacitance to pF for readability

print(Q)
print(beta_new)
print(C_new*1e12)