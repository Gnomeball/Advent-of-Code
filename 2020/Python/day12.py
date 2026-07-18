with open("data/day12.txt", "r") as file:
    directions = [(d[0], int(d[1:])) for d in file.read().splitlines()]

headings_d = ["N", "E", "S", "W"]
headings_v = [0, 0, 0, 0]

heading_c = "E"

for direction in directions:
    d = direction[0]

    if d in headings_d:
        headings_v[headings_d.index(d)] += direction[1]

    elif d == "F":
        headings_v[headings_d.index(heading_c)] += direction[1]

    else:
        c = [1, -1][["R", "L"].index(d)]
        heading_c = headings_d[int((headings_d.index(heading_c) + (c * (direction[1]) / 90)) % 4)]

print(abs(headings_v[0] - headings_v[2]) + abs(headings_v[1] - headings_v[3]))
