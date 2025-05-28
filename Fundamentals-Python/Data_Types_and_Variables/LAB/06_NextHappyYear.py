year = int(input())

is_happy_year = False

while not is_happy_year:
    year += 1
    year_as_str = str(year)

    if len(year_as_str) == len(set(year_as_str)):
        print(year)
        break








