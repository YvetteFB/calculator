# Addition
def add(x, y):
    return x + y


# Subtraction
def subtract(x, y):
    return x - y


# Multiplication
def multiply(x, y):
    return x * y


# Division
def divide(x, y):
    return x / y


print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    operation = input("Select operation: ")

    # check if operation is one of the four options
    if operation in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operation == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif operation == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif operation == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

        else:
            print("Invalid Input")
