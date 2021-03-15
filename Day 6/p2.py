inputFile = open("Day 6\\input.txt", "r")
input = inputFile.readlines()
inputFile.close()

groupAnswers = ""
groups = list()

for line in input:
    if line.strip() == "":
        groups.append(groupAnswers)
        groupAnswers = ""
    else:
        groupAnswers += line

groups.append(groupAnswers)

commonAnswers = list()

for group in groups:
    people = [set(person) for person in group.splitlines()]
    commonAnswers.append(set.intersection(*people))

print(sum([len(answers) for answers in commonAnswers]))