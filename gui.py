import tkinter as tk
from calculator.basic_calc import add, subtract, multiply, divide
from calculator.advanced_calc import square_root, power, logarithm

def perform_operation():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        operation = operation_var.get()

        if operation == 'add':
            result = add(a, b)
        elif operation == 'subtract':
            result = subtract(a, b)
        elif operation == 'multiply':
            result = multiply(a, b)
        elif operation == 'divide':
            result = divide(a, b)
        elif operation == 'sqrt':
            result = square_root(a)
        elif operation == 'power':
            result = power(a, b)
        elif operation == 'log':
            result = logarithm(a, b)
        else:
            result = "Invalid operation"

        label_result.config(text=f"Result: {result}")
    except Exception as e:
        label_result.config(text=f"Error: {str(e)}")

def set_inputs(a, b, operation):
    entry_a.delete(0, tk.END)
    entry_a.insert(0, str(a))
    entry_b.delete(0, tk.END)
    entry_b.insert(0, str(b))
    operation_var.set(operation)

def get_result():
    return label_result.cget("text")

root = tk.Tk()
root.title("Calculator")

entry_a = tk.Entry(root)
entry_a.pack()

entry_b = tk.Entry(root)
entry_b.pack()

operation_var = tk.StringVar(root)
operation_var.set("add")  # default value

operations = ["add", "subtract", "multiply", "divide", "sqrt", "power", "log"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack()

button_calc = tk.Button(root, text="Calculate", command=perform_operation)
button_calc.pack()

label_result = tk.Label(root, text="Result: ")
label_result.pack()

if __name__ == "__main__":
    root.mainloop()
