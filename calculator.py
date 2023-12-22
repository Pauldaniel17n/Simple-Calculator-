def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def exponentiate(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exponentiate' for exponentiation")
    print("Enter 'sqrt' for square root")
    print("Enter 'factorial' for factorial")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break

    if user_input in ["add", "subtract", "multiply", "divide", "exponentiate"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    elif user_input in ["sqrt", "factorial"]:
        num1 = float(input("Enter a number: "))

    if user_input == "add":
        print(add(num1, num2))
    elif user_input == "subtract":
        print(subtract(num1, num2))
    elif user_input == "multiply":
        print(multiply(num1, num2))
    elif user_input == "divide":
        print(divide(num1, num2))
    elif user_input == "exponentiate":
        print(exponentiate(num1, num2))
    elif user_input == "sqrt":
        print(square_root(num1))
    elif user_input == "factorial":
        print(factorial(int(num1)))
    else:
        print("Invalid input. Please enter a valid option.")
