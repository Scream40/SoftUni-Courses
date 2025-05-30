number1 = int(input())
number2 = int(input())

print("Before:")
print(f"a = {number1}")
print(f"b = {number2}")

number1, number2 = number2, number1

print("After:")
print(f"a = {number1}")
print(f"b = {number2}")


