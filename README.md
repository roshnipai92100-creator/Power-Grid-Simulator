# Power Grid Simulator

A Python-based electrical circuit calculator and simulator. This project started with basic series and parallel resistor calculations and has expanded to support dynamic, nested circuits and DC circuit analysis.

## Features

### Circuit Calculations
- Calculate equivalent resistance in series circuits.
- Calculate equivalent resistance in parallel circuits.
- Calculate equivalent resistance in nested series-parallel circuits.
- Support dynamically entered resistor quantities and resistance values.

### DC Circuit Analysis
- Calculate total circuit resistance.
- Calculate total circuit current.
- Calculate voltage across individual resistors.
- Calculate current through individual resistors.
- Calculate power used by individual resistors.
- Verify Kirchhoff's Voltage Law (KVL).
- Verify Kirchhoff's Current Law (KCL).
- Verify power conservation.

### Input Validation
- Check that resistance values are positive.
- Reject invalid numerical inputs.
- Prevent duplicate or invalid resistor names.
- Handle invalid circuit configurations.

### Testing
- Includes automated unit tests using Python's `unittest` framework.
- Tests calculation functions, input validation, and circuit law verification.

## Requirements

- Python 3.12 or newer.

## Project Structure

| File | Description |
|---|---|
| `series.py` | Series circuit calculator |
| `dynamic_series.py` | Dynamic series circuit calculator |
| `parallel.py` | Parallel circuit calculator |
| `combined.py` | Fixed mixed circuit calculator |
| `dynamic_combined.py` | Dynamic nested series-parallel circuit calculator |
| `utils.py` | Reusable calculation and validation functions |
| `test_circuits.py` | Automated unit tests |

## How to Run

1. Clone or download the repository.
2. Open the project in your Python IDE.
3. Run the Python script for the circuit you want to calculate.
4. Follow the prompts to enter voltage, resistor quantities, and resistance values.

For dynamic mixed circuits, you can combine components into series or parallel groups until the entire circuit is connected.

## Running Tests

Run the following command from the project directory:

```bash
python -m unittest test_circuits.py -v
```

This runs the automated tests and displays the results.

## Concepts Used

This project uses several electrical engineering and programming concepts:

- Ohm's Law
- Series and parallel resistance
- Kirchhoff's Voltage Law
- Kirchhoff's Current Law
- Electrical power
- Recursive functions
- Dictionaries and tuples
- Input validation
- Unit testing

## Current Limitations

- The simulator currently focuses on DC circuits.
- Circuit components are limited to resistors.
- Capacitors, inductors, and AC analysis are not implemented yet.
- Circuit construction and results are handled through the console.

## Future Plans

- Introduce AC voltage and current calculations.
- Add RMS and peak voltage and current.
- Add frequency and period calculations.
- Introduce capacitors, inductors, and impedance.
- Expand into more advanced AC circuit analysis.
- Explore a graphical circuit interface.

## License

See [LICENSE](LICENSE) for license information.
