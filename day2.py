import re

def part_1(input):
    valid_passwords = []
    invalid_passwords = []

    for line in input:
        split = re.split(r"-| |: ", line)

        min_occurance = int(split[0])
        max_occurance = int(split[1])
        expected_letter = split[2]
        password = split[3]
        occurances = len([char for char in password if char == expected_letter])

        if occurances >= min_occurance and occurances <= max_occurance:
            valid_passwords.append(password)
        else:
            invalid_passwords.append(password)

    return len(valid_passwords)

def part_2(input):
    valid_passwords = []
    invalid_passwords = []

    for line in input:
        split = re.split(r"-| |: ", line)
        
        first_index = int(split[0]) - 1
        second_index = int(split[1]) - 1
        expected_letter = split[2]
        password = split[3]

        expected_char_at_first_index = password[first_index] == expected_letter
        expected_char_at_second_index = password[second_index] == expected_letter

        if expected_char_at_first_index and expected_char_at_second_index:
            invalid_passwords.append(password)
        elif expected_char_at_first_index or expected_char_at_second_index:
            valid_passwords.append(password)
        else:
            invalid_passwords.append(password)

    return len(valid_passwords)
