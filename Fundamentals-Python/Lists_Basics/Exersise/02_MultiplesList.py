factor = int(input())
count = int(input())

my_list = [factor]

while len(my_list) < count:
    add_number = factor + (len(my_list) * factor)
    my_list.append(add_number)

print(my_list)