import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00
MAX_PRICE = 100.00
INITIAL_PRICE = 10.00
NUMBER_OF_DAYS = 425
FILENAME = "stock_prices.txt"

# Initialize the starting price
price = INITIAL_PRICE
out_file = open(FILENAME, 'w')

# Write the starting price
print(f"Starting price: ${price:,.2f}", file=out_file)

for day in range(1, NUMBER_OF_DAYS + 1):
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    if MIN_PRICE <= price <= MAX_PRICE:
        print(f"On day {day} price is: ${price:,.2f}", file=out_file)
    else:
        break

print(f"On day {day} price is: ${price:,.2f}", file=out_file)
out_file.close()