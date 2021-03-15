input_file = open("Day 3\input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

slope_map = [list(x) for x in input]

tree_count = 0
right = 0
width = len(slope_map[0])

for down in range(0, len(slope_map)):
    item_at_location = slope_map[down][right]
    if item_at_location == "#":
        tree_count += 1

    right = (right + 3) % width

print (tree_count)