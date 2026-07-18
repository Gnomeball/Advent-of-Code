# Read in the data, line by line, and unzip them into two lists (one for each column)

with open("data/day01.txt") as file:
    left, right = zip(*[[int(x) for x in line.split()] for line in file.read().splitlines()])

# Don't know how to fit this in the above segment

left = sorted(left)
right = sorted(right)

# Function to get the distance between a pair of locations

def distance_between(left, right, index) -> int:
    return abs(left[index] - right[index])

# Part one: Accumule the distances

count = sum([distance_between(left, right, i) for i in range(len(left))])

print(f"Part one: {count}")

# Part two: Count up instances of first list item in second list

similarity = sum([item * right.count(item) for item in left])

print(f"Part two: {similarity}")
