import re

inputFile = open("Day 2\input.txt", "r")
input = inputFile.read().splitlines()
inputFile.close()

validPasswords = list()
invalidPasswords = list()

for line in input:
    split = re.split(r"-| |: ", line)
    
    firstIndex = int(split[0]) - 1
    secondIndex = int(split[1]) - 1
    expectedLetter = split[2]
    password = split[3]

    expectedCharAtFirstIndex = password[firstIndex] == expectedLetter
    expectedCharAtSecondIndex = password[secondIndex] == expectedLetter

    if (expectedCharAtFirstIndex and expectedCharAtSecondIndex):
        invalidPasswords.append(password)
    elif (expectedCharAtFirstIndex or expectedCharAtSecondIndex):
        validPasswords.append(password)
    else:
        invalidPasswords.append(password)

print(len(validPasswords))