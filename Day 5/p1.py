inputFile = open("Day 5\\input.txt", "r")
input = inputFile.read().splitlines()
inputFile.close()

numRows = 128
numColumns = 8
seatIds = list()

for seatPos in input:
    rowSpecifier = seatPos[0:7]
    columnSpecifier = seatPos[7:10]

    rowStep = numRows / 2
    minRow = 0
    maxRow = numRows - 1

    for rowChar in rowSpecifier:
        if rowChar == "F":
            maxRow -= rowStep
        elif rowChar == "B":
            minRow += rowStep
        rowStep /= 2

    colStep = numColumns / 2
    minCol = 0
    maxCol = numColumns - 1

    for colChar in columnSpecifier:
        if colChar == "L":
            maxCol -= colStep
        elif colChar == "R":
            minCol += colStep
        colStep /= 2

    seatId = (minRow * 8) + minCol

    print(f"Input: {seatPos} Row: {rowSpecifier} {minRow}-{maxRow} Col: {columnSpecifier} {minCol}-{maxCol} Id: {seatId}")
    
    seatIds.append(seatId)

print(max(seatIds))