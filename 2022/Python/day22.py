# This was a tough one, but fun

with open("data/day22.txt") as file:
    MAP, MOVES = file.read().split("\n\n")

# These are hard coded because I believe the map might be a cube,
# and as such everyone will have the same shape, and starting position

START = 51 + 1j
WIDTH = 150
DEPTH = 200

# Using complex numbers to represent X and Y with single values
# These are [ Right, Down, Left, Up ]
DIRS = [ 1, 1j, -1, -1j ]

# Build our tile grid

TILE_GRID = dict()

for y, row in enumerate(MAP.splitlines(), 1):
    for x, tile in enumerate(row, 1):
        # We don't care abous empty space
        if tile != ' ': TILE_GRID[x + y * 1j] = tile

# Parse the instructions

# First, append an X to each R or L in the string, then split on that X
# So that from "123R456L890" we get [ "123R", "456L"¸ "890" ]
MOVES = MOVES.replace("R", "RX").replace("L", "LX").split("X")

# Set up a map to convert the letter into our direction
TURNS = {"R": 1, "L": -1}

# Parse all except the last one (because it doesn't have a letter)
instructions = [ ( int(move[:len(move)-1]), TURNS[move[-1]] ) for move in MOVES[:-1] ]

# And manually add the last one, with a zero direction
instructions.append( (int(MOVES.pop()), 0) )

def generate_password(pos, dir):
    # The final password is the sum of
    #   1000 times the row, 4 times the column, and the facing.
    return int(sum([ 1000 * pos.imag, 4 * pos.real, dir ]))

# Part one

def follow_minkeys(start, instructions):
    CURR_POS, CURR_DIR = start, 0
    for (step, turn) in instructions:
        for _ in range(step):
            new = CURR_POS + DIRS[CURR_DIR]
            while new not in TILE_GRID:
                new += DIRS[CURR_DIR]
                x, y = new.real, new.imag
                x = WIDTH if x < 1 else 1 if x > WIDTH else x
                y = DEPTH if y < 1 else 1 if y > DEPTH else y
                new = x + y * 1j
            if TILE_GRID[new] == '.':
                  CURR_POS = new
            else: break
        CURR_DIR = (CURR_DIR + turn) % 4
    return generate_password(CURR_POS, CURR_DIR)

print(f"Part one = {follow_minkeys(START, instructions)}")

# Part two

# Doing quite a lot of hard coding here because it's just easier
#   And, these are not meant to be general solutions anyway

def traverse_cube(start, instructions):
    CURR_POS, CURR_DIR = start, 0
    for (step, turn) in instructions:
        for _ in range(step):
            new = CURR_POS
            new += DIRS[CURR_DIR]
            switch = False
            if new not in TILE_GRID:
                # Assume we will switch direction
                switch = True
                if CURR_DIR == 0:
                    # We are going Right
                    if 1 <= new.imag <= 50:
                        # B's right matches E's right
                        x, y = 100, 151 - new.imag
                        # so next dir is left
                        new_dir = 2
                    elif 51 <= new.imag <= 100:
                        # C's right matches B's bottom
                        x, y = 50 + new.imag, 50
                        # so next dir is up
                        new_dir = 3
                    elif 101 <= new.imag <= 150:
                        # E's right matches B'right
                        x, y = 150, 51 - (new.imag - 100)
                        # so next dir is left
                        new_dir = 2
                    else:
                        # F's right matches E's bottom
                        x, y = 50 + (new.imag - 150), 150
                        # so next dir is up
                        new_dir = 3
                elif CURR_DIR == 1:
                    # We are going Down
                    if 101 <= new.real <= 150:
                        # B's bottom matches C's right
                        x, y = 100, 50 + (new.real - 100)
                        # next dir is left
                        new_dir = 2
                    elif 51 <= new.real <= 100:
                        # E's bottom matches F's right
                        x, y = 50, 150 + (new.real - 50)
                        # next dir is left
                        new_dir = 2
                    else:
                        # F's bottom matches B's top
                        x, y = new.real + 100, new.imag - 200
                        # no change in direction
                        switch = False
                elif CURR_DIR == 2:
                    # We are going Left
                    if 1 <= new.imag <= 50:
                        # A's left matches D's left
                        x, y = 1, 151 - new.imag
                        # next dir is right
                        new_dir = 0
                    elif 51 <= new.imag <= 100:
                        # C's left matches D's top
                        x, y = new.imag - 50, 101
                        # next dir is down
                        new_dir = 1
                    elif 101 <= new.imag <= 150:
                        # D's left matches A's left
                        x, y = 51, 151 - new.imag
                        # next dir is right
                        new_dir = 0
                    else:
                        # F's left matches A's top
                        x, y = 50 + (new.imag - 150), 1
                        # next dir is down
                        new_dir = 1
                else: # CURR_DIR = 4:
                    # We are going Up
                    if 1 <= new.real <= 50:
                        # D's top matches C's left
                        x, y = 51, 50 + new.real
                        # next dir is right
                        new_dir = 0
                    elif 51 <= new.real <= 100:
                        # A's top matches F's left
                        x, y = 1, 100 + new.real
                        # next dir is right
                        new_dir = 0
                    else:
                        # B's top matches F's bottom
                        x, y = new.real - 100, 200
                        # no change in direction
                        switch = False
                new = x + y * 1j
            if TILE_GRID[new] == '.':
                  CURR_POS = new
                  if switch: CURR_DIR = new_dir
            else: break
        CURR_DIR = (CURR_DIR + turn) % 4
    return generate_password(CURR_POS, CURR_DIR)

print(f"Part two = {traverse_cube(START, instructions)}")
