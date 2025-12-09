# Read in the grid, exploding the lines into character arrays

with open("data/day04.txt") as file:
    grid = [ [*line] for line in file.read().splitlines() ]

# Function to print a grid

def print_grid(grid):
    for line in grid:
        print("".join(line))
    print()

# Function to pad the grid

def pad_grid(grid):
    grid_height = len(grid)
    grid_width = len(grid[0])

    out_grid = [ [ "." for _ in range(0, grid_width +2) ] for _ in range(0, grid_height +2) ]

    for y in range(0, grid_height):
        for x in range(0, grid_width):
            out_grid[y+1][x+1] = grid[y][x]

    return out_grid

grid = pad_grid(grid) # removes the need to constantly check the edges

# Function to count neighbours

NEIGHBOURS = [
    (-1, -1), (+0, -1), (+1, -1),
    (-1, +0),           (+1, +0),
    (-1, +1), (+0, +1), (+1, +1),
]

def count_neighbours(pos_x, pos_y, grid):
    neighbours = [ '@' == grid[ pos_y + y ][ pos_x + x ] for (x, y) in NEIGHBOURS ]
    # print(neighbours)
    return sum(neighbours)

# Function to collect movable rolls

def get_movable(grid):
    movable_rolls = []

    grid_height = len(grid)
    grid_width = len(grid[0])

    for y in range(0, grid_height):
        for x in range(0, grid_width):
            if grid[y][x] == '@' and count_neighbours(x, y, grid) < 4:
                movable_rolls.append((x,y))

    return movable_rolls

# Function to remove movable rolls from a grid

def remove_moveable(moveable, grid):
    grid_height = len(grid)
    grid_width = len(grid[0])

    for y in range(0, grid_height):
        for x in range(0, grid_width):
            if (x,y) in moveable:
                grid[y][x] = '.'

    # print(f"Removed {len(moveable)} rolls")

    return grid

# Function to move rolls until we can roll no more

def move_rolls(grid):

    total_moveable = 0
    move = [ 1 ] # seed value to kick off the loop

    # print_grid(grid)
    while len(move) != 0:
        move = get_movable(grid)
        total_moveable += len(move)
        grid = remove_moveable(move, grid)
        # print_grid(grid)

    return total_moveable

# Output

print("Part one = ", len(get_movable(grid)))
print("Part two = ", move_rolls(grid))
