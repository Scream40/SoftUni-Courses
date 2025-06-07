my_list = input().split(' ')

command = input()
new_list = []
odd_list = []
even_list = []

for number in my_list:
    number = int(number)
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

print(len(odd_list))

while command != "end":
    command_parts = command.split(' ')
    type_command = command_parts[0]

    if type_command == "exchange":
        exchange_index = int(command_parts[1])

        if 0 > exchange_index > len(my_list) - 1:
            print("Invalid index")
        else:
            new_list =  my_list[exchange_index:] +  my_list[:exchange_index]
            print(new_list)

    elif type_command == "max":
        if command_parts[1] == "even":
            if even_list:
                max_even = max(even_list)
                for i in range(-1, -len(my_list) - 1, -1):
                    max_even_index = 0
                    if int(my_list[i]) == max_even:
                        max_even_index = i + len(my_list)
                        print(max_even_index)
                        break
            else:
                print("No matches")

        elif type_command[1] == "odd":
            if len(odd_list) > 0:
                max_odd = max(odd_list)
                for i in range(-1, -len(my_list) - 1, -1):
                    max_odd_index = 0
                    if int(my_list[i]) == max_odd:
                        max_odd_index = i + len(my_list)
                        print(max_odd_index)
                        break

            else:
                print("No matches")

    elif type_command == "min":
        if command_parts[1] == "even":
            if even_list:
                min_even = min(even_list)
                print(min_even)
            else:
                print("No matches")

        elif type_command[1] == "odd":
            if odd_list:
                min_odd = min(odd_list)
                print(min_odd)
            else:
                print("No matches")

    elif type_command == "first":
        num = int(command_parts[1])
        even_or_odd = command_parts[2]

        if even_or_odd == "even":
            first_even = []
            for i in range(num):
                first_even.append(even_list[i])
            print(first_even)


        elif even_or_odd == "odd":
            pass


    elif type_command == "last":
        pass



    command = input()