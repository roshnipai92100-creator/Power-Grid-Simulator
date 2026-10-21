# Import get_valid_number from utils.py
from utils import get_valid_number

# Get source voltage and three resistances
voltage = get_valid_number("Enter source voltage (just the #): ")
resistance1 = get_valid_number("Enter resistance 1 (just the #): ", positive_only=True)
resistance2 = get_valid_number("Enter resistance 2 (just the #): ", positive_only=True)
resistance3 = get_valid_number("Enter resistance 3 (just the #): ", positive_only=True)

# Calculations + Outputs (print statements)
parallel_resistance = resistance2 * resistance3 / (resistance2 + resistance3)
print(f"\nParallel resistance: {parallel_resistance:.3f} Ω")
total_resistance = resistance1 + parallel_resistance
print(f"Total resistance: {total_resistance:.3f} Ω")
total_current = voltage / total_resistance
print(f"Total current: {total_current:.3f} A")

r1_voltage = total_current * resistance1
print(f"\nVoltage across R1: {r1_voltage:.3f} V")
parallel_voltage = total_current * parallel_resistance
print(f"Voltage across parallel section: {parallel_voltage:.3f} V")

r2_current = parallel_voltage / resistance2
print(f"\nCurrent through R2: {r2_current:.3f} A")
r3_current = parallel_voltage / resistance3
print(f"Current through R3: {r3_current:.3f} A")

total_power = voltage * total_current
print(f"\nTotal power: {total_power:.3f} W")

# Tolerance for floating-point-precision error
tolerance = 1e-6

# Check if Kirchhoff's Voltage Law (KVL) is followed
voltage_error = voltage - r1_voltage - parallel_voltage
if abs(voltage_error) <= tolerance:
    print(f"\nKVL verification: PASSED")
else:
    print(f"\nKVL verification: FAILED")

# Check if Kirchhoff's Current Law (KCL) is followed
current_error = total_current - r2_current - r3_current
if abs(current_error) <= tolerance:
    print(f"\nKCL verification: PASSED")
else:
    print(f"\nKCL verification: FAILED")
