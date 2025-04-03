from itertools import permutations

with open("data/day08.txt") as file:
    grid = { i+j*1j : col for i,row in enumerate(file) for j,col in enumerate(row.strip())}

for r in [1], range(50):
    anti = []
    for freq in {*grid.values()} - {'.'}:
        ants = [p for p in grid if grid[p] == freq]
        pairs = permutations(ants, 2)
        for f in pairs: print(f)
        anti += [ a+n*(a-b) for a,b in pairs for n in r ]

    print(len(set(anti) & set(grid)))