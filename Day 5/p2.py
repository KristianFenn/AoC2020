input_file = open("Day 5\\input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

now_rows = 128
num_cols = 8
seat_ids = []

for seat_pos in input:
    row_spec = seat_pos[0:7]
    col_spec = seat_pos[7:10]

    row_step = now_rows / 2
    row_min = 0
    row_max = now_rows - 1

    for rowChar in row_spec:
        if rowChar == "F":
            row_max -= row_step
        elif rowChar == "B":
            row_min += row_step
        row_step /= 2

    colStep = num_cols / 2
    minCol = 0
    maxCol = num_cols - 1

    for colChar in col_spec:
        if colChar == "L":
            maxCol -= colStep
        elif colChar == "R":
            minCol += colStep
        colStep /= 2

    seat_id = (row_min * 8) + minCol

    print(f"Input: {seat_pos} Row: {row_spec} {row_min}-{row_max} Col: {col_spec} {minCol}-{maxCol} Id: {seat_id}")
    
    seat_ids.append(int(seat_id))

for seat_id in range(min(seat_ids), max(seat_ids)):
    if seat_id not in seat_ids:
        print(seat_id)
        break