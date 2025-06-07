string = input()
count_of_beggars = int(input())

money_list = string.split(', ')
money_int_list = []

beggars_money_list = []

for i in money_list:
    money_int_list.append(int(i))

for current_beggar in range(count_of_beggars):
    current_beggar_sum = 0

    for summ in range(current_beggar, len(money_int_list), count_of_beggars ):
        current_beggar_sum += money_int_list[summ]

    beggars_money_list.append(current_beggar_sum)

print(beggars_money_list)



