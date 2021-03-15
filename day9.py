from itertools import permutations

def part_1(input, preamble_len):
    input = [int(x) for x in input]
    idx = 0

    while True:
        preamble = input[idx:idx + preamble_len]
        value = input[idx + preamble_len]

        valid = False

        for permutation in permutations(preamble, 2):
            if sum(permutation) == value:
                valid = True
                break
        
        if not valid:
            return value

        idx += 1

def part_2(input, preamble_len):
    invalid_value = part_1(input, preamble_len)
    
    input = [int(x) for x in input]

    found_value = False
    acc = []

    for idx in range(0, len(input) - preamble_len):
        acc = []
        acc_vals = 1
        while True:
            acc = input[idx:idx + acc_vals]
            acc_sum = sum(acc)

            if acc_sum > invalid_value:
                break
            elif (acc_sum == invalid_value):
                found_value = True
                break

            acc_vals += 1  

        if found_value:
            break

    return min(acc) + max(acc)
