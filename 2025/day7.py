with open("data/day7.txt") as file:
    space = [ [ _ for _ in line ] for line in file.read().splitlines() ]

# Function to print the space

def print_space(space):
    for line in space:
        print(line)
    print()

# Swap out the S, so we aren't having to check for another thing

space[0][space[0].index("S")] = "|"

# Part one

collisions = 0

for y in range(1, len(space)):
    for x in range(len(space[0])):
        above = space[y-1][x]

        if above == "|":
            if space[y][x] == ".":
                space[y][x] = "|"
            if space[y][x] == "^":
                space[y][x-1] = "|"
                space[y][x+1] = "|"
                collisions += 1

# print_space(space)

print("Part one =", collisions)

# Part two

y = len(space) -1
for x in range(len(space[-1])):
    if space[y][x] == "|":
        space[y][x] = 1

for y in range(len(space)-2, -1, -1):
    for x in range(len(space[0])):
        if space[y][x] == "|":
            space[y][x] = space[y+1][x]
    for x in range(len(space[0])):
        if space[y][x] == "^":
            space[y][x] = space[y][x-1] + space[y][x+1]

# print_space(space)

print("Part two =", "".join(map(str, space[0])).replace(".", ""))
