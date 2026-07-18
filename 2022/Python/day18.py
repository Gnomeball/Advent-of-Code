# This one really confused me, partly because I didn't know what to do

with open("data/day18.txt") as file:
    cubes = [ tuple(map(int, l.split(","))) for l in file.read().splitlines() ]

# But after some thinking, I realised we don't actually care about it being
# voxels, we only care about what each point / cube can see

# Get the neighbours for a cube

def neighbours(x, y, z):
    delta = [ (+1, 0, 0), (0, +1, 0), (0, 0, +1),
              (-1, 0, 0), (0, -1, 0), (0, 0, -1) ]
    return [ (x+dx, y+dy, z+dz) for dx, dy, dz in delta]

# Collect the open faces in the magma blob

def exposed_faces(cubes):
    n_exposed = 0
    for cube in cubes:
        for neighbour in neighbours(*cube):
            n_exposed += neighbour not in cubes
    return n_exposed

# Part one

print(f"Part one = {exposed_faces(cubes)}")

# Part two

# Ok so I don't usually use imports .. because they do too much heavy lifting
# and that is definitely the case here, but I'm ok with it on this ocasion
# because I knew the overall logic, I just couldn't transfer that to code

from scipy.ndimage import binary_fill_holes as flood_fill

# Work out maximual size of our 3d matrix, and build our space
size = max(map(lambda c: c[0], cubes)) + 1
space =  [ [ [ 0 for x in range(size) ]
                 for y in range(size) ]
                 for z in range(size) ]

# Transfer the blob into that space
for x, y, z in cubes: space[z][y][x] = 1

# Fill all the gaps in (flood fill)
space = flood_fill(space)

filled_blob = [ (x, y, z)
                for x in range(len(space[0][0]))
                for y in range(len(space[0]))
                for z in range(len(space))
                if space[z][y][x] == 1 ]

print(f"Part two = {exposed_faces(filled_blob)}")
