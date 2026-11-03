# Import from utils.py
from utils import get_valid_number, calculate_series

def main() -> None:
    # Get source voltage and resistances
    voltage = get_valid_number("Enter source voltage: ")
    resistances = []

    # Get the number of resistors
    number_of_resistors = get_valid_number("Enter number of resistors: ", positive_only=True, int_only=True)

    for i in range(number_of_resistors):
        resistances.append(get_valid_number(f"Enter resistance {i + 1}: ", positive_only=True))

    # Calculations + Outputs (print statements)
    try:
        total_resistance, total_current, voltage_drops, total_voltage_drop, kvl_law = calculate_series(voltage, resistances)

        print(f"\nTotal resistance: {total_resistance:.3f} Ω")
        print(f"Total current: {total_current:.3f} A\n")

        for index, voltage_drop in enumerate(voltage_drops, start=1):
            print(f"Voltage drop of R{index}: {voltage_drop:.3f} V")

        print(f"\nTotal voltage drop: {total_voltage_drop:.3f} V")

        print(f"\nKVL verification: {kvl_law}")
    except ValueError as error:
        print(error)

if __name__ == '__main__':
    main()