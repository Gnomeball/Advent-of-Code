with open('data/day23.txt', 'r') as file:
    data = file.read().splitlines()

DIRS = { 'N' : ( 0, -1), 'E' : ( 1,  0),
         'S' : ( 0,  1), 'W' : (-1,  0),
         'NE': ( 1, -1), 'NW': (-1, -1),
         'SE': ( 1,  1), 'SW': (-1,  1) }

from collections import deque as circular_array

MOVES = circular_array( ['N', 'S', 'W', 'E'] )

CHECKS = { 'N': ( 'NW', 'N', 'NE' ),
           'S': ( 'SW', 'S', 'SE' ),
           'E': ( 'SE', 'E', 'NE' ),
           'W': ( 'SW', 'W', 'NW' ), }

START_STATE = set()

for y, row in enumerate(data):
    for x, cell in enumerate(row):
        if cell == '#': START_STATE.add((x, y))

def move(elf_x, elf_y, moves):
    possible = { direction: (elf_x + xd, elf_y + yd)
                 for direction, (xd, yd) in DIRS.items()
                 # Only if this isn't already taken by another elf
                 if (elf_x + xd, elf_y + yd) not in elfs }
    if len(possible) == 8: # Remain still
        return (elf_x, elf_y)
    else:
        for move in moves:
            possibles = CHECKS[move]
            if len(set(possibles).intersection(possible)) == 3:
                return possible[move]
        else: # Remain still because none were possible
            return (elf_x, elf_y)

def check_possible_moves(moves):
    possibles = {}
    for v in moves.values(): possibles[v] = possibles.get(v, 0) + 1
    return { k: (v if possibles[v] == 1 else k) for (k, v) in moves.items() }

def move_elfs(elfs, moves):
    next_elfs = check_possible_moves({
        elf: move(*elf, moves) for elf in elfs })
    moves.rotate(-1)
    return set(next_elfs.values()), moves

# Part one

elfs, moves = START_STATE.copy(), MOVES.copy()

for _ in range(10): elfs, moves = move_elfs(elfs, moves)

def area_of(elfs):
    elfs = sorted(elfs)
    min_elf, max_elf = elfs[0][0], elfs[-1][0] + 1
    area = (max_elf - min_elf) * (max_elf - min_elf)
    return area - len(elfs)

print(f"Part one = {area_of(elfs)}")

# Part two

elfs, moves = START_STATE, MOVES

N_MOVES = 0

while True: # tut tut
    next_elfs, moves = move_elfs(elfs, moves)
    N_MOVES += 1
    if len(next_elfs.intersection(elfs)) == len(elfs):
        break # No one moved
    # implicit else
    elfs = next_elfs

print(f"Part two = {N_MOVES}")
