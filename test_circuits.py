# Import unittest to test circuit calculators
import unittest
# Import from utils.py
from utils import calculate_series, calculate_parallel, calculate_combined

# Test series circuit calculator
class TestSeries(unittest.TestCase):
    # Test calculate_series from utils
    def test_series(self) -> None:
        voltage = 12
        resistances = [1,2,3]

        total_resistance, total_current, voltage_drops, total_voltage_drop, kvl_law = calculate_series(voltage, resistances)

        self.assertAlmostEqual(total_resistance, 6)
        self.assertAlmostEqual(total_current, 2)
        self.assertEqual(voltage_drops, [2, 4, 6])
        self.assertAlmostEqual(total_voltage_drop, 12)
        self.assertEqual(kvl_law, "PASSED")

    # Test if ValueError is raised when empty list is passed for resistances
    def test_series_empty_list(self) -> None:
        with self.assertRaises(ValueError):
            calculate_series(24, [])

    # Test if ValueError is raised when NaN or inf is passed as voltage
    def test_series_invalid_voltage(self) -> None:
        with self.assertRaises(ValueError):
            calculate_series(float("nan"), [2,4,6])
        with self.assertRaises(ValueError):
            calculate_series(float("inf"), [1,2,3])

    # Test if ValueError is raised when a non-positive number, NaN, or inf is passed as a resistance
    def test_series_invalid_resistance(self) -> None:
        with self.assertRaises(ValueError):
            calculate_series(18, [2,0,4])
        with self.assertRaises(ValueError):
            calculate_series(16, [2,4,float("nan")])
        with self.assertRaises(ValueError):
            calculate_series(11, [8,float("inf"),5])

    # Test if calculations are correct for a voltage of 0 V
    def test_series_zero_voltage(self) -> None:
        voltage = 0
        resistances = [2,4,6]

        total_resistance, total_current, voltage_drops, total_voltage_drop, kvl_law = calculate_series(voltage, resistances)

        self.assertAlmostEqual(total_resistance, 12)
        self.assertAlmostEqual(total_current, 0)
        self.assertEqual(voltage_drops, [0,0,0])
        self.assertAlmostEqual(total_voltage_drop, 0)
        self.assertEqual(kvl_law, "PASSED")

# Test parallel circuit calculator
class TestParallel(unittest.TestCase):
    # Test calculate_parallel from utils
    def test_parallel(self) -> None:
        voltage = 12
        resistances = [2,3,4]

        equivalent_resistance, total_current, total_power, resistor_currents, kcl_law = calculate_parallel(voltage, resistances)

        self.assertAlmostEqual(equivalent_resistance, 12/13)
        self.assertAlmostEqual(total_current, 13)
        self.assertAlmostEqual(total_power, 156)
        self.assertAlmostEqual(resistor_currents[0], 6)
        self.assertAlmostEqual(resistor_currents[1], 4)
        self.assertAlmostEqual(resistor_currents[2], 3)
        self.assertEqual(kcl_law, "PASSED")

    # Test if ValueError is raised when empty list is passed for resistances
    def test_parallel_empty_list(self) -> None:
        with self.assertRaises(ValueError):
            calculate_parallel(12, [])

    # Test if ValueError is raised when NaN or inf is passed as voltage
    def test_parallel_invalid_voltage(self) -> None:
        with self.assertRaises(ValueError):
            calculate_parallel(float("nan"), [9,5,1])
        with self.assertRaises(ValueError):
            calculate_parallel(float("inf"), [2,5,2])

    # Test if ValueError is raised when a non-positive number, NaN, or inf is passed as a resistance
    def test_parallel_invalid_resistance(self) -> None:
        with self.assertRaises(ValueError):
            calculate_parallel(15, [6, -3, 2])
        with self.assertRaises(ValueError):
            calculate_parallel(19, [float("nan"),9,3])
        with self.assertRaises(ValueError):
            calculate_parallel(14, [1,3,float("inf")])

    # Test if calculations are correct for a voltage of 0 V
    def test_parallel_zero_voltage(self) -> None:
        voltage = 0
        resistances = [4,6,3]

        equivalent_resistance, total_current, total_power, resistor_currents, kcl_law = calculate_parallel(voltage, resistances)

        self.assertAlmostEqual(equivalent_resistance, 4/3)
        self.assertAlmostEqual(total_current, 0)
        self.assertAlmostEqual(total_power, 0)
        self.assertEqual(resistor_currents, [0,0,0])
        self.assertEqual(kcl_law, "PASSED")

# Test combined circuit calculator
class TestCombined(unittest.TestCase):
    # Test calculate_combined from utils
    def test_combined(self) -> None:
        voltage = 12
        resistance1 = 4
        resistance2 = 6
        resistance3 = 3

        parallel_resistance, total_resistance, total_current, r1_voltage, parallel_voltage, r2_current, r3_current, total_power, kvl_law, kcl_law = calculate_combined(voltage, resistance1, resistance2, resistance3)

        self.assertAlmostEqual(parallel_resistance, 2)
        self.assertAlmostEqual(total_resistance, 6)
        self.assertAlmostEqual(total_current, 2)
        self.assertAlmostEqual(r1_voltage, 8)
        self.assertAlmostEqual(parallel_voltage, 4)
        self.assertAlmostEqual(r2_current, 2/3)
        self.assertAlmostEqual(r3_current, 4/3)
        self.assertAlmostEqual(total_power, 24)
        self.assertEqual(kvl_law, "PASSED")
        self.assertEqual(kcl_law, "PASSED")

    # Test if ValueError is raised when NaN or inf is passed as voltage
    def test_combined_invalid_voltage(self) -> None:
        with self.assertRaises(ValueError):
            calculate_combined(float("nan"), 6, 2, 9)
        with self.assertRaises(ValueError):
            calculate_combined(float("inf"), 7, 3, 5)

    # Test if ValueError is raised when a non-positive number, NaN, or inf is passed as a resistance
    def test_combined_invalid_resistance(self) -> None:
        with self.assertRaises(ValueError):
            calculate_combined(24, 4, 0, 3)
        with self.assertRaises(ValueError):
            calculate_combined(21, 7, float("nan"), 4)
        with self.assertRaises(ValueError):
            calculate_combined(23, float("inf"), 6, 3)

    # Test if calculations are correct for a voltage of 0 V
    def test_combined_zero_voltage(self) -> None:
        voltage = 0
        resistance1 = 4
        resistance2 = 6
        resistance3 = 3

        parallel_resistance, total_resistance, total_current, r1_voltage, parallel_voltage, r2_current, r3_current, total_power, kvl_law, kcl_law = calculate_combined(voltage, resistance1, resistance2, resistance3)

        self.assertAlmostEqual(parallel_resistance, 2)
        self.assertAlmostEqual(total_resistance, 6)
        self.assertAlmostEqual(total_current, 0)
        self.assertAlmostEqual(r1_voltage, 0)
        self.assertAlmostEqual(parallel_voltage, 0)
        self.assertAlmostEqual(r2_current, 0)
        self.assertAlmostEqual(r3_current, 0)
        self.assertAlmostEqual(total_power, 0)
        self.assertEqual(kvl_law, "PASSED")
        self.assertEqual(kcl_law, "PASSED")