from parse import parse

with open("data/day07.txt", "r") as file:
    rules = dict([(r,[(int(b.split()[0])," ".join(b[2:].split()[:-1])) for b in b.split(", ")] if b != "no other bags" else []) for r,b in map(lambda l: parse("{} bags contain {}", l[:-1]).fixed, file.read().splitlines())])

def get_candidates(bag):
    return [rule for rule in rules if bag in [bag[1] for bag in rules[rule]]]

candidates = get_candidates("shiny gold")

last, curr = 0, 1

while last != curr:
    last = curr
    for bag in candidates:
        new = get_candidates(bag)
        candidates += new
    curr = len(set(candidates))

print(f"Part one = {len(set(candidates))}")

# print(f"Part two = {}")
