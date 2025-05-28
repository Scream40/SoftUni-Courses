animal_elements = []

for current_element in range(3):
    element = input()
    animal_elements.append(element)

animal_elements[0], animal_elements[2] = animal_elements[2], animal_elements[0]

print(animal_elements)



