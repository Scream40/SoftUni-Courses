TANK_CAPACITY = 255

number_of_fillings = int(input())

watter_in_tank = 0

for current_filling in range(number_of_fillings):

    litters = int(input())

    if TANK_CAPACITY >= litters:
        TANK_CAPACITY -= litters
        watter_in_tank += litters

    else:
        print("Insufficient capacity!")
        continue

print(watter_in_tank)