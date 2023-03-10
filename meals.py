from asyncio import streams


child_meal = float(input( "What is the price of a child's meal? " ))

adult_meal = float(input( "What is the price of an adult's meal? " ))

number_of_children = int(input( "How many chlidren are there? " ))

number_of_adults = int(input( "How many chlidren are there? " ))

sale_tax = float(input("What is the sale tax rate? " ))

subtotal = child_meal * number_of_children + adult_meal * number_of_adults

tax = subtotal * sale_tax / 100

total = subtotal + sale_tax


print(f"Subtotal: ${subtotal:.2f}")

print(f"Sales Tax: ${tax:.2f}")

print(f"Total: ${total:.2f}")

payment_amount = float(input("What is the payment amount? "))

change = payment_amount - total

print(f"Change is: ${change:.2f}")

