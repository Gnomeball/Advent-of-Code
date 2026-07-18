with open("data/day01.txt", "r") as file:
    ints = [int(i) for i in file.read().splitlines()]

print(f"Part one = {max([i * (2020-i) if 2020-i in ints else 0 for i in ints])}")
print(f"Part two = {max([i * j * (2020 - (i + j)) if 2020 - (i + j) in ints else 0 for i in ints for j in ints])}")