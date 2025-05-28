group_size = int(input())
days = int(input())




coins_earned = 0

for current_day in range(1, days +1):

    if current_day % 10 == 0:
        group_size -= 2 # deserters

    if current_day % 15 == 0:
        group_size += 5 # fresh strength

    food_for_the_companions = 2 * group_size  # food is must
    daily_earnings = 50 - food_for_the_companions
    coins_earned += daily_earnings

    if current_day % 3 == 0: # people need watter
        coins_earned -= 3 * group_size

    if current_day % 5 == 0: # slay the Dragon
        coins_earned += 20 * group_size

        if current_day % 3 == 0: # if trow a party
            coins_earned -= 2 * group_size

coins_per_companion = int(coins_earned / group_size) # to be fair

print(f"{group_size} companions received {coins_per_companion} coins each.")