# Shopping Cart
print("Welcome to the Shopping Cart Program!")

items = []
prices = []
item = None
total_price = 0
while True:
    print()
    print("Please select on the following: ")
    print("1. Add item ")
    print("2. View cart ")
    print("3. Remove Item ")
    print("4. Compute total")
    print("5. Quit")
# Build the lists

    action = int(input('Please enter an action: '))
    if action == 1:
        item = input("What item would you like to add? ")
        price = float(input(f'What is the price of {item}? '))
        print(f'{item} has been added to the cart.')

        items.append(item)
        prices.append(price)

    if action == 2:
        print("The contents of the shopping cart are: ")
        for item in items:
         print(f'{item} - ${price}')

    if action == 3:
        remove = input('What item would you like to remove? ')
        items.remove(remove) 

    if action == 4: 
         for price in prices:
            total_price += price
            print(f"The total price of the items in the shopping cart is ${total_price:.2f}")
    
    if action == 5:
        print('Thank you. Goodbye.')
        break
