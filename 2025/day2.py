with open("data/day2.txt") as file:
    ranges = [ tuple(map(int, line.split("-"))) for line in file.read().split(",") ]
    all_ids = [ str(n) for r in ranges for n in tuple(range(r[0], r[1] +1)) ]

import re # a cheap solution, I'm sorry!

def part_one(number):
    return re.findall(r'^(\w+)\1$', number) != []

def part_two(number):
    return re.findall(r'^(\w+)\1+$', number) != []

part_one_total = 0
part_two_total = 0

for n in all_ids:
    if part_two(n):
        part_two_total += int(n)
        if part_one(n):
            part_one_total += int(n)

print("Part one = ", part_one_total)
print("Part two = ", part_two_total)

# Make them ugly?

# print("Part one = ", sum([ int(s) if re.findall(r'^(\w+)\1$',  str(s)) != [] else 0 for s in all_ids ]) )
# print("Part two = ", sum([ int(s) if re.findall(r'^(\w+)\1+$', str(s)) != [] else 0 for s in all_ids ]) )
