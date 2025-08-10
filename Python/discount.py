import sys


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not a valid number!")


def calculate_discounted_price(amount, discount):
    return round(amount * (1 - discount / 100), 2)

def main():
    amount = get_float("Enter the amount: $")
    discount = get_float("Enter the discount %: ")
    total = calculate_discounted_price(amount, discount)
    print(f"Final Total: ${total}")

if __name__ == "__main__":
    main()



