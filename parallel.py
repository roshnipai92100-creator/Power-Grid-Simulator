# Import from utils.py
from utils import get_valid_number, calculate_parallel

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
        equivalent_resistance, total_current, total_power, resistor_currents, kcl_law = calculate_parallel(voltage, resistances)

        print(f"\nEquivalent resistance: {equivalent_resistance:.3f} Ω\n")

        for index, resistor_current in enumerate(resistor_currents, start=1):
            print(f"Current through R{index}: {resistor_current:.3f} A")

        print(f"\nTotal current: {total_current:.3f} A")
        print(f"Total power: {total_power:.3f} W")

        print(f"\nKCL verification: {kcl_law}")
    except ValueError as error:
        print(error)

if __name__ == '__main__':
    main()