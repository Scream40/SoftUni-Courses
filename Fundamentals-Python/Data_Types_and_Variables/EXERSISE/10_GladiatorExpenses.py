lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_shield_count = 0

expenses = 0

for current_fight in range(1, lost_fights + 1):

    if current_fight % 2 == 0:
        expenses += helmet_price

    if current_fight % 3 == 0:
        expenses += sword_price

        if current_fight % 2 == 0:
            expenses += shield_price
            broken_shield_count += 1

        if broken_shield_count == 2:
            expenses += armor_price
            broken_shield_count = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")