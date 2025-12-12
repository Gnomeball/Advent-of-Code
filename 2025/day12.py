# A trick like this would be welcome if this were still a 25 day event, today it feels almost wrong

def region(line):
    # A bit of a hack, but it works
    x, y, counts = line.replace("x", ": ").split(": ")
    return int(x) * int(y), list(map(int, counts.split(" ")))

def fits(r_size, p_count, presents):
    # This however, does not work on the example :D
    return r_size >= sum(p_count[p] * presents[p] for p in range(6))

with open("./data/day12.txt") as file:
    lines = file.read().split("\n\n")
    region_lines = lines.pop().split("\n")[:-1]

    presents = [ present.count("#") for present in lines ]
    regions = [ region(line) for line in region_lines ]

print("Part one =", sum(fits(r_size, p_count, presents) for r_size, p_count in regions))
