# Power Grid Simulator

A Python-based electrical circuit calculator that simulates basic resistor circuits and calculates important electrical values using Ohm's Law and Kirchhoff's Laws.

This project is designed to help me develop my Python programming skills while exploring electrical engineering concepts.

## Features

### 1. Series Circuit Calculator
- Accepts a source voltage and multiple resistor values.
- Calculates total resistance and current.
- Calculates the voltage drop across each resistor.
- Checks Kirchhoff's Voltage Law (KVL).

### 2. Parallel Circuit Calculator
- Accepts a source voltage and multiple resistor values.
- Calculates equivalent resistance.
- Calculates current through each resistor.
- Calculates total current and power.
- Checks Kirchhoff's Current Law (KCL).

### 3. Combined Circuit Calculator
- Calculates a circuit containing one resistor in series with two parallel resistors.
- Calculates total resistance, current, voltage drops, branch currents, and power.
- Checks KVL and KCL.

### 4. Dynamic Mixed Circuit Calculator
- Allows users to create circuits using multiple resistors.
- Allows components to be combined in series or parallel.
- Supports nested series-parallel circuit configurations.
- Uses recursion to calculate equivalent resistance.
- Automatically displays the equivalent resistance of the completed circuit.

## Project Structure

| File | Purpose |
|---|---|
| `utils.py` | Contains reusable input validation and circuit calculation functions. |
| `dynamic_series.py` | Calculates series circuits with a user-defined number of resistors. |
| `parallel.py` | Calculates parallel circuits with a user-defined number of resistors. |
| `combined.py` | Calculates a predefined combined series-parallel circuit. |
| `dynamic_combined.py` | Allows users to construct nested series-parallel circuits dynamically. |
| `test_circuits.py` | Contains unit tests for the circuit calculation functions. |

## Requirements

- Python 3.12 or newer.
- No external Python packages are required.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/roshnipai92100-creator/Power-Grid-Simulator.git
```

Navigate into the project directory:

```bash
cd Power-Grid-Simulator
```

Run a calculator:

```bash
python dynamic_series.py
```

Other available programs:

```bash
python parallel.py
python combined.py
python dynamic_combined.py
```

## Running Tests

The project uses Python's built-in `unittest` framework.

Run the test suite:

```bash
python -m unittest test_circuits.py -v
```

## Concepts Used

- Ohm's Law
- Series and parallel resistance
- Kirchhoff's Voltage Law (KVL)
- Kirchhoff's Current Law (KCL)
- Python functions and dictionaries
- Input validation and exception handling
- Recursion
- Unit testing

## Current Limitations

The dynamic mixed-circuit calculator currently calculates equivalent resistance. Calculating individual voltage drops, branch currents, and power throughout arbitrary nested circuits is a potential future improvement.

## Future Improvements

- Calculate voltage and current throughout dynamically constructed mixed circuits.
- Add power calculations for individual components.
- Expand circuit validation and testing.
- Explore more advanced electrical circuit configurations.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
