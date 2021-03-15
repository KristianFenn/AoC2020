import re

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

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def validate_year(val: str, min: int, max: int):
    if (is_int(val)):
        year_val = int(val)
        return year_val >= min and year_val <= max
    return False

def validate_height(val: str):
    height_parsed = re.match(r"^([0-9]{2,3})(cm|in)$", val)

    if height_parsed is None:
        return False

    height_val = int(height_parsed.group(1))
    height_type = height_parsed.group(2)

    if height_type == "cm":
        return height_val >= 150 and height_val <= 193
    elif height_type == "in":
        return height_val >= 59 and height_val <= 76

valid_eye_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

validators = {
    "byr": lambda byr: validate_year(byr, 1920, 2002),
    "iyr": lambda iyr: validate_year(iyr, 2010, 2020),
    "eyr": lambda eyr: validate_year(eyr, 2020, 2030),
    "hgt": lambda hgt: validate_height(hgt),
    "hcl": lambda hcl: re.match(r"^#[0-9a-f]{6}$", hcl) is not None,
    "ecl": lambda ecl: ecl in valid_eye_colours,
    "pid": lambda pid: re.match(r"^[0-9]{9}$", pid),
    "cid": lambda cid: True,
}

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for passport in passports:
    passport_fields = passport.split()
    passport_invalid_fields = required_fields.copy()

    for field in passport_fields:
        field_name,field_val = field.split(":")
        isValid = validators[field_name](field_val)
        
        if isValid and field_name in passport_invalid_fields:
            passport_invalid_fields.remove(field_name)
    
    if len(passport_invalid_fields) == 0:
        valid_passports.append(passport)
    else:
        invalid_passports.append(f"{passport} Invalid fields: {passport_invalid_fields}")

print(len(valid_passports))