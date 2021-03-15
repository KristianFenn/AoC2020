import re

input_file = open("Day 2\\input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

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

print(len(valid_passwords))
