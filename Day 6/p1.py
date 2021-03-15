input_file = open("Day 6\\input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

group_answers = ""
groups = []

for line in input:
    if line == "":
        groups.append(group_answers)
        group_answers = ""
    else:
        group_answers += line

groups.append(group_answers)

answers_per_group = [len(set(group)) for group in groups]

print(sum(answers_per_group))
