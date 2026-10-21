# Import get_valid_number from utils.py
from utils import get_valid_number, calculate_series

# Get source voltage and resistances
voltage = get_valid_number("Enter source voltage (just the #): ")
resistances = []

# Run until valid # of resistors is inputted
while True:
    # Get input
    number_of_resistors = get_valid_number("Enter number of resistors (just the #): ", positive_only=True)
    # Check if input is an integer and break if it is
    if number_of_resistors.is_integer():
        break
    # If input is not an integer, warn the user and run loop again
    else:
        print("\nPlease enter a positive integer")
        print("Try again\n")
        continue

for i in range(int(number_of_resistors)):
    resistances.append(get_valid_number(f"Enter resistance {i + 1} (just the #): ", positive_only=True))

# Calculations + Outputs (print statements)
try:
    total_resistance, total_current, voltage_drops, kvl_law = calculate_series(voltage, resistances)

    print(f"\nTotal resistance: {total_resistance:.3f} Ω")
    print(f"Total current: {total_current:.3f} A\n")

    for index, voltage_drop in enumerate(voltage_drops, start=1):
        print(f"Voltage across R{index}: {voltage_drop:.3f} V")

    print(f"\nKVL verification: {kvl_law}")
except ValueError as error:
    print(error)


