number = input()

number_list = list(number)

number_list.sort(reverse=True)

largest_number = ''.join(number_list)

print(largest_number)

