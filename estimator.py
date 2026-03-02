item = input("\nWhat would you like to buy?: ")

while True:
    try:
        price = float(
            input(f"How much is one single {item} going to cost £: "))
        break
    except ValueError:
        print("Error: Please enter the price using numbers (e.g., 3.75)")

while True:
    try:
        quantity = int(input(f"Amount, how many {item} do you want to buy?: "))
        break
    except ValueError:
        print("Error: Quantity must be a whole number.")

total = price * quantity

print(f"\nIf you buy {quantity} x {item}")
print(f"Your total is £{total:.2f}\n")
