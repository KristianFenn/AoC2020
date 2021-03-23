
def day_15(input, x_number_spoken):
    last_spoken = {}
    current = 0

    for idx,val in enumerate(input[:-1]):
        last_spoken[val] = idx
    current = input[-1]

    for idx in range(len(input) - 1, x_number_spoken - 1):
        if current in last_spoken:
            diff_to_last_said = idx - last_spoken[current]
            last_spoken[current] = idx
            current = diff_to_last_said
        else:
            last_spoken[current] = idx
            current = 0
    
    return current
