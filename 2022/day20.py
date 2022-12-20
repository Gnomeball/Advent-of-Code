from collections import deque as circular_array

def shift():
    for i in range(len(data)):
        while data[0][0] != i: data.rotate()
        index, shift = data.popleft()
        data.rotate(-(shift % len(data)))
        data.appendleft((index, shift))

def number_shifting_shenanigans(iter=1):
    for _ in range(iter): shift()
    return data

def find_elfs(data):
    while data[0][1] != 0: data.rotate(-1)
    return sum([ data[1000][1], data[2000][1], data[3000][1] ])

# Part one

with open("data/day20.txt") as file:
    data = circular_array(enumerate(map(int, file.read().splitlines())))

print(f"Part one = {find_elfs(number_shifting_shenanigans())}")

# Part two

with open("data/day20.txt") as file:
    data = circular_array(enumerate((int(line) * 811589153 for line in file)))

print(f"Part two = {find_elfs(number_shifting_shenanigans(10))}")
