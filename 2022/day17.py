#!bin/python3

# Ok, so this one may be the most convoluted Python I've ever been obligated
# to write, so I'm going to comment this like it's going out of fashion :D

# Right, with that out of the way;

# First, we define the Tet.. I mean Rock, shapes

# Because they are always 2 slots from the left, we define their
# starting position as if they are already inserted to the map

LINE_H = [ (2, 0), (3, 0), (4, 0), (5, 0) ]

PLUS   = [         (3, 2),
           (2, 1), (3, 1), (4, 1),
                   (3, 0)         ]

ELL    = [                 (4, 2),
                           (4, 1),
           (2, 0), (3, 0), (4, 0) ]

LINE_V = [ (2, 3),
           (2, 2),
           (2, 1),
           (2, 0) ]

SQUARE = [ (2, 1), (3, 1),
           (2, 0), (3, 0) ]

# And then we put them into an array, so we call them in the correct order

SHAPES = [ LINE_H, PLUS, ELL, LINE_V, SQUARE ]

# Now the map of slots that we've already filled
# This must start as the floor

SLOTS_TAKEN = [ (0, 0), (1, 0), (2, 0) ,(3, 0), (4, 0), (5, 0), (6, 0) ]

# And finally, read in the moves

MOVES = [ *open("data/day17.txt", "r").read().strip() ]

# To make things posibly clearer, we also define our movements

LEFT, RIGHT, DOWN = -1, 1, -1

# For tracking the growth of the pile

HEIGHTS = []

# Now, we're set to start implementing some methods

# First, one to get the height of the map, so we can print it,
# as well as detect where to add the next shape
def map_height():
    # This is simple, we collect the maximum y, via a map
    return max(map(lambda x: x[1], SLOTS_TAKEN))

# Something to use to visualise if we are building the tower correctly
# Not really useful beyond that because it gets very long
def print_map(n_lines):
    # Work out the current height of the map
    height = map_height()

    # Work out where we stop printing
    if n_lines == height:
          n_lines = 0 # To the bottom
    else: n_lines = height - n_lines

    # Now, for each line in the height, we print it's taken slots
    for y in range(height, n_lines, -1):
        # current y and left wall
        line = f"{str(y).ljust(5)}|"
        # slots
        for x in range(0, 7):
            if (x, y) in SLOTS_TAKEN:
                  line += "#"
            else: line += " "
        # right wall
        print(line + "|")

    # If not printing the entire tower, filler
    if n_lines != 0:
        print("     | ..... |")

    # And then print the base of the map
    print("     +-------+")


def get_next_move():
    # Get next move
    move = MOVES.pop(0)
    # Put it on the back, so they wrap around
    MOVES.append(move)
    # Now parse
    if   move == "<": move = LEFT
    elif move == ">": move = RIGHT
    # For reasons of running out of input ..
    elif move == ".": move = "stop"
    # And return
    return move

# Checkinp function to see if the shape can still move sideways
def can_move_sideways(shape):
    for (x, y) in shape:
        # Check the shape won't be in the wall, or inside another shape
        if x == -1 or x == 7 or (x, y) in SLOTS_TAKEN:
            return False
    return True

# The above, but only interested in the downward direction
# ( we could technically the above function insdead, but naming things
#   is hard and we would be doing unecessary wall checks )
def can_move_down(shape):
    for (x, y) in shape:
        # Check the shape isn't inside another shape
        if (x, y) in SLOTS_TAKEN:
            return False
    return True

# Moves act somewhat recursively, so in this fuection we have to return either
# itself, or the shape's final resting place, but on condition, because even
# after landing, shapes can still move sideways, once
def move_shape(shape):
    last_move = None

    # First, get the sideways move
    MOVE = get_next_move()

    # For reasons of running out of input ..
    if MOVE == "stop":
        last_move = "anything except down"
        return shape, last_move

    # and try to move the shape
    new_shape = [ (x + MOVE, y) for (x, y) in shape ]
    if can_move_sideways(new_shape):
        shape = new_shape
        last_move = "sideways"

    # Then, down
    new_shape = [ (x, y + DOWN) for (x, y) in shape ]
    if can_move_down(new_shape):
        shape = new_shape
        last_move = "down"

    # If it can still move .. (this is the hard part it seems)
    new_shape = [ (x, y + DOWN) for (x, y) in shape ]
    if can_move_down(new_shape):
          return move_shape(shape)
    else: return shape, last_move

# And finally, the function that causes all the chaos, here we nede to first
# add a shape to the top of the map, then move it down, and then add it to the
# map, so that the next shape can see it.
def add_shape(shape):
    # First, work out the current height of the map
    height = map_height()

    # Now, make a shape at that height
    shape = [ (x, y + height + 4) for (x, y) in shape ]

    last_move = "down"
    # Now, whilst this shape can still fall, we move it
    while last_move == "down":
        shape, last_move = move_shape(shape)

    # Then, add the shape to the map
    for slot in shape: SLOTS_TAKEN.append(slot)

    # And maybe get rid of layers 30 below this one?
    # ( Ok, not enough speed up.. there's a trick to this )
    for (x, y) in SLOTS_TAKEN.copy():
        if y <= height - 30:
            SLOTS_TAKEN.remove((x, y))

    # Look for a cycle in the height changes
    height_change = map_height() - height
    HEIGHTS.append(height_change)

# Part one

for i in range(2022):
    add_shape(SHAPES[i % 5])

# 3202
print(f"Part one = {map_height()}")

# Part two

# Cycle length was semi-guessed, in that I knew it was likely to be < 2022
# so that it wouldn't show up in the data for part one if you were to simulate
# the result and print it out, as I did.

# As such, I decided to print out the first 5,000 shapes, and then start looking
# for a pattern, this wasn't very helpful though.  And that's when it hit me
# that all we really care about is the change in height - and any sufficiently
# long repeated pattern would probably be the cycle we are looking for.

# So after adding the HEIGHTS array, I printed it out, and starting looking in
# the 1,500 -> 2,000 region (thinking it would probably be on the higher end,
# as a lot of these problems are - going backwards often helps).  Starting
# with 1,750, and then moving + / - 1 each time, until I had a match with the
# test data - turns out I didn't have to go far - eventually confirmed this.

OSFF = 1745

# I am yet to work out a way to do this dynamically though,
# but I'm sure I will before the year is out

trillion  = 1000000000000

# RUn our main loop again, this time until 2 x the cycle length
for i in range(2022, 2 * OSFF):
    add_shape(SHAPES[i % 5])

# so that we can then split it into two,
CYCLES    = [ HEIGHTS[s:s + OSFF] for s in range(0, 2 * OSFF, OSFF) ]
# the first of which contains the initial data used to get us into a cycle
INITIAL   = sum(CYCLES[0])
# and the second is a cycle that is ten reperted ad-infinitum.
CYCLE     = sum(CYCLES[1])

# Now, we do some maths to work out how many cycles we need,
FACTOR    = int( (trillion - OSFF) / OSFF )
# and what the remainder will be in the final cycle.
REMAINDER = sum(CYCLES[1][:(trillion - OSFF) % OSFF])

# Before we put all this together to work out the height;
TRILLION  = INITIAL + ( CYCLE * FACTOR ) + REMAINDER

# 1591977077352
print(f"Part two = {TRILLION}")

# And with that, this most certainly is the most complex thing I've ever
# successfully programmed in Python .. even if so far it's not complete
