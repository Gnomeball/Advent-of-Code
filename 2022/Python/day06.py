with open("data/day06.txt") as file:
    packet = file.read()

ends = [ [ len(set(packet[i:i+b])) == b for b in [4, 14] ] for i in range(len(packet)) ]

print(f"Part one = {ends.index([True, False]) + 4}")
print(f"Part two = {ends.index([True, True]) + 14}")


# with open("data/day06.txt") as file:
#     packet = file.read()
#     print("Part one = {0[0]}\nPart two = {0[1]}".format(
#         [ [ len(set(item))
#             for item in list(zip(*[packet[i:] for i in range(b)]))
#         ].index(b) + b for b in [4, 14] ]))


# print("Part one = {0[0]}\nPart two = {0[1]}".format([ [ len(set(item)) for item in list(zip(*[open("data/day06.txt").read()[i:] for i in range(b)])) ].index(b) + b for b in [4, 14] ]))

