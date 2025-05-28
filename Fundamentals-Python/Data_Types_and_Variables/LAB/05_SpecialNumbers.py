n = int(input())

for num in range(1, n + 1):

    num_as_str = str(num)
    digit_sum = 0
    is_special = False

    for digit in num_as_str:

        digit_sum += int(digit)

    if digit_sum in [5, 7, 11]:
        is_special = True

    print(f"{num} -> {is_special}")






