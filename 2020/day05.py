with open("day05.txt", "r") as file:
    passes = file.read().splitlines()

# Part 1

print(max([(8*int(p[:7].replace("F","0").replace("B","1"),2))+int(p[7:].replace("L","0").replace("R","1"),2) for p in passes]))

# Part 2

values = sorted([(8*int(p[:7].replace("F","0").replace("B","1"),2))+int(p[7:].replace("L","0").replace("R","1"),2) for p in passes])

seat = [x for x in range(len(passes)) if x not in values and x > values[0]]

print(seat)
