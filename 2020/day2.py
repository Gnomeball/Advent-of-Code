from parse import *
from functools import *

with open("day2.txt") as file:
    passwords = file.read().splitlines()

# Part 1

print(len([p for a,b,l,p in map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, passwords) if a <= p.count(l) <= b]))

# Part 2

print(len([p for a,b,l,p in map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, passwords) if (p[a-1] == l) != (p[b-1] == l)]))