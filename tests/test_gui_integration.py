import unittest
import tkinter as tk
from gui import set_inputs, get_result, perform_operation

class TestCalculatorGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.title("Calculator")

        self.entry_a = tk.Entry(self.root)
        self.entry_a.pack()

        self.entry_b = tk.Entry(self.root)
        self.entry_b.pack()

        self.operation_var = tk.StringVar(self.root)
        self.operation_var.set("add")  # Set default operation

        self.operations = ["add", "subtract", "multiply", "divide", "sqrt", "power", "log"]
        self.operation_menu = tk.OptionMenu(self.root, self.operation_var, *self.operations)
        self.operation_menu.pack()

        self.button_calc = tk.Button(self.root, text="Calculate", command=perform_operation)
        self.button_calc.pack()

        self.label_result = tk.Label(self.root, text="Result: ")
        self.label_result.pack()

    def tearDown(self):
        self.root.quit()
        self.root.destroy()

    def test_addition(self):
        set_inputs('2', '3', 'add')  # Set input values and operation
        perform_operation()  # Trigger the calculation
        result = get_result()  # Get the result from the GUI
        expected_result = 'Result: 5.0'  # Update the expected result
        self.assertEqual(result, expected_result)  # Compare the results

    def test_subtraction(self):
        set_inputs('5', '2', 'subtract')  # Set input values and operation
        perform_operation()  # Trigger the calculation
        result = get_result()  # Get the result from the GUI
        expected_result = 'Result: 3.0'  # Update the expected result
        self.assertEqual(result, expected_result)  # Compare the results

if __name__ == '__main__':
    unittest.main()
