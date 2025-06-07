numbers_list = input().split(' ')
text = input()
text_list = list(text)

message = ''

for current_number in numbers_list:

    index_sum = 0

    for digit in current_number:
        index_sum += int(digit)

    char_index = index_sum % len(text_list)

    message += text_list.pop(char_index)

print(message)


