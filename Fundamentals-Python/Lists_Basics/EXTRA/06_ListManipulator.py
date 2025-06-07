my_list = input()
my_list_str = my_list.split(' ')
command = input()
odd_list = []
even_list = []
new_list = my_list_str
final_list = []

for number in my_list_str:
    number = int(number)
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

while command != "end":
    parts_command = command.split(' ')
    type_command = parts_command[0]

    if type_command == "exchange":
        exchange_index = int(parts_command[1])
        new_list = []

        if exchange_index > len(my_list_str) - 1 or exchange_index < 0:
            print("Invalid index")
        else:
            new_list = my_list_str[exchange_index + 1:] + my_list_str[:exchange_index + 1]
            new_list_int = []
            for i in new_list:
                new_list_int.append(int(i))
            print(new_list_int)

    elif type_command == "max":
        if parts_command[1] == "even":
            if even_list:
                max_even = max(even_list)
                for i in range(-1, -len(my_list_str) - 1, -1):
                    max_even_index = 0
                    if int(my_list_str[i]) == max_even:
                        max_even_index = i + len(my_list_str)
                        print(max_even_index)
                        break
            else:
                print("No matches")

        elif parts_command[1] == "odd":
            if len(odd_list) > 0:
                max_odd = max(odd_list)
                for i in range(-1, -len(my_list_str) - 1, -1):
                    max_odd_index = 0
                    if int(my_list_str[i]) == max_odd:
                        max_odd_index = i + len(my_list_str)
                        print(max_odd_index)
                        break

            else:
                print("No matches")

    elif type_command == "min":
        if parts_command[1] == "even":
            if even_list:
                min_even = min(even_list)
                for i in range(-1, -len(my_list_str) - 1, -1):
                    min_even_index = 0
                    if int(my_list_str[i]) == min_even:
                        min_even_index = i + len(my_list_str)
                        print(min_even_index)
                        break
            else:
                print("No matches")

        elif parts_command[1] == "odd":
            if odd_list:
                min_odd = min(odd_list)
                for i in range(-1, -len(my_list_str) - 1, -1):
                    min_odd_index = 0
                    if int(my_list_str[i]) == min_odd:
                        min_odd_index = i + len(my_list_str)
                        print(min_odd_index)
                        break
            else:
                print("No matches")

    elif type_command == "first":
        count = int(parts_command[1])
        even_or_odd = parts_command[2]

        if count > len(my_list_str):
            print("Invalid count")


        elif even_or_odd == "even":
            first_even = []

            if even_list:
                for i in range(count):
                    if i > len(even_list) - 1:
                        break
                    first_even.append(even_list[i])

            print(first_even)

        elif even_or_odd == "odd":
            first_odd = []

            if odd_list:
                for i in range(count):
                    if i > len(odd_list) - 1:
                        break
                    first_odd.append(odd_list[i])

            print(first_odd)


    elif type_command == "last":
        count = int(parts_command[1])
        even_or_odd = parts_command[2]
        even_list.reverse()
        odd_list.reverse()

        if count > len(my_list_str):
            print("Invalid count")


        elif even_or_odd == "even":
            last_even = []

            if even_list:
                for i in range(count):
                    if i > len(even_list) - 1:
                        break
                    last_even.append(even_list[i])

            last_even.reverse()

            print(last_even)

        elif even_or_odd == "odd":
            last_odd = []

            if odd_list:
                for i in range(count):
                    if i > len(odd_list) - 1:
                        break
                    last_odd.append(odd_list[i])

            last_odd.reverse()
            print(last_odd)

    command = input()
for i in new_list:
    final_list.append(int(i))

print(final_list)