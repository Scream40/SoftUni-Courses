budget = float(input())
flour_price_kg = float(input())

eggs_price = flour_price_kg * 0.75
milk_price_1lit = flour_price_kg * 1.25

loaf_recipe = flour_price_kg + eggs_price + (milk_price_1lit * 0.25)

colored_eggs = 0
loaf_maid = 0

while True:

    if budget - loaf_recipe < 0:
        break

    loaf_maid += 1
    colored_eggs += 3

    if loaf_maid % 3 == 0:
        colored_eggs -= (loaf_maid - 2)

    budget -= loaf_recipe

print(f"You made {loaf_maid} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")