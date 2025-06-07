COFFEE_PRICE = 1.50
WATER_PRICE = 1.00
COKE_PRICE = 1.40
SNACKS_PRICE = 2.00

product = input()
quantity = int(input())

def calculating_price (prod_type, amount):

    total_price = None

    if prod_type == "coffee":
        total_price = amount * COFFEE_PRICE
    elif prod_type == "coke":
        total_price = amount * COKE_PRICE
    elif prod_type == "water":
        total_price = amount * WATER_PRICE
    elif prod_type == "snacks":
        total_price = amount * SNACKS_PRICE

    return total_price

print(f'{calculating_price(product, quantity):.2f}')