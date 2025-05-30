lines_count = int(input())

is_balanced = True

bracket = 0

for _ in range(lines_count):

    char = input()

    if char == '(':
        bracket += 1

        if bracket > 1:
            is_balanced = False
            break

    elif char == ')':
        bracket -= 1
        if bracket < 0:
            is_balanced = False
            break

if bracket != 0:
    is_balanced = False


if is_balanced:
    print("BALANCED")

else:
    print("UNBALANCED")





