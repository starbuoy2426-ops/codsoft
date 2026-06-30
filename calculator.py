import math

print("=" * 40)
print("      Advanced Python Calculator")
print("=" * 40)
print("Supported Operations:")
print("+   Addition")
print("-   Subtraction")
print("*   Multiplication")
print("/   Division")
print("%   Modulus")
print("**  Power")
print("//  Floor Division")
print("sqrt(x)")
print("abs(x)")
print("round(x)")
print("Type 'exit' to quit.")
print("=" * 40)

allowed_functions = {
    "sqrt": math.sqrt,
    "abs": abs,
    "round": round,
    "pow": pow
}

while True:
    expression = input("\nEnter Expression: ")

    if expression.lower() == "exit":
        print("Calculator Closed.")
        break

    try:
        result = eval(expression, {"__builtins__": None}, allowed_functions)
        print("Result =", result)

    except ZeroDivisionError:
        print("Error: Division by zero!")

    except Exception:
        print("Invalid Expression!")