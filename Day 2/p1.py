import re

inputFile = open("Day 2\input.txt", "r")
input = inputFile.read().splitlines()
inputFile.close()

validPasswords = list()
invalidPasswords = list()

for line in input:
    split = re.split(r"-| |: ", line)
    
    minOccurance = int(split[0])
    maxOccurance = int(split[1])
    expectedLetter = split[2]
    password = split[3]
    occurances = list(filter(lambda x: x == expectedLetter, password))

    if len(occurances) >= minOccurance and len(occurances) <= maxOccurance:
        validPasswords.append(password)
    else:
        invalidPasswords.append(password)

print(len(validPasswords))