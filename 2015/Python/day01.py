def part_one(string: str) -> int:
    floor = 0
    for char in string:
        if char == '(': floor += 1
        else: floor -= 1
    return floor

def part_two(string: str) -> int:
    floor = 0
    pos = 0
    for char in string:
        pos += 1
        if char == '(': floor += 1
        else: floor -= 1
        if floor == -1:
            return pos;

with open("../data/day01.txt", "r") as file:
    brackets = file.read()
    print(part_one(brackets))
    print(part_two(brackets))
