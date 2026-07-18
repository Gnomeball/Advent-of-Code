with open("data/day09.txt") as file:
    moves = [ (move[0], int(move[2:])) for move in file.readlines() ]

dirs = { 'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1) }

def move_head(head, direction):
    head[0] += dirs[direction][0]
    head[1] += dirs[direction][1]

def move_knot(knot, prev):
    knot[0] += comparator(prev[0] - knot[0])
    knot[1] += comparator(prev[1] - knot[1])

def distance_between(this, prev):
    return max(abs(this[0] - prev[0]), abs(this[1] - prev[1]))

def comparator(n):
    return 0 if n == 0 else 1 if n > 0 else -1

# Knot 0 is the head
knots   = [ [0, 0] for _ in range(10) ]
history = [ set()  for _ in range(10) ]

for move in moves:
    for _ in range(move[1]):
        # Move the head
        move_head(knots[0], move[0])
        # Move the other knots
        for i in range(1, 10):
            if distance_between(knots[i], knots[i-1]) == 2:
                move_knot(knots[i], knots[i-1])
        # Update location history for all knots, including head
        for k in range(10):
            history[k].add(tuple(knots[k]))

print(f"Part one = {len(history[1])}")
print(f"Part two = {len(history[9])}")