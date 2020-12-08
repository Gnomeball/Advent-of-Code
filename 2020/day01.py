with open("day01.txt", "r") as file:
    ints = [int(i) for i in file.read().splitlines()]

# Part 1

print(max([i * (2020-i) if 2020-i in ints else 0 for i in ints]))

# Part 2

print(max([i * j * (2020 - (i + j)) if 2020 - (i + j) in ints else 0 for i in ints for j in ints]))