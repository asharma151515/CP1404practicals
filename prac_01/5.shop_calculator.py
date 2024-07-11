def main():
    total_price = 0
    num_items = int(input("Number of items: "))
    while num_items < 0:
        print("Invalid number of items. Please enter a valid number.")
        num_items = int(input("Number of items: "))
    for _ in range(num_items):
        price = float(input("Price of item: "))
        total_price += price
    if total_price > 100:
        total_price *= 0.9
    print("Total price for {} items is ${:.2f}".format(num_items, total_price))

if __name__ == '__main__':
    main()