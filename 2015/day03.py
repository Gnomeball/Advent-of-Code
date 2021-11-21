def part_one(arrows: str) -> int:
    x, y = 0, 0
    houses = {(x, y)}
    for char in arrows:
        if char == ">": x += 1
        if char == "<": x -= 1
        if char == "^": y += 1
        if char == "v": y -= 1
        houses.add((x, y))
    return len(houses)

def part_two(arrows: str) -> int:
    robo_x, santa_x = 0, 0
    robo_y, santa_y = 0, 0
    houses = {(robo_x, robo_y), (santa_x, santa_y)}
    chunks = [arrows[i:i+2] for i in range(0, len(arrows), 2)]
    for chunk in chunks:
        if chunk[0] == ">": santa_x += 1
        if chunk[0] == "<": santa_x -= 1
        if chunk[0] == "^": santa_y += 1
        if chunk[0] == "v": santa_y -= 1
        if chunk[1] == ">": robo_x += 1
        if chunk[1] == "<": robo_x -= 1
        if chunk[1] == "^": robo_y += 1
        if chunk[1] == "v": robo_y -= 1
        houses.add((robo_x, robo_y))
        houses.add((santa_x, santa_y))
    return len(houses)

with open("day03.txt", "r") as file:
    arrows = file.read()
    print(part_one(arrows))
    print(part_two(arrows))
