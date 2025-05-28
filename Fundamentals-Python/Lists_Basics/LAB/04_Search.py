strings_count = int(input())
secret_word = input()

strings = []
filtered_strings = []

for cur_string in range(strings_count):

    string = input()
    strings.append(string)


for string in strings:

    if secret_word in string:
        filtered_strings.append(string)

print(strings)
print(filtered_strings)
