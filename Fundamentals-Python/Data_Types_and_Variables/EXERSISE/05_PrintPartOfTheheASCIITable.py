start_index = int(input())
end_index = int(input())

for index in range(start_index, end_index + 1):

    if index == end_index:
        print(f"{chr(index)}")
    else:
        print(f"{chr(index)}", end=" ")