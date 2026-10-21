# Power Grid Simulator

## Overview
Power Grid Simulator is a Python-based electrical calculator/simulator that performs calculations for electrical circuits. The goal of this project is to start with basic electrical calculations and eventually build a simulator that can solve and visualize more complex circuits and power grids.

This project is currently in early development.

## Features

- Console/terminal-based inputs and outputs
- Input checking to filter out invalid inputs, such as non-positive resistances
- Calculate total resistance and current
- Calculate voltage drops across resistors in series circuits
- Verify Kirchhoff's Voltage Law (KVL) to make sure the voltage calculations are correct
- Display calculations with the correct units

## Requirements

- Python 3.10 or later
- No external packages required for the current implementation

## Installation

1. Download the source code by downloading the ZIP file from GitHub or cloning the repository.
2. Extract the ZIP file if you downloaded it.
3. Open the project folder in a code editor, such as PyCharm or VS Code.
4. Open the terminal in the project folder.

## Usage

Run the Python file for the calculator you want to use.

For example, to run the dynamic series circuit calculator, enter:

```bash
python dynamic_series.py
```

On macOS or Linux, you may need to use `python3` instead of `python`.

The program will ask for inputs such as source voltage, number of resistors, and resistance values. After the inputs are entered, it will return the corresponding electrical calculations.

Make sure `utils.py` is included in the project folder because it contains reusable functions used by the main program.

## Project Structure

- `dynamic_series.py` — Handles user inputs and displays the results for dynamic series circuits.
- `utils.py` — Contains reusable functions for input validation and electrical calculations.
- `series.py` — Handles user inputs and displays the results for series circuits (hardcoded # of resistors, unlike `dynamic_series.py`).
- `parallel.py` — Handles user inputs and displays the results for parallel circuits (hardcoded # of resistors, unlike `dynamic_series.py`).
- `combined.py` — Handles user inputs and displays the results for combined parallel + series circuits (hardcoded # of resistors, unlike `dynamic_series.py`).

## Current Limitations

- Calculations and inputs are currently handled through the console/terminal.
- Not all circuit types have dedicated calculation functions in `utils.py`.
- The tolerance used for verifying Kirchhoff's Voltage Law may need improvement for calculations with different numerical scales.
- A visual circuit builder and power-grid simulation have not been implemented yet.

## Future Plans

### Mixed-Circuit Solver
- Support series and parallel resistors.
- Solve combinations of series and parallel circuits.
- Calculate branch currents and power consumption.
- Verify Kirchhoff's Voltage Law (KVL) and Kirchhoff's Current Law (KCL).

### Visual Circuit Builder
- Place batteries and resistors on a canvas.
- Connect components with wires.
- Set component values by clicking them.
- Display calculated voltage and current directly on the circuit.

### Power-Grid Simulator
- Model generators, transmission lines, transformers, and loads.
- Calculate power losses and voltage drops.
- Simulate changing loads and component failures.
- Visualize how electricity flows through a network.

## License

See the [LICENSE](LICENSE) file for information about the license for this project.
