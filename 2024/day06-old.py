# Read in the file, by line

with open("data/day06.txt") as file:
    grid = [ [*line] for line in file.read().splitlines()]

# Function to print a grid

def print_grid(grid):
    for line in grid:
        print("".join(line))
    print()

# Function to rotate a grid 90° anticlockwise

def rotate_grid(grid):
    grid_out = []
    # rotate the first row
    first_row = grid[0]
    for char in first_row:
        grid_out.append([char])
    # rotate the rest of the grid
    for index in range(1, len(grid[0])):
        line = grid[index]
        for index in range(0, len(line)):
            char = line[index]
            grid_out[index] += char
    return list(reversed(grid_out))

# Function to find the guard

def find_guard(grid):
    guard = (0, 0)

    for line in grid:
        for cell in line:
            if cell == "^":
                guard = (grid.index(line), line.index(cell))

    return guard

# Function to move the guard

def move_guard(grid, guard):
    x, y = guard
    if grid[x-1][y] == "#":
        grid = rotate_grid(grid)
    else:
        grid[x-1][y] = "^"
        grid[x][y] = "X"
    return grid, find_guard(grid)

# Find the guard

guard = (0, 0)

for line in grid:
    for cell in line:
        if cell == "^":
            guard = (grid.index(line), line.index(cell))

# print(guard)

# print_grid(grid)

x, y = guard

while x != 0:
    grid, guard = move_guard(grid, guard)
    # print_grid(grid)
    x, y = guard

print_grid(grid)

# Part one; count the X's

count = 1 # the guard

for line in grid:
    for cell in line:
        if cell == "X":
            count += 1

print(f"Part one: {count}")

# print(grid)
# grid = rotate_grid(grid)
# print(grid)
# grid = rotate_grid(grid)
# print(grid)
# grid = rotate_grid(grid)
# print(grid)
