number_of_people = int(input())
capacity = int(input())

courses = 0

while number_of_people > 0:

    if number_of_people >= capacity:
        number_of_people -= capacity

    else:
        number_of_people = 0

    courses += 1

print(courses)



