from sympy import symbols, solve, pi

# Define the symbol for the new capacitancepython -m pip install -e 
C_prime = symbols('C_prime')

# Given values for the original filter
L = 625e-6  # Original inductance in Henry (625 µH)
C = 25e-12  # Original capacitance in Farads (25 pF)
R = 80e3  # Original resistance in Ohms (80 kΩ)
omega_0 = 700e3  # Desired center frequency in rad/s (500 krad/s)
L_prime = 75e-6  # New inductance in Henry (75 µH)

# Recalculate the new capacitance C' with the desired center frequency and new inductance L'
C_prime_new = 1 / (omega_0**2 * L_prime)

# Recalculate the original Q factor
Q_original = R * (C / L)**0.5

# Calculate the new resistance R' using the original Q and new C'
R_prime_new = Q_original * (L_prime / C_prime_new)**0.5

# Output the new capacitance and resistance values
print(C_prime_new)
print(R_prime_new)
