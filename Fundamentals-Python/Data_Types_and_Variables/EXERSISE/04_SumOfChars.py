number_of_lines = int(input())

sum = 0

for _ in range(number_of_lines):

    letter = input()

    sum += ord(letter)

print(f"The sum equals: {sum}")