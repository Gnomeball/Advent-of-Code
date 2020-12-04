with open("day4.txt") as file:
    lines = file.read().splitlines()

passports = []

i = 0
while i < len(lines):
    passport = []
    try:
        while lines[i] != "":
            passport.append(lines[i])
            i += 1
    except IndexError:
        passport = " ".join(passport)
        passports.append(passport)
        break
    passport = " ".join(passport)
    passports.append(passport)
    i += 1

# Part 1

valid = [p for p in passports if "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p and "hcl" in p and "ecl" in p and "pid" in p]

print(len(passports))
print(len(valid))

# Part 2

valid = [[f.split(":") for f in o] for o in [sorted([word for word in v.split()]) for v in valid]]

keyed = []

for v in valid:
    keys = {}
    [keys.update({k[0]: k[1]}) for k in v]
    keyed.append(keys)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.

valid = [v for v in keyed if 1920 <= int(v["byr"]) <= 2002 and 2010 <= int(v["iyr"]) <= 2020 and 2020 <= int(v["eyr"]) <= 2030]

# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.

valid = [v for v in valid if ("cm" in v["hgt"] and 150 <= int(v["hgt"][:-2]) <= 193) or ("in" in v["hgt"] and 59 <= int(v["hgt"][:-2]) <= 76)]

# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.

valid = [v for v in valid if "#" in v["hcl"] and (len(v["hcl"]) == 7)]

# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.

valid = [v for v in valid if v["ecl"] in "amb blu brn gry grn hzl oth" and len(v["pid"]) == 9]

# cid (Country ID) - ignored, missing or not.

print(len(valid))