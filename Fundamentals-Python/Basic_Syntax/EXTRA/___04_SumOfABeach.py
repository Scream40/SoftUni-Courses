string = 'gOfIshsunesunFiSh'

string = string.lower()

counter = 0

for char in string:
    if char == 'w':
        if 'water' in string:
            string = string.replace('water', '')
            counter += 1

    elif char == 'f':
        if 'fish' in string:
            string = string.replace('fish', '')
            counter += 1

    elif char == 's':
        if 'sun' in string:
            string = string.replace('sun', "")
            counter += 1
        elif 'sand' in string:
            string = string.replace('sand', "")
            counter += 1



print(counter)

