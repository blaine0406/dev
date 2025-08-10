import sys


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not a valid number!")

amount = get_float("Enter the amount: ")

print(amount)

