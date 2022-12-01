with open("data/day05.txt", "r") as file:
    passes = file.read().splitlines()

print("Part one = {}".format(max([(8*int(p[:7].replace("F","0").replace("B","1"),2))+int(p[7:].replace("L","0").replace("R","1"),2) for p in passes])))

values = sorted([(8*int(p[:7].replace("F","0").replace("B","1"),2))+int(p[7:].replace("L","0").replace("R","1"),2) for p in passes])

print(f"Part two = {[x for x in range(len(passes)) if x not in values and x > values[0]][0]}")