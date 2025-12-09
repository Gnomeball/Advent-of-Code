def part_one(sums: [str]) -> int:
    total = 0
    for s in sums:
        l, w, h = [int(x) for x in s.split("x")]
        a, b, c = l * w, w * h, h * l
        total += a+a + b+b + c+c + min([a, b, c])
    return total

def part_two(sums: [str]) -> int:
    total = 0
    for s in sums:
        l, w, h = [int(x) for x in s.split("x")]
        wrap = l+l + w+w + h+h - max([l+l, w+w, h+h])
        extra = l * w * h
        total += extra + wrap
    return total

with open("../data/day02.txt", "r") as file:
    sums = file.read().splitlines()
    print(part_one(sums))
    print(part_two(sums))
