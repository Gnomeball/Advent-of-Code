# Read in the input file, storing each node as a map using real+imaginary

with open('data/day10.txt') as file:
    grid = { i+j*1j : int(col) for i,row in enumerate(file) for j,col in enumerate(row.strip())}

# Recursive DFS to search for paths

def search(part, current, already_seen, elevation = 0):
    if current in grid and grid[current] == elevation:
        # Only count unique endpoints for part one!
        if elevation < 9 or (part == 1 and current in already_seen):
            # Search for paths from next elevation up
            return sum(search(part, current + n, already_seen, elevation + 1) for n in [1, -1, 1j, -1j])
        already_seen.add(current)
        # Path found
        return True
    # Impossible move; either outside of grid, or too steep
    return False

# Seach the grids, passing in the part so we can discount duplicate endpoints

for n,p in enumerate(["one", "two"], start=1):
    print(f"Part {p}: {sum(search(n, pos, set()) for pos in grid if grid[pos] == 0)}")
