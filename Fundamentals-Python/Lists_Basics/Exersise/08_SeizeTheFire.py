fire_cell_list = input().split('#')
total_water = int(input())

total_effort = 0
total_fire = 0
cells_put_out = []

for fire_cell in fire_cell_list:

    current_fire  = fire_cell.split(" = ")
    type_of_fyre = current_fire[0]
    value_of_fyre = int(current_fire[1])
    effort = value_of_fyre * 0.25

    if (((type_of_fyre == "High") and (81 <= value_of_fyre <= 125) and (total_water >= value_of_fyre))
            or ((type_of_fyre == "Medium") and (51 <= value_of_fyre <= 80) and (total_water >= value_of_fyre))
            or ((type_of_fyre == "Low") and (1 <= value_of_fyre <= 50) and (total_water >= value_of_fyre))):
        total_water -= value_of_fyre
        total_fire += value_of_fyre
        total_effort += effort
        cells_put_out.append(value_of_fyre)

print("Cells:")

for cell in cells_put_out:
    print(f" - {cell}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
