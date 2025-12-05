with open("data/day5.txt") as file:
    [ ranges, ingredients ] = file.read().split("\n\n")
    ranges = [ list(map(int, (r.split("-")))) for r in ranges.splitlines() ]
    ingredients = list(map(int, ingredients.splitlines()))

# Function to flatten a list of ranges, merging any overlaps

def flatten_ranges(ranges):
    ranges = sorted(ranges)

    out = []
    current_start, current_stop = ranges.pop(0)

    for next_start, next_stop in ranges:
        # print(current_start, current_stop, next_start, next_stop)
        if next_start <= current_stop:
            # Overlap
            current_stop = max(current_stop, next_stop)
        else: # next_start > current_stop:
            # Gap, no overlap
            out.append([current_start, current_stop])
            current_start, current_stop = next_start, next_stop

    out.append([current_start, current_stop])

    return out

ranges = flatten_ranges(ranges)

# Output

print("Part one = ", sum(id >= left and id <= right for left, right in ranges for id in ingredients))
print("Part two = ", sum(right + 1 - left for left, right in ranges))
