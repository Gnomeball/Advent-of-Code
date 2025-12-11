# Little bit of caching never hurt!
from functools import cache

# Tree?

tree = {}

with open("./data/day11.txt") as file:
    lines = [ line.split() for line in file.read().splitlines() ]
    for line in lines:
        tree[line[0].strip(":")] = line[1:]

@cache
def count_paths_from_and_to(_from, to):
	# if we are at the destination node
	if _from == to:
		return True
	# implicit else, continue counting more paths
	return sum(count_paths_from_and_to(node, to) for node in tree[_from])

print("Part one =", count_paths_from_and_to("you", "out"))

@cache
def count_paths_from_and_via(_from, dac, fft):
	# if we are at the destination node
	if _from == "out":
        # return true if we've also seen the two via nodes
		return True if dac and fft else False
	# implicit else, continue counting more paths, passing in if we've passed a via node
	return sum(count_paths_from_and_via(node, dac or _from == "dac", fft or _from == "fft") for node in tree[_from])

print("Part two =", count_paths_from_and_via("svr", False, False))
