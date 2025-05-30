key = int(input())
lines_count = int(input())

code_message = ''

for line in range(lines_count):

    letter = input()
    true_letter = chr(ord(letter) + key)
    code_message += true_letter

print(code_message)



