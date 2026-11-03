# Import from utils.py
from utils import get_valid_number, calculate_combined

def main() -> None:
    # Get source voltage and three resistances
    voltage = get_valid_number("Enter source voltage: ")
    resistance1 = get_valid_number("Enter resistance 1: ", positive_only=True)
    resistance2 = get_valid_number("Enter resistance 2: ", positive_only=True)
    resistance3 = get_valid_number("Enter resistance 3: ", positive_only=True)

    # Calculations
    parallel_resistance, total_resistance, total_current, r1_voltage, parallel_voltage, r2_current, r3_current, total_power, kvl_law, kcl_law = calculate_combined(voltage, resistance1, resistance2, resistance3)

    # Outputs (print statements)
    print(f"\nParallel resistance: {parallel_resistance:.3f} Ω")
    print(f"Total resistance: {total_resistance:.3f} Ω")
    print(f"Total current: {total_current:.3f} A")
    print(f"\nVoltage across R1: {r1_voltage:.3f} V")
    print(f"Voltage across parallel section: {parallel_voltage:.3f} V")
    print(f"\nCurrent through R2: {r2_current:.3f} A")
    print(f"Current through R3: {r3_current:.3f} A")
    print(f"\nTotal power: {total_power:.3f} W")
    print(f"\nKVL verification: {kvl_law}")
    print(f"\nKCL verification: {kcl_law}")

if __name__ == '__main__':
    main()