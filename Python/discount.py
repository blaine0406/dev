# import sys

# Function to get input and convert to float
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not a valid number!")


# Actual Math for conversion
def calculate_discounted_price(amount, discount):
    return round(amount * (1 - discount / 100), 2) #Returns the rounded amount

def main():
    amount = get_float("Enter the amount: $")
    discount = get_float("Enter the discount %: ")
    total = calculate_discounted_price(amount, discount)
    print(f"Final Total: ${total}")

if __name__ == "__main__":
    main()
