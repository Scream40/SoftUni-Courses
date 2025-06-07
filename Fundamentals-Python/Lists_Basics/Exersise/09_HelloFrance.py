TICKET_PRICE = 150
CLOTHES_MAX_PRICE = 50.00
SHOES_MAX_PRICE = 35.00
ACCESSORIES_MAX_PRICE = 20.50

items_collection = input().split("|")
budget = float(input())

current_money = budget
bought_items_prices = []
items_new_prices = []
earnings_from_sales = 0
spent_money = 0

for item in items_collection:

    new_item = item.split("->")
    type_item = new_item[0]
    price_item = float(new_item[1])

    if type_item == "Clothes":
        if price_item <= CLOTHES_MAX_PRICE and price_item <= current_money:
            current_money -= price_item
            bought_items_prices.append(price_item)


    elif type_item == "Shoes":
        if price_item <= SHOES_MAX_PRICE and price_item <= current_money:
            current_money -= price_item
            bought_items_prices.append(price_item)

    elif type_item == "Accessories":
        if price_item <= ACCESSORIES_MAX_PRICE and price_item <= current_money:
            current_money -= price_item
            bought_items_prices.append(price_item)

# selling the items and calculate earnings and money spent to buy items.
for new_price in bought_items_prices:
    spent_money += new_price
    new_price = new_price * 1.4
    items_new_prices.append(new_price)
    earnings_from_sales += new_price

current_money += earnings_from_sales
profit = earnings_from_sales - spent_money

for prices in range(len(items_new_prices)):
    if prices < len(items_new_prices) - 1:
        print(f"{items_new_prices[prices]:.2f}", end=" ")
    else:
        print(f"{items_new_prices[prices]:.2f}")

print(f"Profit: {profit:.2f}")
if current_money >= TICKET_PRICE:
    print("Hello, France!")
else:
    print("Not enough money.")