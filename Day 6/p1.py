inputFile = open("Day 6\\input.txt", "r")
input = inputFile.read().splitlines()
inputFile.close()

groupAnswers = ""
groups = list()

for line in input:
    if line == "":
        groups.append(groupAnswers)
        groupAnswers = ""
    else:
        groupAnswers += line

groups.append(groupAnswers)

answersPerGroup = list(map(lambda group: len(set(group)), groups))

print(sum(answersPerGroup))