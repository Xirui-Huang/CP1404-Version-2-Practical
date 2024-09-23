DISCOUNT_THRESHOLD = 100  # Threshold for applying discount
DISCOUNT_RATE = 0.10      # Discount rate of 10%

# Initialize total price
total_price = 0

# Get the number of items from the user
number_items = int(input("Number of items: "))

# Process each item's price and add to the total price
for i in range(1, number_items + 1):
    price = float(input(f"Price of item {i}: "))
    total_price += price

# Apply discount if the total price exceeds the threshold
if total_price > DISCOUNT_THRESHOLD:
    total_price -= total_price * DISCOUNT_RATE

# Output the total price formatted to two decimal places
print(f"Total price for {number_items} items is ${total_price:.2f}")

