# Power Grid Simulator

A Python-based electrical circuit calculator and simulator. This project was created to explore electrical engineering concepts through programming, starting with basic DC circuit calculations and gradually expanding toward more advanced electrical systems.

## Features

### Series Circuits
- Calculate total resistance.
- Calculate total current using Ohm's Law.
- Calculate voltage drops across individual resistors.
- Verify Kirchhoff's Voltage Law (KVL).
- Supports multiple resistors.

### Parallel Circuits
- Calculate equivalent resistance.
- Calculate current through each branch.
- Calculate total current and power.
- Verify Kirchhoff's Current Law (KCL).
- Supports multiple resistors.

### Combined Circuits
- Calculate circuits containing a series resistor and a parallel section.
- Calculate total resistance and current.
- Calculate individual voltage drops and branch currents.
- Calculate total power.
- Verify both KVL and KCL.

### Input Validation
- Rejects invalid numerical input.
- Checks for negative or zero resistance.
- Rejects NaN and infinite values.
- Supports integer-only input when needed.

### Automated Testing
- Uses Python's built-in `unittest` framework.
- Tests series, parallel, and combined circuit calculations.
- Includes tests for invalid inputs and zero-voltage circuits.

## Project Structure

| File | Purpose |
|---|---|
| `utils.py` | Contains reusable input validation and circuit calculation functions. |
| `series.py` | Runs the series circuit calculator. |
| `parallel.py` | Runs the parallel circuit calculator. |
| `combined.py` | Runs the combined circuit calculator. |
| `test_circuits.py` | Contains automated tests for circuit calculations. |

## Requirements

- Python 3.10 or newer
- No external Python packages required.

## How to Run

Clone the repository:

```bash
git clone https://github.com/roshnipai92100-creator/Power-Grid-Simulator.git
```

Navigate into the project folder:

```bash
cd Power-Grid-Simulator
```

Run any calculator:

```bash
python series.py
python parallel.py
python combined.py
```

Run the automated tests:

```bash
python -m unittest test_circuits.py -v
```

## Electrical Concepts

This project uses several fundamental electrical engineering principles:

- **Ohm's Law:** \(V = IR\)
- **Electrical Power:** \(P = VI\)
- **Series Resistance:** RT = R1 + R2 + ... + Rn
- **Parallel Resistance:** 1/RT = 1/R1 + 1/R2 + ... + 1/Rn
- **Kirchhoff's Voltage Law (KVL):** The sum of voltage changes around a closed loop is zero.
- **Kirchhoff's Current Law (KCL):** The total current entering a junction equals the total current leaving it.

## Current Limitations

- The combined circuit calculator currently supports one resistor in series with two resistors in parallel.
- The application runs through the command line.
- AC circuit calculations are not currently supported.

## Future Plans

- Support for more flexible mixed circuits.
- Alternating Current (AC) circuit calculations.
- More advanced electrical engineering calculations.
- Eventually expand toward power-grid simulation.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
