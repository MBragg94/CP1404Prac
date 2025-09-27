
num_items = int(input("Number of items: "))
total_price = 0.0
while num_items > 0:
    for i in range(num_items):
        price = float(input(f"Price of item {i + 1}: "))
        total_price += price
    if total_price > 100:
        total_price *= 0.9
    print(f"Total price for {num_items} items is ${total_price:.2f}")
    num_items = int(input("Number of items: "))
else:
    print("Invalid Number of Items")
    num_items = int(input("Number of items: "))