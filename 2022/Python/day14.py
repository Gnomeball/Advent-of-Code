from functools import cmp_to_key

# class Point:
#     def __init__(self, x, y): self.x = x; self.y = y
#     def __repr__(self): return f"({self.x}, {self.y})"
#     def __eq__(self, other): return self.x == other.x and self.y == other.y

def comparator(left, right):
    if left[0] == right[0]:
        if left[1] > right[1]: return -1
    if     left[0] > right[0]: return -1
    return 1

with open("data/day14.txt") as file:
    lines = file.read().splitlines()
    lines = [ [ tuple(map(int, edge.split(","))) for edge in l.split(" -> ") ] for l in lines ]
    lines = [ list(zip(line, line[1:])) for line in lines ]
    lines = [ [ sorted(p, key = cmp_to_key(comparator), reverse = True) for p in l ] for l in lines ]
    rocks = [ [ [ (x, y) for x in range(p[0][0], p[1][0] +1) for y in range(p[0][1], p[1][1] +1) ] for p in l ] for l in lines ]
    rocks = set( item for sublist in [ item for sublist in rocks for item in sublist ] for item in sublist )

min_y = max(r[1] for r in rocks)

sand = set()

sand_castle, into_the_abyss = True, False

while sand_castle:
    curr_x, curr_y = 500, 0
    sand_still_falling = True
    while sand_still_falling:
        if curr_y > min_y:
            if not into_the_abyss:
                print(f"Part one = {len(sand)}")
                into_the_abyss = True
            sand.add((curr_x, curr_y))
            break
        # Down
        new_y = curr_y +1
        if (curr_x, new_y) not in rocks and (curr_x, new_y) not in sand:
            curr_y = new_y; continue
        # Down and Left
        new_x, new_y = curr_x -1, curr_y +1
        if (new_x, new_y) not in rocks and (new_x, new_y) not in sand:
            curr_x, curr_y = new_x, new_y; continue
        # Down and Right
        new_x, new_y = curr_x +1, curr_y +1
        if (new_x, new_y) not in rocks and (new_x, new_y) not in sand:
            curr_x, curr_y = new_x, new_y; continue
        # Landed
        sand.add((curr_x, curr_y))
        if (curr_x, curr_y) == (500, 0):
            sand_castle = False
            print(f"Part two = {len(sand)}")
            break
        sand_still_falling = False
