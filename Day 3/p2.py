from functools import reduce

inputFile = open("Day 3\input.txt", "r")
input = inputFile.read().splitlines()
inputFile.close()

slopeMap = list(map(lambda x: list(x), input))

trajectories = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

treeCounts = list()
width = len(slopeMap[0])

for traj in trajectories:
    rightStep = traj[0]
    downStep = traj[1]
    right = 0
    treeCount = 0

    for down in range(0, len(slopeMap), downStep):
        itemAtLocation = slopeMap[down][right]

        if itemAtLocation == "#":
            treeCount += 1

        right = (right + rightStep) % width
    
    treeCounts.append(treeCount)

finalTreeCount = reduce(lambda x, y: x * y, treeCounts)
print(finalTreeCount)