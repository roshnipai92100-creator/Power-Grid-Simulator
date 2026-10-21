# Import get_valid_number from utils.py
from utils import get_valid_number

# Get source voltage and two resistances
voltage = get_valid_number("Enter source voltage (just the #): ")
resistance1 = get_valid_number("Enter resistance 1 (just the #): ", positive_only=True)
resistance2 = get_valid_number("Enter resistance 2 (just the #): ", positive_only=True)

# Calculations + Outputs (print statements)
equivalent_resistance = resistance1 * resistance2 / (resistance1 + resistance2)
print(f"\nEquivalent resistance: {equivalent_resistance:.3f} Ω")

r1_current = voltage / resistance1
print(f"Current through R1: {r1_current:.3f} A")
r2_current = voltage / resistance2
print(f"Current through R2: {r2_current:.3f} A")

total_current = r1_current + r2_current
print(f"Total current: {total_current:.3f} A")
total_power = voltage * total_current
print(f"Total power: {total_power:.3f} W")

# Tolerance for floating-point-precision error
tolerance = 1e-6
# Check if Kirchhoff's Current Law (KCL) is followed
current_error = voltage / equivalent_resistance - r1_current - r2_current
if abs(current_error) <= tolerance:
    print(f"\nKCL verification: PASSED")
else:
    print(f"\nKCL verification: FAILED")