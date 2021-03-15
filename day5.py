def part_1(input):
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

    return max(seat_ids)

def part_2(input):
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
        
        seat_ids.append(int(seat_id))

    for seat_id in range(min(seat_ids), max(seat_ids)):
        if seat_id not in seat_ids:
            return seat_id
