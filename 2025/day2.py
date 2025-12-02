with open("data/day2.txt") as file:
    ranges = [ tuple(map(int, line.split("-"))) for line in file.read().split(",") ]

import re # a cheap solution, I'm sorry!

def part_one(number):
    return re.findall(r'^(\w+)\1$', number) != []

def part_two(number):
    return re.findall(r'^(\w+)\1+$', number) != []

part_one_total = 0
part_two_total = 0

for r in ranges:
    for n in range(r[0], r[1] +1):
        if part_two(str(n)):
            part_two_total += n
            if part_one(str(n)):
                part_one_total += n


print("Part one = ", part_one_total)
print("Part two = ", part_two_total)

# Make them ugly?

# print("Part one = ", sum([sum([ n if re.findall(r'^(\w+)\1$',  str(n)) != [] else 0 for n in range(r[0], r[1] +1)]) for r in ranges]))
# print("Part two = ", sum([sum([ n if re.findall(r'^(\w+)\1+$', str(n)) != [] else 0 for n in range(r[0], r[1] +1)]) for r in ranges]))
