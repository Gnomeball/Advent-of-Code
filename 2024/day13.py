# Read in the input file

import re

with open('data/day13.txt') as file:
    machines = [ [ tuple(map(int, re.findall('\\d+', line))) for line in machine_raw ] for machine_raw in [ machine.split("\n") for machine in file.read().split("\n\n") ] ]

# Do the maths!

def do_the_maths(machines, offset = 0):
    total = 0
    for machine in machines:
        (ax, ay), (bx, by), (px, py) = machine

        if offset:
            px += offset
            py += offset

        # Worked out on pen and paper

        J = (ax*py - ay*px) / (ax*by - ay*bx)
        I = ((by-bx)*J -py +px) / (ax-ay)

        if I.is_integer() and J.is_integer():
            total +=  I*3 + J

    return int(total)

part_one = do_the_maths(machines)

print(f"Part one: {part_one}")

part_two = do_the_maths(machines, 10000000000000)

print(f"Part two: {part_two}")
