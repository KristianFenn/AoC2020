input_file = open("Day 4\\input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

current_passport = ""
passports = []
valid_passports = []
invalid_passports = []

for line in input:
    if line == "":
        passports.append(current_passport.strip())
        current_passport = ""
    else:
        current_passport += f"{line} "

passports.append(current_passport)

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for passport in passports:
    passport_fields = passport.split()
    passport_required_fields = required_fields.copy()

    for field in passport_fields:
        field_name = field.split(":")[0]
        if field_name in passport_required_fields:
            passport_required_fields.remove(field_name)
    
    if len(passport_required_fields) == 0:
        valid_passports.append(passport)
    else:
        invalid_passports.append(f"{passport} Missing fields: {passport_required_fields}")

print(len(valid_passports))
