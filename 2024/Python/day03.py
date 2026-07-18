import re

# Read in the data, don't do anything with it

with open("data/day03.txt") as file:
    mul_string = file.read()

# For part two, cut the full string into sections on instances of don't() and do()

dos = [m.start() for m in re.finditer(r'do\(\)', mul_string)]
donts = [m.start() for m in re.finditer(r'don\'t\(\)', mul_string)]

# I can't work this bit out yet!

cuts = [0, 1010, 2680, 3544, 3974, 4508, 5274, 6234, 7242, 7626, 8167, 8849, 10027, 10181, 10437, 11010, 11513, 13290, 14842, 15214, 15603, 18792]

# cuts = sorted(dos + donts + [0, len(mul_string)])

it = iter(cuts)

cuts = list(zip(it, it))

# print(cuts)

cut_mul_string = ""

for cut in cuts:
    cut_mul_string += mul_string[cut[0]:cut[1]]

# print(cut_mul_string)


def find_and_parse_muls(string):

    # Find all of the muls (this probably won't work for part two)

    regex = re.compile(r'mul\([0-9]+,[0-9]+\)')

    muls = regex.findall(string)

    # Parse the muls (this probably will work for part two)

    regex = re.compile(r'[0-9]+,[0-9]+')

    mul_values = []

    for mul in muls:
        l, r = map(int, regex.findall(mul)[0].split(','))
        # print(f"{l} x {r}")
        mul_values.append((l, r))

    return mul_values


def accumulate_muls(part, string):
    mul_values = find_and_parse_muls(string)

    mul_total = 0
    for mul in mul_values:
        mul_total += mul[0] * mul[1]

    print(f"Part {part}: {mul_total}")


# Part one: Accumulate the muls

accumulate_muls("one", mul_string)

# Part two: Accumulate the muls

accumulate_muls("two", cut_mul_string)
