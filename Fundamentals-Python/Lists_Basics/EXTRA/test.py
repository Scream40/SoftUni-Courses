my_list = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break

    parts_command = command.split()
    action = parts_command[0]

    if action == "exchange":
        index = int(parts_command[1])
        if 0 <= index < len(my_list):
            my_list = my_list[index+1:] + my_list[:index+1]
        else:
            print("Invalid index")

    elif action == "max" or action == "min":
        parity = parts_command[1]
        filtered = [num for num in my_list if num % 2 == (0 if parity == "even" else 1)]
        if not filtered:
            print("No matches")
        else:
            target = max(filtered) if action == "max" else min(filtered)
            # Rightmost index
            for i in range(len(my_list)-1, -1, -1):
                if my_list[i] == target:
                    print(i)
                    break

    elif action == "first" or action == "last":
        count = int(parts_command[1])
        parity = parts_command[2]
        if count > len(my_list):
            print("Invalid count")
            continue

        filtered = [num for num in my_list if num % 2 == (0 if parity == "even" else 1)]
        if action == "first":
            print(filtered[:count])
        else:
            print(filtered[-count:])

print(my_list)