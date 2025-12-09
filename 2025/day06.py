from functools import reduce

# Boilerplate

def add(x, y): return x + y

def mult(x, y): return x * y

# Function to transpose a grid

def transpose(grid):
    grid_height = len(grid)
    grid_width = max(len(grid[x]) for x in range(grid_height))

    out_grid = [ [ "." for _ in range(0, grid_height) ] for _ in range(0, grid_width) ]

    for y in range(0, grid_height):
        for x in range(0, grid_width):
            try:
                out_grid[x][y] = grid[y][x]
            except:
                IndexError
                out_grid[x][y] = ' '

    return out_grid



with open("data/day06.txt") as file:
    # Part two - I can't be fucked working out how to pull these together lol
    grid = file.read().splitlines()
    # print(grid)

    operators = grid.pop().split()

    # Part one
    grid_by_lines = transpose([ line.split() for line in grid ])
    # print(grid_by_lines)

    # Part two - again
    grid = transpose(grid)

    print("Part one = ", sum(reduce(mult if operators[i] == '*' else add, list(map(int, grid_by_lines[i]))) for i in range(len(operators))))

    numbers = [ list(map(int, item.split('-'))) for item in '-'.join( ''.join(n).strip() for n in grid ).split('--') ]
    print("Part two = ", sum(reduce(mult if operators[i] == '*' else add, list(map(int,       numbers[i]))) for i in range(len(operators))))

# Part one

# cephalopod_maths_is_strange = 0

# for i in range(len(operators)):
#     op = operators[i]
#     numbers = list(map(int, grid_by_lines[i]))
#     cephalopod_maths_is_strange += reduce(mult if op == '*' else add, numbers)

# print("Part one = ", cephalopod_maths_is_strange)

# Part two

# numbers = []
# line = []

# for chars in grid:
#     number_maybe = ''.join(chars).strip()
#     if number_maybe != "":
#         line.append(int(number_maybe))
#     else:
#         numbers.append(line)
#         line = []

# numbers.append(line)

# cephalopod_maths_is_strange = sum(reduce(mult if operators[i] == '*' else add, numbers[i]) for i in range(len(operators)))

# print("Part two = ", cephalopod_maths_is_strange)
