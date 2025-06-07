numbers_list = input().split(" ")
step = int(input())

killing_order = []
final_list = []
starting_idx = 0

while numbers_list:
    current_idx = (starting_idx + step - 1) % len(numbers_list)

    killing_order.append(numbers_list.pop(current_idx))
    starting_idx = current_idx

final_list = "[" + ",".join(killing_order) + "]"

print(final_list)