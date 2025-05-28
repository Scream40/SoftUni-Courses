command = input()

coffee_needed = 0
need_sleep = False

while command != "END":

    if command in ["coding", "dog", "cat", "movie"]:
        coffee_needed += 1

    elif command in ["CODING", "DOG", "CAT", "MOVIE"]:
        coffee_needed += 2

    if coffee_needed > 5:
        print("You need extra sleep")
        need_sleep = True
        break

    command = input()

if not need_sleep:
    print(coffee_needed)