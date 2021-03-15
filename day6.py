def part_1(input):
    group_answers = []
    groups = []

    for line in input:
        if line == "":
            groups.append(group_answers)
            group_answers = []
        else:
            group_answers.append(line)

    groups.append(group_answers)

    answers_per_group = [len(set(str.join("", group))) for group in groups]

    return sum(answers_per_group)

def part_2(input):
    group_answers = []
    groups = []

    for line in input:
        if line == "":
            groups.append(group_answers)
            group_answers = []
        else:
            group_answers.append(line)

    groups.append(group_answers)

    common_answers = []

    for group in groups:
        people = [set(person) for person in group]
        common_answers.append(set.intersection(*people))

    return sum([len(answers) for answers in common_answers])
