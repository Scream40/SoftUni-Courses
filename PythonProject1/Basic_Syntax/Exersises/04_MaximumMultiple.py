divisor = int(input())
boundary = int(input())

largest_N = 0

for x in range(1, boundary + 1, 1):
    if x % divisor == 0:
        largest_N = x

print(largest_N)
