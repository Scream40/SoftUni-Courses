string = input()
string_list = string.split(', ')

for animal in range(-1, -len(string_list) - 1, -1):

    # print(f"{string_list[animal]} -> idx {animal}")

    if string_list[-1] == 'wolf':
        print("Please go away and stop eating my sheep")
        break

    elif string_list[animal] == 'wolf':
        print(f"Oi! Sheep number {abs(animal + 1)}! You are about to be eaten by a wolf!")
        break


