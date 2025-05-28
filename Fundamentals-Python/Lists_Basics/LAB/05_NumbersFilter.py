integers_count = int(input())

numbers = []
filtered_numbers = []

for _ in range(integers_count):

    number = int(input())
    numbers.append(number)

command = input()

for cur_n in numbers:

    if ((command == 'even' and cur_n % 2 == 0)
        or (command == 'odd' and cur_n % 2 != 0)
        or (command == 'negative' and cur_n < 0)
        or (command == 'positive' and cur_n >= 0)):
         filtered_numbers.append(cur_n)




print(filtered_numbers)
