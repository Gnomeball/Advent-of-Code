with open("data/day03.txt") as file:
    wires = [ [ (m[0], int(m[1:])) for m in line.split(",") ]
                for line in file.read().splitlines() ]

dirs = { 'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1) }

def manhattan(pos):
    return sum(map(abs, pos))

def get_distances(wire_a, wire_b, collisions):
    return [ wire_a.index(c) + wire_b.index(c) + 2 for c in collisions ]

def get_collisions(wire_a, wire_b):
    return list(set(wire_a) & set(wire_b))

def get_wire_history(wire):
    loc, history = [0, 0], []
    for move in wire:
        for _ in range(move[1]):
            loc[0] += dirs[move[0]][0]
            loc[1] += dirs[move[0]][1]
            history.append(tuple(loc))
    return history

# print("Paths")
paths = list(map(get_wire_history, wires))

# print("Collisions")
collisions = get_collisions(*paths)

# print("Manhattan")
print(f"Part one = {min(map(manhattan, collisions))}")

# print("Distances")
distances = get_distances(*paths, collisions)
print(f"Part two = {min(distances)}")