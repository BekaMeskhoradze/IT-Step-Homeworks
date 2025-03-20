def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    if b == 0:
        return "Division by zero is not allowed!"
    return a / b

def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Try again!")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Try again!")

    while True:
        operation = input("Enter The operation: ")

        if operation == '+':
            result = add(num1, num2)
            break
        elif operation == '-':
            result = sub(num1, num2)
            break
        elif operation == '*':
            result = mult(num1, num2)
            break
        elif operation == '/':
            result = div(num1, num2)
            break
        else:
            print("Invalid operation selected. Please try again.")

    return f"The result is: {result}"

print(calculator())