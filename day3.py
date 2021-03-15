from functools import reduce

def part_1(input):
    slope_map = [list(x) for x in input]

    tree_count = 0
    right = 0
    width = len(slope_map[0])

    for down in range(0, len(slope_map)):
        item_at_location = slope_map[down][right]
        if item_at_location == "#":
            tree_count += 1

        right = (right + 3) % width

    return tree_count

def part_2(input):
    slope_map = [list(x) for x in input]

    trajectories = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    tree_counts = []
    width = len(slope_map[0])

    for traj in trajectories:
        right_step,down_step = traj
        right = 0
        tree_count = 0

        for down in range(0, len(slope_map), down_step):
            item_at_location = slope_map[down][right]

            if item_at_location == "#":
                tree_count += 1

            right = (right + right_step) % width
        
        tree_counts.append(tree_count)

    return reduce(lambda x, y: x * y, tree_counts)
