times = input().split(' ')

left_car_times = []
right_car_times = []
left_car_total_time = 0
right_car_total_time = 0

half_times = len(times) // 2

for i in range(half_times):
    left_car_times.append(times[i])

for x in range(-1, -half_times - 1, -1):
    right_car_times.append(times[x])

for left_time in left_car_times:
    if left_time == '0':
        left_car_total_time = left_car_total_time * 0.8
    else:
        left_car_total_time += int(left_time)

for right_time in right_car_times:
    if right_time == '0':
        right_car_total_time = right_car_total_time * 0.8
    else:
        right_car_total_time += int(right_time)

if left_car_total_time < right_car_total_time:
    print(f"The winner is left with total time: {left_car_total_time:.1f}")

elif right_car_total_time < left_car_total_time:
    print(f"The winner is right with total time: {right_car_total_time:.1f}")

