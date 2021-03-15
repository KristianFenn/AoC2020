from itertools import permutations
from functools import reduce

def part_1(input: str):
    input = [int(x) for x in input]

    for num_1_index in range(0, len(input)):
        for num_2_index in range(num_1_index + 1, len(input)):
            num_1 = input[num_1_index]
            num_2 = input[num_2_index]
            if (num_1 + num_2 == 2020):
                return num_1 * num_2

def part_2(input):
    input = [int(x) for x in input]

    for num_1_index in range(0, len(input)):
        for num_2_index in range(num_1_index + 1, len(input)):
            for num_3_index in range(num_2_index + 1, len(input)):
                num_1 = input[num_1_index]
                num_2 = input[num_2_index]
                num_3 = input[num_3_index]
                if (num_1 + num_2 + num_3 == 2020):
                    return num_1 * num_2 * num_3

def day_1_fancy(input: str, premutation_size: int):
    input = [int(x) for x in input]
    val = next(val for val in permutations(input, premutation_size) if sum(val) == 2020)
    return reduce(lambda x, y: x * y, val)