import os
from art import logo

print(logo)


# add
def add(num1, num2):
    return num1 + num2


# subtract
def sub(num1, num2):
    return num1 - num2


# multiply
def multiply(num1, num2):
    return num1 * num2


# divide
def divide(num1, num2):
    return num1 / num2


def calculator():
    num1 = float(input("What's the first number?: "))

    values = {"+": add, "-": sub, "*": multiply, "/": divide}

    for symbol in values:
        print(symbol)

    check = 'y'
    while check == 'y':

        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = values[operation]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        check = input(
            f"Type 'y' to continue calculating with {answer}, or Type 'n' to start a new calculation.: ").lower()
        if check == 'y':
            num1 = answer
        else:
            os.system('cls')
            calculator()


calculator()
