from calculator.basic_calc import add, subtract, multiply, divide
from calculator.advanced_calc import square_root, power, logarithm

def perform_operation(a, b, operation):
    try:
        if operation == 'add':
            return add(a, b)
        elif operation == 'subtract':
            return subtract(a, b)
        elif operation == 'multiply':
            return multiply(a, b)
        elif operation == 'divide':
            return divide(a, b)
        elif operation == 'sqrt':
            return square_root(a)
        elif operation == 'power':
            return power(a, b)
        elif operation == 'log':
            return logarithm(a, b)
        else:
            return "Invalid operation"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Operations: add, subtract, multiply, divide, sqrt, power, log")
            operation = input("Enter the operation: ")

            result = perform_operation(a, b, operation)
            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter a number.")
        
        if input("Do you want to continue? (yes/no): ").lower() != 'yes':
            break
