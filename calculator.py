def calculate(a, b, op):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Error: invalid number"

    if op in ("+", "add"):
        return a + b
    if op in ("-", "sub"):
        return a - b
    if op in ("*", "x", "mul"):
        return a * b
    if op in ("/", "div"):
        if b == 0:
            return "Error: division by zero"
        return a / b

    return "Error: unknown operation"


def main():
    print("Simple Calculator — enter two numbers and an operation")
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    op = input("Enter operation (+, -, *, /): ")
    result = calculate(a, b, op)
    print("Result:", result)


if __name__ == "__main__":
    main()
