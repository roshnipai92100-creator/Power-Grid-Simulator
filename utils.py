import math

type Circuit = str | tuple[str | Circuit, ...]

# Get valid input function
def get_valid_number(prompt: str, positive_only: bool = False, int_only: bool = False) -> float | int:
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
            elif int_only and not number.is_integer():
                print("\nPlease enter an integer")
                print("Try again\n")
                continue

        # If conversion fails, warn user and run loop again
        except ValueError:
            print("\nPlease enter a valid number")
            print("Try again\n")
        # Break out of loop if input is valid
        else:
            return int(number) if int_only else number

# Calculation function for series circuits
def calculate_series(voltage: float | int, resistances: list[float | int]) -> tuple[float | int, float | int, list[float | int], float | int, str]:
    # Check if resistances list is empty and stop if it is
    if not resistances:
        raise ValueError("\nResistances list cannot be empty")

    # Check if any non-positive resistances exist and stop if one is found
    if any(resistance <= 0 or not math.isfinite(resistance) for resistance in resistances):
        raise ValueError("\nAll resistances must be valid, positive numbers")

    # Check if voltage is valid and stop if not
    if not math.isfinite(voltage):
        raise ValueError("\nVoltage must be a valid number")

    # Calculations
    total_resistance = sum(resistances)
    total_current = voltage / total_resistance

    # Voltage drop calculations
    voltage_drops = []
    for resistance in resistances:
        voltage_drop = total_current * resistance
        voltage_drops.append(voltage_drop)

    total_voltage_drop = sum(voltage_drops)

    # Tolerance for floating-point-precision error
    tolerance = 1e-6

    # Check if Kirchhoff's Voltage Law (KVL) is followed
    voltage_error = voltage - total_voltage_drop
    if abs(voltage_error) <= tolerance:
        kvl_law = "PASSED"
    else:
        kvl_law = "FAILED"

    # Return all calculations
    return total_resistance, total_current, voltage_drops, total_voltage_drop, kvl_law

# Calculation functions for parallel circuits
def calculate_parallel(voltage: float | int, resistances: list[float | int]) -> tuple[float | int, float | int, float | int, list[float | int], str]:
    # Check if resistances list is empty and stop if it is
    if not resistances:
        raise ValueError("\nResistances list cannot be empty")

    # Check if any non-positive resistances exist and stop if one is found
    if any(resistance <= 0 or not math.isfinite(resistance) for resistance in resistances):
        raise ValueError("\nAll resistances must be valid, positive numbers")

    # Check if voltage is valid and stop if not
    if not math.isfinite(voltage):
        raise ValueError("\nVoltage must be a valid number")

    # Make empty list for current through each resistor
    resistor_currents = []

    for resistance in resistances:
        resistor_current = voltage / resistance
        resistor_currents.append(resistor_current)

    # Calculate equivalent resistance, total current, and total power
    equivalent_resistance = 1 / sum(1 / resistance for resistance in resistances)
    total_current = voltage / equivalent_resistance
    total_power = voltage * total_current

    # Tolerance for floating-point-precision error
    tolerance = 1e-6
    # Check if Kirchhoff's Current Law (KCL) is followed
    current_error = total_current - sum(resistor_currents)
    if abs(current_error) <= tolerance:
        kcl_law = "PASSED"
    else:
        kcl_law = "FAILED"

    # Return all calculations
    return equivalent_resistance, total_current, total_power, resistor_currents, kcl_law

# Calculation functions for combined circuits
def calculate_combined(voltage: float | int, resistance1: float | int, resistance2: float | int, resistance3: float | int) -> tuple[float | int, float | int, float | int, float | int, float | int, float | int, float | int, float | int, str, str]:
    # Check if any non-positive resistances exist and stop if one is found
    if any(resistance <= 0 or not math.isfinite(resistance) for resistance in [resistance1, resistance2, resistance3]):
        raise ValueError("\nAll resistances must be valid, positive numbers")

    # Check if voltage is valid and stop if not
    if not math.isfinite(voltage):
        raise ValueError("\nVoltage must be a valid number")

    # Calculations
    parallel_resistance = resistance2 * resistance3 / (resistance2 + resistance3)
    total_resistance = resistance1 + parallel_resistance
    total_current = voltage / total_resistance
    r1_voltage = total_current * resistance1
    parallel_voltage = total_current * parallel_resistance
    r2_current = parallel_voltage / resistance2
    r3_current = parallel_voltage / resistance3
    total_power = voltage * total_current

    # Tolerance for floating-point-precision error
    tolerance = 1e-6

    # Check if Kirchhoff's Voltage Law (KVL) is followed
    voltage_error = voltage - r1_voltage - parallel_voltage
    if abs(voltage_error) <= tolerance:
        kvl_law = "PASSED"
    else:
        kvl_law = "FAILED"

    # Check if Kirchhoff's Current Law (KCL) is followed
    current_error = total_current - r2_current - r3_current
    if abs(current_error) <= tolerance:
        kcl_law = "PASSED"
    else:
        kcl_law = "FAILED"

    # Return all calculations
    return parallel_resistance, total_resistance, total_current, r1_voltage, parallel_voltage, r2_current, r3_current, total_power, kvl_law, kcl_law

# Recursive calculation function for dynamic mixed circuits
def calculate_resistance(circuit: Circuit, resistors: dict[str, float | int]) -> float | int:
    if isinstance(circuit, str):
        # Check if resistor exists
        if circuit not in resistors:
            raise KeyError("\nResistor does not exist. Check circuit and resistor names")

        resistance = resistors[circuit]

        # Check if resistance is valid
        if resistance <= 0:
            raise ValueError("\nResistance must be a positive number")

        if not math.isfinite(resistance):
            raise ValueError("\nResistance must be a valid, positive number")

        return resistance
    else:
        # Check if circuit has resistors
        if len(circuit) < 3:
            raise ValueError("\nNot enough resistors in circuit")

        # Check if circuit connection type is valid
        if circuit[0] != "series" and circuit[0] != "parallel":
            raise ValueError("\nConnection type must be series or parallel")

        equivalent_resistances = []
        for resistor in circuit[1:]:
            resistance = calculate_resistance(resistor, resistors)
            equivalent_resistances.append(resistance)

        if circuit[0] == "series":
            return sum(equivalent_resistances)
        else:
            equivalent_resistance = 1 / sum(1 / resistance for resistance in equivalent_resistances)
            return equivalent_resistance

# Calculation function for the power of a single resistor
def calculate_power(voltage: float | int, resistance: float | int) -> float | int:
    # Validate voltage and resistance
    if not math.isfinite(voltage):
        raise ValueError("\nVoltage must be a valid number")
    if not math.isfinite(resistance):
        raise ValueError("\nResistance must be a valid, positive number")
    if resistance <= 0:
        raise ValueError("\nResistance must be a positive number")

    # Calculate and return power
    power = (voltage ** 2) / resistance
    return power

# Runs calculations off of calculate_resistance
def calculate_circuit(circuit: Circuit, voltage: float | int,  resistors: dict[str, float | int]) -> tuple[dict[str, dict[str, float | int]], float | int, float | int | None, float | int | None]:
    total_resistance = calculate_resistance(circuit, resistors)
    total_current = voltage / total_resistance

    # KVL and KCL Law Variables
    total_voltage_drop = 0
    total_current_change = 0

    resistor_results = dict()
    if isinstance(circuit, str):
        power = calculate_power(voltage, total_resistance)
        resistor_results[circuit] = dict()
        resistor_results[circuit]["voltage"] = voltage
        resistor_results[circuit]["current"] = total_current
        resistor_results[circuit]["power"] = power

        # If the circuit is a single resistor, there isn't any changes in voltage/current
        total_voltage_drop = None
        total_current_change = None

        return resistor_results, total_current, total_voltage_drop, total_current_change
    else:
        if circuit[0] == "series":
            total_current_change = None

            for resistor in circuit[1:]:
                equivalent_resistance = calculate_resistance(resistor, resistors)
                voltage = total_current * equivalent_resistance

                result, *_, child_current_change = calculate_circuit(resistor, voltage, resistors)

                if child_current_change is not None:
                    total_current_change = child_current_change

                resistor_results.update(result)

                total_voltage_drop += voltage

            return resistor_results, total_current, total_voltage_drop, total_current_change
        else:
            total_voltage_drop = None

            for resistor in circuit[1:]:
                result, child_current, child_voltage_drop,_ = calculate_circuit(resistor, voltage, resistors)

                resistor_results.update(result)

                if child_voltage_drop is not None:
                    total_voltage_drop = child_voltage_drop

                if child_current is not None:
                    total_current_change += child_current

            return resistor_results, total_current, total_voltage_drop, total_current_change

# Function to check KVL law
def check_kvl(voltage: float | int, total_voltage_drop: float | int | None, tolerance: float = 1e-6) -> str:
    # Check if Kirchhoff's Voltage Law (KVL) is followed
    if total_voltage_drop is None:
        kvl_law = "N/A"
    else:
        voltage_error = voltage - total_voltage_drop
        if abs(voltage_error) <= tolerance:
            kvl_law = "PASSED"
        else:
            kvl_law = "FAILED"

    return kvl_law


# Function to check KCL law
def check_kcl(total_current: float | int, total_current_change: float | int | None, tolerance: float = 1e-6) -> str:
    # Check if Kirchhoff's Current Law (KCL) is followed
    if total_current_change is None:
        kcl_law = "N/A"
    else:
        current_error = total_current - total_current_change
        if abs(current_error) <= tolerance:
            kcl_law = "PASSED"
        else:
            kcl_law = "FAILED"

    return kcl_law

# Function to check power conservation
def check_power_conservation(total_power: float | int, source_power: float | int, tolerance: float = 1e-6) -> str:
    if abs(total_power - source_power) <= tolerance:
        power_conservation = "PASSED"
    else:
        power_conservation = "FAILED"

    return power_conservation
