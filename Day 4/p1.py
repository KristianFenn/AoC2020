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

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for passport in passports:
    passportFields = passport.split()
    passportRequiredFields = requiredFields.copy()

    for field in passportFields:
        fieldName = field.split(":")[0]
        if fieldName in passportRequiredFields:
            passportRequiredFields.remove(fieldName)
    
    if len(passportRequiredFields) == 0:
        validPassports.append(passport)
    else:
        invalidPassports.append(f"{passport} Missing fields: {passportRequiredFields}")

print(len(validPassports))