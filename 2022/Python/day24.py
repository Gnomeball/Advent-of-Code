# Oh yay a grid, I can do these!

# Blizzard directions
DIRS = { "^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1) }

# Array of all Blizzards - cannot bn a set because they can overlap
BLIZZARDS = []

# Set of walls - these don't move (I hope!)
WALLS = set()

# Popuute the blizzards array
with open("data/day24.txt") as file:
    rows = file.read().splitlines()
    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            if cell == ".":
                # Gap - we don't care
                continue
            # Implicit else
            if cell in "^>v<":
                # Add this the array of blzzards
                BLIZZARDS.append( ((r, c), cell) )
            elif cell == "#":
                # Add this to the set of walls
                WALLS.add( (r, c) )

# Collect the bounds
HEIGHT, WIDTH = len(rows), len(rows[0])

# And define our destinations, top left -> bottom right
START, FINISH = (0, 1), (HEIGHT - 1, WIDTH - 2)

# I'm going to cheat here and pre-calculate the entire set of blizzard states
# this way we only need to map from state to state when we work out the path.

# We can do this because they cycle, forever unchanging;

# > This process repeats at least as long as you are observing it,
# >   but probably forever.

CYCLE_LENGTH = (HEIGHT - 2) * (WIDTH - 2)

# For speed we can actually cut this short..
# but it requires information you don't initially know
# CYCLE_LENGTH = 1000

BLIZZARD_STATES = []

def update_blizzards(blizzards):
    next_blizzards = []
    for pos, dir in blizzards:
        row = pos[0] + DIRS[dir][0]
        col = pos[1] + DIRS[dir][1]
        # Moves out of the top -> bottom
        if   row == 0: row = HEIGHT - 2
        # Moves out of the bottom -> top
        elif row == HEIGHT - 1: row = 1
        # Moves out of the left -> right
        if   col == 0: col = WIDTH - 2
        # Moves out of the right -> left
        elif col == WIDTH - 1:  col = 1
        next_blizzards.append( ( (row, col), dir ) )
    return next_blizzards

# It's a do while!
blizzards = BLIZZARDS.copy()

# For the length of the cycle, we;
for _ in range(CYCLE_LENGTH):
    # work out the current locations of the blizzards,
    blizzard_locations = { blizzard for blizzard, dir in blizzards }
    # put these into the overall set of states,
    BLIZZARD_STATES.append(blizzard_locations)
    # and update them for the next state.
    blizzards = update_blizzards(blizzards)

# print(f"[ {len(BLIZZARD_STATES)} ] Blizzard states have been pre-computed!")

# Ok, now we're set to actually find a path, I think ..

def blizzard_first_search(starting_node, destination, states):
    # Where we begin
    curr_node = [ starting_node ]
    # Where we've been
    visited_nodes = { starting_node }

    # While we haven't taken leave of the universe
    while curr_node:

        # Where are we moving from?
        starting_node = curr_node.pop(0)

        # And when? We need to know both!
        pos, tick = starting_node

        # If we are at the destination
        if pos == destination:
            # We have arrived! (horray)
            return tick

        # Increment our tick
        next_tick = (tick + 1) % CYCLE_LENGTH

        # Update the blizzards for the next state
        next_blizzards = states[ tick % CYCLE_LENGTH ]

        # For each possible move ..
        for dir in [ (0, 1), (1, 0), (0, -1), (-1, 0), (0, 0) ]:
            row, col = pos[0] + dir[0], pos[1] + dir[1]

            # If we're at our destination
            if (row, col) == destination: return tick

            # Oops, we're probably going to end up in Kansas of something
            if (row, col) in next_blizzards: continue

            # Odear, we walked into a wall again (ouch)
            if (row, col) in WALLS: continue

            # We seem to have already been here
            if ((row, col), next_tick) in visited_nodes: continue

            # Now, assuming we've not fallen off the edge of the mountain ..
            if 0 <= row < HEIGHT and 0 <= col < WIDTH:
                visited_nodes.add(((row, col), next_tick))
                curr_node.append(((row, col), tick + 1))

    # If this happens, something really whacky happened
    exit("Uh oh!")

# Part one - There!

TICK = blizzard_first_search((START, 0), FINISH, BLIZZARD_STATES)

print(f"Part one = {TICK}")

# Part two - Back, and there again! (a Hobbit's, I mean Elf's, tale)

TICK = blizzard_first_search((FINISH, TICK), START, BLIZZARD_STATES)
TICK = blizzard_first_search((START, TICK), FINISH, BLIZZARD_STATES)

print(f"Part two = {TICK}")
