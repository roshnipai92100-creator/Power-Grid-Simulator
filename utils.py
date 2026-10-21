import math

# Get valid input function
def get_valid_number(prompt: str, positive_only: bool = False) -> float:
    # Run until valid input
    while True:
        # Try to convert user input (str) to float
        try:
            number = float(input(prompt))
            # Check if number is finite
            if not math.isfinite(number):
                print("\nPlease enter a valid number")
                print("Try again\n")
                continue
            # Check if input is negative and is supposed to be positive
            elif positive_only and number <= 0:
                print("\nPlease enter a positive number")
                print("Try again\n")
                continue

        # If conversion fails, warn user and run loop again
        except ValueError:
            print("\nPlease enter a valid number")
            print("Try again\n")
        # Break out of loop if input is valid
        else:
            return number

# Calculation function
def calculate_series(voltage: float | int, resistances: list[float | int]) -> tuple[float | int, float | int, list[float | int], str]:
    # Check if resistances list is empty and stop if it is
    if not resistances:
        raise ValueError("\nResistances list cannot be empty")

    # Calculations
    total_resistance = sum(resistances)
    total_current = voltage / total_resistance

    # Voltage drop calculations
    voltage_drops = []
    for resistance in resistances:
        voltage_drop = total_current * resistance
        voltage_drops.append(voltage_drop)

    # Tolerance for floating-point-precision error
    tolerance = 1e-6

    # Check if Kirchhoff's Voltage Law (KVL) is followed
    voltage_error = voltage - sum(voltage_drops)
    if abs(voltage_error) <= tolerance:
        kvl_law = "PASSED"
    else:
        kvl_law = "FAILED"

    # Return all calculations
    return total_resistance, total_current, voltage_drops, kvl_law