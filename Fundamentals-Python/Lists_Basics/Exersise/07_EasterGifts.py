gifts_list = input().split(' ')
command = input()

while command != "No Money":

    if "OutOfStock" in command:
        command_list = command.split(' ')
        gift = command_list[1]
        if gift in gifts_list:
            for i in range(len(gifts_list)):
                if gifts_list[i] == gift:
                    gifts_list[i] = "None"

    elif "Required" in command:
        command_list = command.split(' ')
        index = int(command_list[2])
        gift1 = command_list[1]
        if len(gifts_list) > index >= 0:
            gifts_list[index] = gift1

    elif "JustInCase" in command:
        command_list = command.split(' ')
        gift2 = command_list[1]
        gifts_list[-1] = gift2

    command = input()
final_gifts = []

for i in range(len(gifts_list)):
    if gifts_list[i] != "None":
        final_gifts.append(gifts_list[i])

print(" ".join(final_gifts))