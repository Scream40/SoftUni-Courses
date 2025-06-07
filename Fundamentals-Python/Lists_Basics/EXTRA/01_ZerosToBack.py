string = input().split(", ")

new_string = []

for n in string:
    if n != '0':
        new_string.append(int(n))

for f in string:
    if f == '0':
        new_string.append(int(f))

# for i in range(len(string)):
#     if string[i] != '0':
#         new_string.append(int(string[i]))
#
# for y in range(len(string)):
#     if string[y] == '0':
#         new_string.append(int(string[y]))

print(new_string)