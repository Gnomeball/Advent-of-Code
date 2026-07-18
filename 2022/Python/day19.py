from typing import NamedTuple

class Resource(NamedTuple):
    geode: int
    obsidian: int
    clay: int
    ore: int

    def __lt__(self, resource):
        return any(r1 < r2 for r1, r2 in zip(self, resource))

    def __add__(self, resource):
        return Resource(*(r1 + r2 for r1, r2 in zip(self, resource)))

    def __sub__(self, resource):
        return Resource(*(r1 - r2 for r1, r2 in zip(self, resource)))

class Robot:
    def __init__(self, name, costs, prods):
        self.name = name
        self.costs = costs
        self.prods = prods

class Blueprint:
    def __init__(self, number, robots):
        self.number = number
        self.robots = robots

import re

blueprints = {}
with open("data/day19.txt") as file:
    for line in file:
        i, a, b, c, d, e, f = map(int, re.findall(r"\d+", line))
        blueprint = Blueprint(i, (
            Robot("Geode",    Resource(0, f, 0, e), Resource(1, 0, 0, 0)),
            Robot("Obsidian", Resource(0, 0, d, c), Resource(0, 1, 0, 0)),
            Robot("Clay",     Resource(0, 0, 0, b), Resource(0, 0, 1, 0)),
            Robot("Ore",      Resource(0, 0, 0, a), Resource(0, 0, 0, 1)),
            Robot("None",     Resource(0, 0, 0, 0), Resource(0, 0, 0, 0)) ))
        blueprints[i] = blueprint

def run(blueprint, time, threshold):
    todo = [ (Resource(0, 0, 0, 0), Resource(0, 0, 0, 1)) ]
    for minute in range(time):
        temp = []
        for having, making in todo:
            for robot in blueprint.robots:
                if having < robot.costs: continue
                have, make = (having + making - robot.costs), (making + robot.prods)
                temp.append((have, make))
        todo = sorted(temp, reverse=True, key=lambda e: tuple(zip(*e)))[:threshold]
    return max(having.geode for having, _ in todo)

part_one = sum(run(blueprint, 24, 200) * i
           for i, blueprint in blueprints.items())

print("Part one =", part_one)

from math import prod as product

part_two = product(run(blueprint, 32, 8000)
            for i, blueprint in blueprints.items() if i < 4)

print("Part two =", part_two)