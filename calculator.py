import math
import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/calculator.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s")

def square_root(x):
    result = math.sqrt(x)
    logging.info(f"Square root of {x} = {result}")
    return result

def factorial(x):
    result = math.factorial(x)
    logging.info(f"Factorial of {x} = {result}")
    return result

def natural_log(x):
    result = math.log(x)
    logging.info(f"ln({x}) = {result}")
    return result

def power(x, b):
    result = math.pow(x, b)
    logging.info(f"{x}^{b} = {result}")
    return result


def menu():
    while True:
        print("\nScientific Calculator")
        print("\nChoose one option:-")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Natural Log")
        print("4. Power")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            x = float(input("Enter number: "))
            print(square_root(x))

        elif choice == 2:
            x = int(input("Enter number: "))
            print(factorial(x))

        elif choice == 3:
            x = float(input("Enter number: "))
            print(natural_log(x))

        elif choice == 4:
            x = float(input("Enter base: "))
            b = float(input("Enter power: "))
            print(power(x, b))

        elif choice == 5:
            break

if __name__ == "__main__":
    menu()
