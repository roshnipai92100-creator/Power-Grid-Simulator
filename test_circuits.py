# Import unittest to test circuit calculators
import unittest
# Import utils.py
import utils

# Test series circuit calculator
class TestSeries(unittest.TestCase):
    # Test calculate_series from utils
    def test_series(self) -> None:
        voltage = 12
        resistances = [1,2,3]

        total_resistance, total_current, voltage_drops, total_voltage_drop, kvl_law = utils.calculate_series(voltage, resistances)

        self.assertAlmostEqual(total_resistance, 6)
        self.assertAlmostEqual(total_current, 2)
        self.assertEqual(voltage_drops, [2, 4, 6])
        self.assertAlmostEqual(total_voltage_drop, 12)
        self.assertEqual(kvl_law, "PASSED")

    # Test if ValueError is raised when empty list is passed for resistances
    def test_series_empty_list(self) -> None:
        with self.assertRaises(ValueError):
            utils.calculate_series(24, [])

    # Test if ValueError is raised when NaN or inf is passed as voltage
    def test_series_invalid_voltage(self) -> None:
        with self.assertRaises(ValueError):
            utils.calculate_series(float("nan"), [2,4,6])
        with self.assertRaises(ValueError):
            utils.calculate_series(float("inf"), [1,2,3])

    # Test if ValueError is raised when a non-positive number, NaN, or inf is passed as a resistance
    def test_series_invalid_resistance(self) -> None:
        with self.assertRaises(ValueError):
            utils.calculate_series(18, [2,0,4])
        with self.assertRaises(ValueError):
            utils.calculate_series(17, [6, -10, 8])
        with self.assertRaises(ValueError):
            utils.calculate_series(16, [3,4,float("nan")])
        with self.assertRaises(ValueError):
            utils.calculate_series(11, [8,float("inf"),5])

    # Test if calculations are correct for a voltage of 0 V
    def test_series_zero_voltage(self) -> None:
        voltage = 0
        resistances = [2,4,6]

        total_resistance, total_current, voltage_drops, total_voltage_drop, kvl_law = utils.calculate_series(voltage, resistances)

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

        equivalent_resistance, total_current, total_power, resistor_currents, kcl_law = utils.calculate_parallel(voltage, resistances)

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
            utils.calculate_parallel(12, [])

    # Test if ValueError is raised when NaN or inf is passed as voltage
    def test_parallel_invalid_voltage(self) -> None:
        with self.assertRaises(ValueError):
            utils.calculate_parallel(float("nan"), [9,5,1])
        with self.assertRaises(ValueError):
            utils.calculate_parallel(float("inf"), [2,5,2])

    # Test if ValueError is raised when a non-positive number, NaN, or inf is passed as a resistance
    def test_parallel_invalid_resistance(self) -> None:
        with self.assertRaises(ValueError):
            utils.calculate_parallel(13, [3, 0, 5])
        with self.assertRaises(ValueError):
            utils.calculate_parallel(15, [6, -3, 2])
        with self.assertRaises(ValueError):
            utils.calculate_parallel(19, [float("nan"),9,3])
        with self.assertRaises(ValueError):
            utils.calculate_parallel(14, [1,3,float("inf")])

    # Test if calculations are correct for a voltage of 0 V
    def test_parallel_zero_voltage(self) -> None:
        voltage = 0
        resistances = [4,6,3]

        equivalent_resistance, total_current, total_power, resistor_currents, kcl_law = utils.calculate_parallel(voltage, resistances)

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

        parallel_resistance, total_resistance, total_current, r1_voltage, parallel_voltage, r2_current, r3_current, total_power, kvl_law, kcl_law = utils.calculate_combined(voltage, resistance1, resistance2, resistance3)

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
            utils.calculate_combined(float("nan"), 6, 2, 9)
        with self.assertRaises(ValueError):
            utils.calculate_combined(float("inf"), 7, 3, 5)

    # Test if ValueError is raised when a non-positive number, NaN, or inf is passed as a resistance
    def test_combined_invalid_resistance(self) -> None:
        with self.assertRaises(ValueError):
            utils.calculate_combined(22, 12, -10, 11)
        with self.assertRaises(ValueError):
            utils.calculate_combined(24, 4, 0, 3)
        with self.assertRaises(ValueError):
            utils.calculate_combined(21, 7, float("nan"), 4)
        with self.assertRaises(ValueError):
            utils.calculate_combined(23, float("inf"), 6, 3)

    # Test if calculations are correct for a voltage of 0 V
    def test_combined_zero_voltage(self) -> None:
        voltage = 0
        resistance1 = 4
        resistance2 = 6
        resistance3 = 3

        parallel_resistance, total_resistance, total_current, r1_voltage, parallel_voltage, r2_current, r3_current, total_power, kvl_law, kcl_law = utils.calculate_combined(voltage, resistance1, resistance2, resistance3)

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

# Test dynamic_combined circuit calculator
class TestCalculateResistance(unittest.TestCase):
    # Test no-nest series circuit
    def test_calculate_resistance_series(self) -> None:
        resistors = {
            "R1": 10,
            "R2": 20,
            "R3": 30
        }
        circuit = ("series", "R1", "R2")
        resistance = utils.calculate_resistance(circuit, resistors)

        self.assertAlmostEqual(resistance, 30)

    # Test no-nest parallel circuit
    def test_calculate_resistance_parallel(self) -> None:
        resistors = {
            "R1": 10,
            "R2": 20,
            "R3": 30
        }
        circuit = ("parallel", "R1", "R2")
        resistance = utils.calculate_resistance(circuit, resistors)

        self.assertAlmostEqual(resistance, 20/3)

    # Test series inside parallel circuit
    def test_calculate_resistance_series_in_parallel(self) -> None:
        resistors = {
            "R1": 10,
            "R2": 20,
            "R3": 30
        }
        circuit = ("parallel", ("series", "R1", "R2"), "R3")
        resistance = utils.calculate_resistance(circuit, resistors)

        self.assertAlmostEqual(resistance, 15)

    # Test parallel inside series circuit
    def test_calculate_resistance_parallel_in_series(self) -> None:
        resistors = {
            "R1": 10,
            "R2": 20,
            "R3": 30
        }
        circuit = ("series", "R1", ("parallel", "R2", "R3"))
        resistance = utils.calculate_resistance(circuit, resistors)

        self.assertAlmostEqual(resistance, 22)

    # Test multi-nested circuit
    def test_calculate_resistance_multi_nested(self) -> None:
        resistors = {
            "R1": 10,
            "R2": 20,
            "R3": 30
        }
        circuit = ("series",
            "R1",
            ("parallel",
                "R2",
                ("series", "R3", "R1")
            )
        )
        resistance = utils.calculate_resistance(circuit, resistors)

        self.assertAlmostEqual(resistance, 70/3)

    # Test single resistor circuits
    def test_calculate_resistance_single_resistor(self) -> None:
        resistors = {
            "R1": 10
        }
        circuit = "R1"

        resistance = utils.calculate_resistance(circuit, resistors)

        self.assertAlmostEqual(resistance, 10)

    # Test a circuit with three resistors in parallel
    def test_calculate_resistance_three_parallel(self) -> None:
        resistors = {
            "R1": 10,
            "R2": 20,
            "R3": 30
        }
        circuit = ("parallel", "R1", "R2", "R3")
        resistance = utils.calculate_resistance(circuit, resistors)

        self.assertAlmostEqual(resistance, 60/11)

    # Test if ValueError is raised when resistance = NaN or inf
    def test_calculate_resistance_invalid_resistance(self) -> None:
        resistors = {
            "R1": float("nan"),
            "R2": float("inf"),
            "R3": 30,
            "R4": float("-inf"),
            "R5": 50
        }
        circuit1 = "R1"
        circuit2 = ("parallel", "R2", "R3")
        circuit3 = ("series", "R4", "R5")

        with self.assertRaises(ValueError):
            utils.calculate_resistance(circuit1, resistors)
        with self.assertRaises(ValueError):
            utils.calculate_resistance(circuit2, resistors)
        with self.assertRaises(ValueError):
            utils.calculate_resistance(circuit3, resistors)

    # Test if ValueError is raised when resistance = 0
    def test_calculate_resistance_zero_resistance(self) -> None:
        resistors = {
            "R1": 0
        }
        circuit = "R1"

        with self.assertRaises(ValueError):
            utils.calculate_resistance(circuit, resistors)

    # Test if ValueError is raised when resistance is negative
    def test_calculate_resistance_negative_resistance(self) -> None:
        resistors = {
            "R1": -10
        }
        circuit = "R1"

        with self.assertRaises(ValueError):
            utils.calculate_resistance(circuit, resistors)

    # Test if KeyError is raised when circuit contains an unknown resistor
    def test_calculate_resistance_unknown_resistor(self) -> None:
        resistors = {
            "R1": 10,
            "R2": 20,
            "R3": 30
        }
        circuit = "R4"

        with self.assertRaises(KeyError):
            utils.calculate_resistance(circuit, resistors)

    # Test if ValueError is raised when the circuit doesn't contain resistors
    def test_calculate_resistance_zero_resistors(self) -> None:
        resistors = {}
        circuit = ("series",)

        with self.assertRaises(ValueError):
            utils.calculate_resistance(circuit, resistors)

    # Test if ValueError is raised when the circuit has an invalid connection type
    def test_calculate_resistance_invalid_connection(self) -> None:
        resistors = {
            "R1": 10,
            "R2": 20,
            "R3": 30
        }
        circuit = ("mixed", "R1", "R2")

        with self.assertRaises(ValueError):
            utils.calculate_resistance(circuit, resistors)

# Test calculation function for the power of a single resistor
class TestCalculatePower(unittest.TestCase):
    # Test normal circumstances
    def test_calculate_power(self) -> None:
        voltage = 12
        resistance = 4

        power = utils.calculate_power(voltage, resistance)

        self.assertAlmostEqual(power, 36)

    # Test if ValueError is raised when resistance = NaN or inf
    def test_calculate_power_invalid_resistance(self) -> None:
        voltage = 12
        resistance1 = float("nan")
        resistance2 = float("inf")
        resistance3 = float("-inf")

        with self.assertRaises(ValueError):
            utils.calculate_power(voltage, resistance1)
        with self.assertRaises(ValueError):
            utils.calculate_power(voltage, resistance2)
        with self.assertRaises(ValueError):
            utils.calculate_power(voltage, resistance3)

    # Test if ValueError is raised when voltage = NaN or inf
    def test_calculate_power_invalid_voltage(self) -> None:
        voltage1 = float("nan")
        voltage2 = float("inf")
        voltage3 = float("-inf")
        resistance = 4

        with self.assertRaises(ValueError):
            utils.calculate_power(voltage1, resistance)
        with self.assertRaises(ValueError):
            utils.calculate_power(voltage2, resistance)
        with self.assertRaises(ValueError):
            utils.calculate_power(voltage3, resistance)

    # Test if ValueError is raised when resistance = 0
    def test_calculate_power_zero_resistance(self) -> None:
        voltage = 12
        resistance = 0

        with self.assertRaises(ValueError):
            utils.calculate_power(voltage, resistance)

    # Test if ValueError is raised when resistance is negative
    def test_calculate_power_negative_resistance(self) -> None:
        voltage = 12
        resistance = -4

        with self.assertRaises(ValueError):
            utils.calculate_power(voltage, resistance)

    # Test if results are the same when voltage is negative
    def test_calculate_power_negative_voltage(self) -> None:
        voltage = -12
        resistance = 4

        power = utils.calculate_power(voltage, resistance)

        self.assertAlmostEqual(power, 36)

# Test recursive calculate_circuit() function
class TestCalculateCircuit(unittest.TestCase):
    # Test single-resistor calculations
    def test_calculate_circuit_single_resistor(self) -> None:
        voltage = 12
        resistors = {
            "R1": 4
        }
        circuit = "R1"

        resistor_results, *_ = utils.calculate_circuit(circuit, voltage, resistors)

        self.assertAlmostEqual(resistor_results["R1"]["voltage"], 12)
        self.assertAlmostEqual(resistor_results["R1"]["current"], 3)
        self.assertAlmostEqual(resistor_results["R1"]["power"], 36)

    # Test series circuit calculations
    def test_calculate_circuit_series(self) -> None:
        voltage = 12
        resistors = {
            "R1": 2,
            "R2": 4
        }
        circuit = ("series", "R1", "R2")

        resistor_results, *_ = utils.calculate_circuit(circuit, voltage, resistors)

        self.assertAlmostEqual(resistor_results["R1"]["voltage"], 4)
        self.assertAlmostEqual(resistor_results["R1"]["current"], 2)
        self.assertAlmostEqual(resistor_results["R1"]["power"], 8)

        self.assertAlmostEqual(resistor_results["R2"]["voltage"], 8)
        self.assertAlmostEqual(resistor_results["R2"]["current"], 2)
        self.assertAlmostEqual(resistor_results["R2"]["power"], 16)

    # Test parallel circuit calculations
    def test_calculate_circuit_parallel(self) -> None:
        voltage = 12
        resistors = {
            "R1": 2,
            "R2": 4
        }
        circuit = ("parallel", "R1", "R2")

        resistor_results, *_ = utils.calculate_circuit(circuit, voltage, resistors)

        self.assertAlmostEqual(resistor_results["R1"]["voltage"], 12)
        self.assertAlmostEqual(resistor_results["R1"]["current"], 6)
        self.assertAlmostEqual(resistor_results["R1"]["power"], 72)

        self.assertAlmostEqual(resistor_results["R2"]["voltage"], 12)
        self.assertAlmostEqual(resistor_results["R2"]["current"], 3)
        self.assertAlmostEqual(resistor_results["R2"]["power"], 36)

    # Test nested mixed series-parallel circuit calculations
    def test_calculate_circuit_nested_series_parallel(self) -> None:
        voltage = 12
        resistors = {
            "R1": 2,
            "R2": 6,
            "R3": 3
        }
        circuit = ("series", "R1", ("parallel", "R2", "R3"))

        resistor_results, *_ = utils.calculate_circuit(circuit, voltage, resistors)

        self.assertAlmostEqual(resistor_results["R1"]["voltage"], 6)
        self.assertAlmostEqual(resistor_results["R1"]["current"], 3)
        self.assertAlmostEqual(resistor_results["R1"]["power"], 18)

        self.assertAlmostEqual(resistor_results["R2"]["voltage"], 6)
        self.assertAlmostEqual(resistor_results["R2"]["current"], 1)
        self.assertAlmostEqual(resistor_results["R2"]["power"], 6)

        self.assertAlmostEqual(resistor_results["R3"]["voltage"], 6)
        self.assertAlmostEqual(resistor_results["R3"]["current"], 2)
        self.assertAlmostEqual(resistor_results["R3"]["power"], 12)

    # Test nested mixed parallel-series circuit calculations
    def test_calculate_circuit_nested_parallel_series(self) -> None:
        voltage = 12
        resistors = {
            "R1": 2,
            "R2": 4,
            "R3": 4
        }
        circuit = ("parallel", ("series", "R1", "R2"), "R3")

        resistor_results, *_ = utils.calculate_circuit(circuit, voltage, resistors)

        self.assertAlmostEqual(resistor_results["R1"]["voltage"], 4)
        self.assertAlmostEqual(resistor_results["R1"]["current"], 2)
        self.assertAlmostEqual(resistor_results["R1"]["power"], 8)

        self.assertAlmostEqual(resistor_results["R2"]["voltage"], 8)
        self.assertAlmostEqual(resistor_results["R2"]["current"], 2)
        self.assertAlmostEqual(resistor_results["R2"]["power"], 16)

        self.assertAlmostEqual(resistor_results["R3"]["voltage"], 12)
        self.assertAlmostEqual(resistor_results["R3"]["current"], 3)
        self.assertAlmostEqual(resistor_results["R3"]["power"], 36)

# Test if circuit laws are followed
class TestCircuitLaws(unittest.TestCase):
    # Check if KVL passes with correct values
    def test_circuit_laws_kvl_correct_voltage_drops(self) -> None:
        voltage = 12
        total_voltage_drop = 12

        kvl_law = utils.check_kvl(voltage, total_voltage_drop)

        self.assertEqual(kvl_law, "PASSED")

    # Check if KVL fails with incorrect values
    def test_circuit_laws_kvl_incorrect_voltage_drops(self) -> None:
        voltage = 12
        total_voltage_drop = 10

        kvl_law = utils.check_kvl(voltage, total_voltage_drop)

        self.assertEqual(kvl_law, "FAILED")

    # Check if KVL passes with precision error within tolerance
    def test_circuit_laws_kvl_within_tolerance(self) -> None:
        voltage = 12
        total_voltage_drop = 12.0000005
        tolerance = 1e-6

        kvl_law = utils.check_kvl(voltage, total_voltage_drop, tolerance)

        self.assertEqual(kvl_law, "PASSED")

    # Check if KVL fails with precision error outside tolerance
    def test_circuit_laws_kvl_outside_tolerance(self) -> None:
        voltage = 12
        total_voltage_drop = 12.000002
        tolerance = 1e-6

        kvl_law = utils.check_kvl(voltage, total_voltage_drop, tolerance)

        self.assertEqual(kvl_law, "FAILED")

    # Check if KVL passes with 0 voltage
    def test_circuit_laws_kvl_zero_voltage(self) -> None:
        voltage = 0
        total_voltage_drop = 0

        kvl_law = utils.check_kvl(voltage, total_voltage_drop)

        self.assertEqual(kvl_law, "PASSED")

    # Check if KVL is not applicable when total_voltage_drop is None
    def test_circuit_laws_kvl_not_applicable(self) -> None:
        voltage = 12
        total_voltage_drop = None

        kvl_law = utils.check_kvl(voltage, total_voltage_drop)

        self.assertEqual(kvl_law, "N/A")

    # Check if KCL passes with correct values
    def test_circuit_laws_kcl_correct_current_split(self) -> None:
        total_current = 5
        total_current_change = 5

        kcl_law = utils.check_kcl(total_current, total_current_change)

        self.assertEqual(kcl_law, "PASSED")

    # Check if KCL fails with incorrect values
    def test_circuit_laws_kcl_incorrect_current_split(self) -> None:
        total_current = 5
        total_current_change = 4

        kcl_law = utils.check_kcl(total_current, total_current_change)

        self.assertEqual(kcl_law, "FAILED")

    # Check if KCL passes with precision error within tolerance
    def test_circuit_laws_kcl_within_tolerance(self) -> None:
        total_current = 5
        total_current_change = 5.0000005
        tolerance = 1e-6

        kcl_law = utils.check_kcl(total_current, total_current_change, tolerance)

        self.assertEqual(kcl_law, "PASSED")

    # Check if KCL fails with precision error outside tolerance
    def test_circuit_laws_kcl_outside_tolerance(self) -> None:
        total_current = 5
        total_current_change = 5.000002
        tolerance = 1e-6

        kcl_law = utils.check_kcl(total_current, total_current_change, tolerance)

        self.assertEqual(kcl_law, "FAILED")

    # Check if KCL passes with 0 current
    def test_circuit_laws_kcl_zero_current(self) -> None:
        total_current = 0
        total_current_change = 0

        kcl_law = utils.check_kcl(total_current, total_current_change)

        self.assertEqual(kcl_law, "PASSED")

    # Check if KCL is not applicable when total_current_change is None
    def test_circuit_laws_kcl_not_applicable(self) -> None:
        total_current = 5
        total_current_change = None

        kcl_law = utils.check_kcl(total_current, total_current_change)

        self.assertEqual(kcl_law, "N/A")

    # Check if power conservation passes with correct values
    def test_circuit_laws_power_correct_power(self) -> None:
        total_power = 36
        source_power = 36

        power_conservation = utils.check_power_conservation(total_power, source_power)

        self.assertEqual(power_conservation, "PASSED")

    # Check if power conservation fails with incorrect values
    def test_circuit_laws_power_incorrect_power(self) -> None:
        total_power = 36
        source_power = 30

        power_conservation = utils.check_power_conservation(total_power, source_power)

        self.assertEqual(power_conservation, "FAILED")

    # Check if power conservation passes with precision error within tolerance
    def test_circuit_laws_power_within_tolerance(self) -> None:
        total_power = 36
        source_power = 36.0000005
        tolerance = 1e-6

        power_conservation = utils.check_power_conservation(total_power, source_power, tolerance)

        self.assertEqual(power_conservation, "PASSED")

    # Check if power conservation fails with precision error outside tolerance
    def test_circuit_laws_power_outside_tolerance(self) -> None:
        total_power = 36
        source_power = 36.000002
        tolerance = 1e-6

        power_conservation = utils.check_power_conservation(total_power, source_power, tolerance)

        self.assertEqual(power_conservation, "FAILED")

    # Check if power conservation passes with 0 power
    def test_circuit_laws_power_zero_power(self) -> None:
        total_power = 0
        source_power = 0

        power_conservation = utils.check_power_conservation(total_power, source_power)

        self.assertEqual(power_conservation, "PASSED")
