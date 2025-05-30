number = int(input())

is_prime = True

for dev in range(2, number):

    if number % dev == 0:
        is_prime = False
        break

print(is_prime)