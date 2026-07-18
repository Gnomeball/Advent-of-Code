from parse import parse

with open("data/day02.txt") as file:
    passwords = file.read().splitlines()

print("Part one = {}".format(len([p for a,b,l,p in map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, passwords) if a <= p.count(l) <= b])))
print("Part two = {}".format(len([p for a,b,l,p in map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, passwords) if (p[a-1] == l) != (p[b-1] == l)])))