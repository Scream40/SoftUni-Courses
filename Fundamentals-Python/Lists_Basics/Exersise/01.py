string = input()

my_list = string.split(' ')
new_list = []

for num in my_list:

    new_list.append(-int(num))

print(new_list)

