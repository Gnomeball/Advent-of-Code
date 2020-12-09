from functools import reduce

with open("day03.txt") as file:
    grid = file.read().splitlines()

# Part 1

gri3 = [line * 3 for line in grid]
path = [(i, (i*3)%len(gri3[i])) for i in range(len(gri3))]
path = [gri3[x][y] for x,y in path if gri3[x][y] == "#"]

print(len(path))

# Part 2

index = [(1,1),(3,1),(5,1),(7,1),(1,2)]

grids = [[line * r for line in grid] for r,d in index]

paths = [[((i*d), (i*r)%(len(grid[0])*r)) for i in range(len(grid)) if (i*d) < len(grid)] for r,d in index]

paths = [[grids[n][x][y] for x,y in paths[n] if grids[n][x][y] == "#"] for n in range(len(index))]

print(reduce(lambda a,b: a*b, map(len, paths)))
