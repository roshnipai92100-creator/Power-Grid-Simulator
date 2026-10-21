# Import get_valid_number from utils.py
from utils import get_valid_number

# Get source voltage and two resistances
voltage = get_valid_number("Enter source voltage (just the #): ")
resistance1 = get_valid_number("Enter resistance 1 (just the #): ", positive_only=True)
resistance2 = get_valid_number("Enter resistance 2 (just the #): ", positive_only=True)

# Calculations + Outputs (print statements)
total_resistance = resistance1 + resistance2
print(f"\nTotal resistance: {total_resistance:.3f} Ω")

current = voltage / total_resistance
print(f"Current: {current:.3f} A")

power = voltage * current
print(f"Power: {power:.3f} W")

voltage_drop1 = current * resistance1
print(f"\nVoltage drop 1: {voltage_drop1:.3f} V")
voltage_drop2 = current * resistance2
print(f"Voltage drop 2: {voltage_drop2:.3f} V")

total_voltage_drop = voltage_drop1 + voltage_drop2
print(f"Total voltage drop: {total_voltage_drop:.3f} V")

# Tolerance for floating-point-precision error
tolerance = 1e-6
# Check if Kirchhoff's Voltage Law (KVL) is followed
voltage_error = voltage - voltage_drop1 - voltage_drop2
if abs(voltage_error) <= tolerance:
    print(f"\nKVL verification: PASSED")
else:
    print(f"\nKVL verification: FAILED")