# Read in the file, by line

with open("data/day04.txt") as file:
    wordsearch = file.read().splitlines()

# Function to flip a grid diagonally

def flip_grid(grid):
    grid_out = []
    # flip the first row
    first_row = grid[0]
    for char in first_row:
        grid_out.append(str(char))
    # flip the rest of the grid
    for index in range(1, len(grid[0])):
        line = grid[index]
        for index in range(0, len(line)):
            char = line[index]
            grid_out[index] += char
    return list(reversed(grid_out))

# Function to read a grid diagonally (funky)

def rotate_grid(grid):
    grid_out = []

    grid_size = len(grid) + len(grid[0]) - 1

    for index in range(0, grid_size):
        points = []
        for p in range(0, index+1):
            point = (p, index - p)
            if point[0] < len(grid) and point[1] < len(grid[0]):
                # points.append(point)
                points.append(grid[point[0]][point[1]])
        grid_out.append("".join(points))

    return grid_out

### ---

# print(wordsearch)

### |||

flipped_wordsearch = flip_grid(wordsearch)

# print(flipped_wordsearch)

## ///

rotated_wordsearch = rotate_grid(wordsearch)

# print(rotated_wordsearch)

### \\\

flipped_rotated_wordsearch = rotate_grid(flipped_wordsearch)

# print(flipped_rotated_wordsearch)

# Well .. that's long winded

# Function to find the word, both ways

def find_word(grid):
    count = 0
    for line in grid:
        if line.count("XMAS")>0: count += line.count("XMAS")
        if line.count("SAMX")>0: count += line.count("SAMX")
    return count

# Part one: count the words

count = find_word(wordsearch) + find_word(flipped_wordsearch)+ find_word(rotated_wordsearch) + find_word(flipped_rotated_wordsearch)

print(f"Part one: {count}")

# Part two: fuck ..

# Function to cut off the outer edges

def cut_and_search(grid):

    count = 0

    matches = [ "MMSS", "SMMS", "SSMM", "MSSM" ]
    #    1 2     M M     S M     S S     M S
    #     A       A       A       A       A
    #    4 3     S S     S M     M M     M S

    def search(x, y):
        ul = grid[x-1][y-1]
        ur = grid[x-1][y+1]
        br = grid[x+1][y+1]
        bl = grid[x+1][y-1]
        # print("".join([ul, ur, br, bl]))
        return "".join([ul, ur, br, bl]) in matches

    # Scan the grid, ignoring the outer edges, for the letter "A"

    for x in range(1, len(grid) - 1):
        for y in range (1, len(grid[0]) - 1):
            if grid[x][y] == "A":
                count += search(x, y)

    return count

count = cut_and_search(wordsearch)

print(f"Part two: {count}")

# with open("data/day04.txt") as file:
#     wordsearch = file.read().splitlines()

# print(f"Part two: {[ "".join([wordsearch[x-1][y-1], wordsearch[x-1][y+1], wordsearch[x+1][y+1], wordsearch[x+1][y-1]]) in [ "MMSS", "SMMS", "SSMM", "MSSM" ] for y in range (1, len(wordsearch[0]) - 1) for x in range(1, len(wordsearch) - 1) if wordsearch[x][y] == "A" ].count(True)}")
