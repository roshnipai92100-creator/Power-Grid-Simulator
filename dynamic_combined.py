# Import util functions
from utils import calculate_resistance, get_valid_number, calculate_circuit, check_kvl, check_kcl, check_power_conservation

type Circuit = str | tuple[str | Circuit, ...]
measurement_units = {
    "voltage": 'V',
    "current": 'A',
    "power": 'W'
}

def get_component_selections(components: dict[str, Circuit], resistors: dict[str, float | int]) -> list[tuple[str, Circuit]]:
    selected_components = []
    component_list = list(components.items())

    while len(selected_components) < 2:
        print()
        for i, (name, circuit) in enumerate(component_list):
            resistance = calculate_resistance(circuit, resistors)
            print(f"{i + 1}. {name} ({resistance:.3f} Ω)")
        print()

        if not selected_components:
            resistor_choice = get_valid_number("Enter the 1st component: ", positive_only=True, int_only=True)
        else:
            resistor_choice = get_valid_number("Enter the 2nd component: ", positive_only=True, int_only=True)

        if resistor_choice > len(component_list):
            print("\nChoose a valid component number")
            continue
        elif component_list[resistor_choice - 1] in selected_components:
            print("\nComponent already chosen")
            continue
        selected_components.append(component_list[resistor_choice - 1])

    return selected_components

def combine_components(components: dict[str, Circuit], selected_components: list[tuple[str, Circuit]], group_number: int) -> None:
    while True:
        connection_type = input("\nEnter connection type (series or parallel, s/p for short): ").strip().lower()
        if connection_type == 's':
            connection_type = "series"
        elif connection_type == 'p':
            connection_type = "parallel"
        if connection_type != "series" and connection_type != "parallel":
            print("\nPlease enter a valid connection type")
            print("Options: series, parallel")
            continue
        break

    new_circuit = (connection_type, selected_components[0][1], selected_components[1][1])
    components.pop(selected_components[0][0])
    components.pop(selected_components[1][0])

    group_name = f"Group {group_number}"

    components[group_name] = new_circuit

def main():
    # Get source voltage and create dictionary for resistors and their resistance
    voltage = get_valid_number("Enter source voltage: ")
    resistors = dict()

    # Create components dictionary to store groups and the resistors in them
    components = dict()

    # Get the number of resistors
    number_of_resistors = get_valid_number("Enter number of resistors: ", positive_only=True, int_only=True)

    # Loop once for each resistor
    for i in range(number_of_resistors):
        # Run until valid input
        while True:
            resistor_name = input("\nEnter resistance name: ").strip()
            if resistor_name in resistors:
                print("\nResistance name already taken")
                continue
            elif resistor_name == "":
                print("\nResistance name cannot be empty")
                continue
            elif len(resistor_name) > 12:
                print("\nResistance name cannot be longer than 12 characters")
                continue
            elif resistor_name == "series" or resistor_name == "parallel":
                print("\nResistance name cannot be series or parallel")
                continue
            elif "group" in resistor_name.lower():
                print("\nResistance name cannot include group as it is used in systemic naming and will be confusing")
                continue
            elif resistor_name.isnumeric():
                print("\nResistance name cannot be just a number (must include letters/symbols)")
                continue

            resistor_value = get_valid_number(f"Enter resistance of {resistor_name}: ", positive_only=True)
            resistors[resistor_name] = resistor_value
            components[resistor_name] = resistor_name
            break

    group_number = 1

    while len(components) > 1:
        selected_components = get_component_selections(components, resistors)
        combine_components(components, selected_components, group_number)

        group_number += 1

    equivalent_resistance = calculate_resistance(next(iter(components.values())), resistors)
    print(f"\nEquivalent Resistance: {equivalent_resistance:.3f} Ω")


    circuit = next(iter(components.values()))

    resistor_results, total_current, total_voltage_drop, total_current_change = calculate_circuit(circuit, voltage, resistors)

    print("----------------------------------------------")
    print("Resistor     Voltage     Current     Power")
    print("----------------------------------------------")
    for resistor_name, measurements in resistor_results.items():
        print(f"{resistor_name:<13}", end='')
        for measurement, value in measurements.items():
            print(f"{value:.2f} {measurement_units[measurement]}      ", end='')
        print()
    print("----------------------------------------------")

    total_power = sum(resistor_results[resistor_name]["power"] for resistor_name in resistor_results)
    source_power = voltage * total_current

    kvl_law = check_kvl(voltage, total_voltage_drop)
    kcl_law = check_kcl(total_current, total_current_change)
    power_conservation = check_power_conservation(total_power, source_power)

    current_change_display = f"{"N/A" if total_current_change is None else f"{total_current_change:.3f}"}"
    current_change_unit = "A" if total_current_change is not None else ""

    voltage_drop_display = f"{"N/A" if total_voltage_drop is None else f"{total_voltage_drop:.3f}"}"
    voltage_drop_unit = "V" if total_voltage_drop is not None else ""

    print(f"\nTotal Current: {total_current:.3f} A")
    print(f"Total Current Change: {current_change_display} {current_change_unit}")
    print(f"Total Voltage Drop: {voltage_drop_display} {voltage_drop_unit}")
    print(f"\nKVL Law: {kvl_law}")
    print(f"KCL Law: {kcl_law}")
    print(f"Conservation of Power: {power_conservation}")

if __name__ == "__main__":
    main()