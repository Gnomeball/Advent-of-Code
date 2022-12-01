from parse import parse

with open("data/day07.txt", "r") as file:
    rules = dict([(r,[(" ".join(b[2:].split()[:-1]), int(b.split()[0])) for b in b.split(", ")] if b != "no other bags" else []) for r,b in map(lambda l: parse("{} bags contain {}", l[:-1]).fixed, file.read().splitlines())])

def bags_that_can_hold(bag):
    candidates = []
    for rule in rules:
        for bags in rules[rule]:
            if bag == bags[0]:
                candidates.append(rule)
                candidates += bags_that_can_hold(rule)
    return set(candidates)

def contains_how_many_bags(bag):
    bags_this_contains = 1
    for bags in rules[bag]:
        bags_this_contains += bags[1] * contains_how_many_bags(bags[0])
    return bags_this_contains

print("Part one = {}".format(len(bags_that_can_hold("shiny gold"))))
print("Part one = {}".format(contains_how_many_bags("shiny gold") - 1))
