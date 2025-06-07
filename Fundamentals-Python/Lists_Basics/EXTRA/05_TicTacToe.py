string1 = input().split(' ')
string2 = input().split(' ')
string3 = input().split(' ')

first_player_won = False
second_player_won = False
its_draw = False

if string1[0] == string1[1] == string1[2]:
    if '1' in string1:
        first_player_won = True
    elif '2' in string1:
        second_player_won = True
    else:
        its_draw = True

elif string2[0] == string2[1] == string2[2]:
    if '1' in string2:
        first_player_won = True
    elif '2' in string2:
        second_player_won = True
    else:
        its_draw = True

elif string3[0] == string3[1] == string3[2]:
    if '1' in string3:
        first_player_won = True
    elif '2' in string3:
        second_player_won = True
    else:
        its_draw = True

elif string1[0] == string2[0] == string3[0]:
    if string1[0] == '1':
        first_player_won = True
    elif string1[0] == '2':
        second_player_won = True
    else:
        its_draw = True

elif string1[1] == string2[1] == string3[1]:
    if string1[1] == '1':
        first_player_won = True
    elif string1[1] == '2':
        second_player_won = True
    else:
        its_draw = True

elif string1[2] == string2[2] == string3[2]:
    if string1[2] == '1':
        first_player_won = True
    elif string1[2] == '2':
        second_player_won = True
    else:
        its_draw = True


elif string1[0] == string2[1] == string3[2]:
    if string1[0] == '1':
        first_player_won = True
    elif string1[0] == '2':
        second_player_won = True
    else:
        its_draw = True

elif string1[2] == string2[1] == string3[0]:
    if string1[2] == '1':
        first_player_won = True
    elif string1[2] == '2':
        second_player_won = True
    else:
        its_draw = True

else:
    its_draw = True

if first_player_won:
    print("First player won")

elif second_player_won:
    print("Second player won")

elif its_draw:
    print("Draw!")