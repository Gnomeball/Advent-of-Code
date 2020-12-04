from parse import *
from functools import *

with open("day2.txt") as file:
    passwords = file.read().splitlines()

# passwords = [(p.split()[0].split("-"), p.split()[1][:1], p.split()[2]) for p in passwords]
# valid = [1 if p[1]*int(p[0][0]) in "".join(sorted(p[2])) and p[1]*(int(p[0][1])+1) not in "".join(sorted(p[2])) else 0 for p in passwords]
# print(sum(valid))

# Part 1

print(len([p for a,b,l,p in map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, passwords) if a <= p.count(l) <= b]))

# Part 2

print(len([p for a,b,l,p in map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, passwords) if (p[a-1] == l) != (p[b-1] == l)]))