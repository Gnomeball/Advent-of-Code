CHARS = "abcdefghijklmnopqrstuvwxyz"

MOVES = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

def start_position(grid, low = False):
    positions = []
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == "S" or low and cell == "a":
                positions.append((row_index, col_index))
    return positions

def is_outside_grid(grid, dest_row, dest_col):
    return ( dest_row < 0 or dest_row >= len(grid)
          or dest_col < 0 or dest_col >= len(grid[0]) )

def can_move(grid, dest_row, dest_col, current):
    if is_outside_grid(grid, dest_row, dest_col):
        return False

    if current == "S": current = "a"
    destination = grid[dest_row][dest_col]

    if destination == "E": destination = "z"

    return CHARS.index(destination) <= CHARS.index(current) + 1

def shortest_path(grid, start_positions):
    path = [ (pos, 0) for pos in start_positions ]
    seen = set(start_positions)

    while path:
        (row, col), step_count = path.pop(0)
        current = grid[row][col]

        if current == "E":
            return step_count

        for row_delta, col_delta in MOVES:
            new_pos = (row + row_delta, col + col_delta)
            if new_pos not in seen and can_move( grid, *new_pos, current ):
                seen.add(new_pos)
                path.append( (new_pos, step_count + 1) )

with open("data/day12.txt") as file:
    grid = file.read().splitlines()

print(f"Part one = {shortest_path(grid, start_position(grid))}")
print(f"Part two = {shortest_path(grid, start_position(grid, True))}")
