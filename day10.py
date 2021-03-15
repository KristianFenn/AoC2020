def part_1(input):
    input = [int(x) for x in input]
    input.append(0)
    input.append(max(input) + 3)
    input.sort()

    differences = [second - first for first, second in zip(input[:-1], input[1:])]

    return len([x for x in differences if x == 1]) * len([x for x in differences if x == 3])

def part_2(input):
    input = [int(x) for x in input]
    input.append(0)
    input.append(max(input) + 3)
    input.sort()

    paths_to_end = [0 for x in input]
    last_index = len(input) - 1
    paths_to_end[last_index] = 1
    lookahead_size = 3

    for root_idx, root_value in reversed(list(enumerate(input[:-1]))):
        # this guff just calculates the window of values we could potentially get to from the value at the current index.
        # we start at the current index, because then enumerate helpfully gives us the offset from the current index to the lookahead value.
        lookahead_end = min(root_idx + lookahead_size, last_index) + 1
        lookahead = [(root_idx + offset, value) for offset, value in enumerate(input[root_idx:lookahead_end])]

        # find all the indexes from the values in the lookahead that we can potentially reach.
        # discard the current node from the lookahead, as we can't traverse to ourselves.
        indexes_reachable_from_root = [idx for idx, value in lookahead[1:] if value - root_value <= 3]

        # the possible paths to the end are just the sum of all the paths to the end for the nodes we can reach.
        paths_to_end[root_idx] = sum(paths_to_end[idx] for idx in indexes_reachable_from_root)

    return paths_to_end[0]

