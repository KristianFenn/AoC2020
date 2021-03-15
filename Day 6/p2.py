input_file = open("Day 6\\input.txt", "r")
input = input_file.readlines()
input_file.close()

group_answers = ""
groups = []

for line in input:
    if line.strip() == "":
        groups.append(group_answers)
        group_answers = ""
    else:
        group_answers += line

groups.append(group_answers)

common_answers = []

for group in groups:
    people = [set(person) for person in group.splitlines()]
    common_answers.append(set.intersection(*people))

print(sum([len(answers) for answers in common_answers]))
