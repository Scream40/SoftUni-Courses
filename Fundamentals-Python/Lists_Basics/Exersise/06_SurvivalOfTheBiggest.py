list_numbers = input().split(" ")
numbers_to_remove = int(input())
int_numbers = []
to_remove = []

# making list_numbers to integers
for num in list_numbers:
    int_numbers.append(int(num))

# sorting numbers
int_numbers.sort()
sorted_numbers = int_numbers

# creating list with numbers need to be removed from the original list
for number in range(numbers_to_remove):
    to_remove.append(sorted_numbers.pop(0))

# removing the smallest numbers from the original list
for x in to_remove:
    list_numbers.remove(str(x))

# printing what`s left from the original list
for y in range(len(list_numbers)):
    if y == len(list_numbers) - 1:
        print(f"{list_numbers[y]}")
    else:
        print(f"{list_numbers[y]}, ", end='')



