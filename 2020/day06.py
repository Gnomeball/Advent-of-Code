with open("data/day06.txt", "r") as file:
    answers = file.read().split("\n\n")

print("Part one = {}".format(sum([len(set(a)) for a in [a.replace("\n", "") for a in answers]])))

print("Part two = {}".format(sum([len(set.intersection(*a)) for a in [[set(sorted(e)) for e in a] for a in [a.split("\n") for a in answers]]])))
