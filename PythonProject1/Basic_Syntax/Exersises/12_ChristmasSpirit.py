PRICE_ORNAMENT_SET = 2
PRICE_TREE_SKIRT = 5
PRICE_TREE_GARLAND = 3
PRICE_TREE_LIGHTS = 15
POINTS_ORNAMENT_SET = 5
POINTS_TREE_SKIRT = 3
POINTS_TREE_GARLAND = 10
POINTS_TREE_LIGHTS = 17

quantity_of_decorations = int(input())
days_until_christmas = int(input())

money_needed = 0
christmas_spirit = 0
days_left = days_until_christmas

for shopping_day in range(1, days_until_christmas + 1):

    if shopping_day % 11 == 0:
        quantity_of_decorations += 2


    if shopping_day % 2 == 0:
        money_needed += PRICE_ORNAMENT_SET * quantity_of_decorations
        christmas_spirit += POINTS_ORNAMENT_SET

    if shopping_day % 3 == 0:
        money_needed += (PRICE_TREE_SKIRT * quantity_of_decorations) + (PRICE_TREE_GARLAND * quantity_of_decorations)
        christmas_spirit += POINTS_TREE_SKIRT + POINTS_TREE_GARLAND


    if shopping_day % 5 == 0:
        money_needed += PRICE_TREE_LIGHTS * quantity_of_decorations
        christmas_spirit += POINTS_TREE_LIGHTS
        if shopping_day % 3 == 0:
            christmas_spirit += 30


    if shopping_day % 10 == 0:
        christmas_spirit -= 20
        money_needed += PRICE_TREE_SKIRT + PRICE_TREE_GARLAND + PRICE_TREE_LIGHTS

if days_until_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {money_needed}")
print(f"Total spirit: {christmas_spirit}")



