inputFile = open("Day 3\input.txt", "r")
input = inputFile.read().splitlines()
inputFile.close()

slopeMap = list(map(lambda x: list(x), input))

treeCount = 0
right = 0
width = len(slopeMap[0])

for down in range(0, len(slopeMap)):
    itemAtLocation = slopeMap[down][right]
    if itemAtLocation == "#":
        treeCount += 1

    right = (right + 3) % width

print (treeCount)