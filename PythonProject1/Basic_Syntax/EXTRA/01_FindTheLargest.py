# Read input from the user
number = input("Enter a number: ")

# Convert the string into a list of characters (digits)
digits = list(number)

# Manual sorting in descending order (selection sort)
n = len(digits)
for i in range(n):
    max_idx = i
    for j in range(i + 1, n):
        if digits[j] > digits[max_idx]:
            max_idx = j
    # Swap the elements
    digits[i], digits[max_idx] = digits[max_idx], digits[i]

# Join the sorted digits into a string
largest_number = ''.join(digits)

# Print the result
print("The largest number formed is:", largest_number)
