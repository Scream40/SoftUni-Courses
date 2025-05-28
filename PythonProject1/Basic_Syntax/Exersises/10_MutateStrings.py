first_string = input()
second_string = input()
new_string = first_string

for char in range(len(first_string)):

    left_string = second_string[:char + 1]
    right_string = first_string[char + 1:]

    if first_string[char] != second_string[char]:
        new_string = left_string + right_string
        print(new_string)