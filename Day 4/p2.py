import re

inputFile = open("Day 4\\input.txt", "r")
input = inputFile.read().splitlines()
inputFile.close()

currentPassport = ""
passports = list()
validPassports = list()
invalidPassports = list()

for line in input:
    if line == "":
        passports.append(currentPassport.strip())
        currentPassport = ""
    else:
        currentPassport += f"{line} "

passports.append(currentPassport)

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def validate_year(val: str, min: int, max: int):
    if (is_int(val)):
        yearVal = int(val)
        return yearVal >= min and yearVal <= max
    return False

def validate_height(val: str):
    heightParsed = re.match(r"^([0-9]{2,3})(cm|in)$", val)

    if heightParsed is None:
        return False

    heightVal = int(heightParsed.group(1))
    heightType = heightParsed.group(2)

    if heightType == "cm":
        return heightVal >= 150 and heightVal <= 193
    elif heightType == "in":
        return heightVal >= 59 and heightVal <= 76

validEyeColours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

validators = {
    "byr": lambda byr: validate_year(byr, 1920, 2002),
    "iyr": lambda iyr: validate_year(iyr, 2010, 2020),
    "eyr": lambda eyr: validate_year(eyr, 2020, 2030),
    "hgt": lambda hgt: validate_height(hgt),
    "hcl": lambda hcl: re.match(r"^#[0-9a-f]{6}$", hcl) is not None,
    "ecl": lambda ecl: ecl in validEyeColours,
    "pid": lambda pid: re.match(r"^[0-9]{9}$", pid),
    "cid": lambda cid: True,
}

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for passport in passports:
    passportFields = passport.split()
    passportInvalidFields = requiredFields.copy()

    for field in passportFields:
        fieldSplit = field.split(":")
        fieldName = fieldSplit[0]
        fieldVal = fieldSplit[1]
        
        isValid = validators[fieldName](fieldVal)
        if isValid and fieldName in passportInvalidFields:
            passportInvalidFields.remove(fieldName)
    
    if len(passportInvalidFields) == 0:
        validPassports.append(passport)
    else:
        invalidPassports.append(f"{passport} Invalid fields: {passportInvalidFields}")

print(len(validPassports))