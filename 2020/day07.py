from parse import parse

with open("day07.txt", "r") as file:
    rules = file.read().splitlines()

rules = dict([(r,[(int(b.split()[0])," ".join(b[2:].split()[:-1])) for b in b.split(", ")] if b != "no other bags" else []) for r,b in map(lambda l: parse("{} bags contain {}", l[:-1]).fixed, rules)])

# Part 1

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

print(len(set(candidates)))
