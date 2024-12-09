# Read in the file, by line

with open("data/day06.txt") as file:
    grid = { i+j*1j : cell for i,line in enumerate(file) for j,cell in enumerate(line.strip()) }

# Function to move the guard

def move_guard(grid):

    guard = min(p for p in grid if grid[p] == "^")

    # Multiplying this by -1j repeatedly will rotate the guard "clockwise"
    current_dir = complex(-1, 0)

    # List to store all previously seen locations for the guard
    seen = []
    loop = False

    # While the guard is still in the grid
    while guard in grid and not loop:
        if (guard, current_dir) in seen:
            loop = True
        #Add this location
        seen.append((guard, current_dir))
        # Try to move the guard
        if grid.get(guard + current_dir) == "#":
            # If wall, rotate
            current_dir *= -1j
        else:
            # Else, move
            guard += current_dir

    return seen, loop

path, loop = move_guard(grid)

uniq_path = set([ p for p,_ in path ])

# Part one: length of the unique points in the seen path

print(f"Part one: {len(uniq_path)}")

# Part two: hmm

guard = min(p for p in grid if grid[p] == "^")

loops = 0

for p in uniq_path:
    if p == guard:
        # print("skip")
        next
    else:
        # make that point a wall
        # print(p)
        grid_copy = grid.copy()
        grid_copy.update({p: "#"})
        # print(grid_copy)
        # check if we find a loop
        path, loop = move_guard(grid_copy)
        # print(loop)
        if loop:
            loops += 1
            # print(loops)

print(f"Part two: {loops}")
