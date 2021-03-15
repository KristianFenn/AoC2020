input_file = open("Day 5\\input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

num_rows = 128
num_cols = 8
seat_ids = []

for seat_pos in input:
    row_spec = seat_pos[0:7]
    col_spec = seat_pos[7:10]

    row_step = num_rows / 2
    row_min = 0
    row_max = num_rows - 1

    for row_char in row_spec:
        if row_char == "F":
            row_max -= row_step
        elif row_char == "B":
            row_min += row_step
        row_step /= 2

    col_step = num_cols / 2
    col_min = 0
    col_max = num_cols - 1

    for col_char in col_spec:
        if col_char == "L":
            col_max -= col_step
        elif col_char == "R":
            col_min += col_step
        col_step /= 2

    seat_id = int((row_min * 8) + col_min)
    
    seat_ids.append(seat_id)

print(max(seat_ids))
