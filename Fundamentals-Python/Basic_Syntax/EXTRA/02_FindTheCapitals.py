string = input()

upper_list = []

for idx in range(len(string)):

    if string[idx].isupper():
        upper_list.append(idx)

print(upper_list)