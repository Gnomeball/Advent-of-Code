from parse import *

with open("data/day04.txt") as file:
    ranges = [ parse("{:d}-{:d},{:d}-{:d}", line) for line in file.read().splitlines() ]

# for r in ranges:
#     if (r[0] >= r[2] and r[1] <= r[3]) or (r[2] >= r[0] and r[3] <= r[1]):
#         held_entirely_within += 1

held_entirely_within = sum([
    1 if (r[0] >= r[2] and r[1] <= r[3])
      or (r[2] >= r[0] and r[3] <= r[1])
    else 0
    for r in ranges ])

print(f"Part one = {held_entirely_within}")

# def groups_overlap(s_1, e_1, s_2, e_2):
#     if e_1 >= s_2 and s_1 <= e_2: # They overlap \ way
#         return True
#     if e_2 >= s_1 and e_1 >= s_2: # They overlap / way
#         return True
#     return False

# def groups_overlap(s_1, e_1, s_2, e_2):
#     return (e_1 >= s_2 and s_1 <= e_2) or (e_2 >= s_1 and e_1 >= s_2)

# overlap_only_a_bit = 0

# for r in ranges:
#     if groups_overlap(*r):
#         overlap_only_a_bit += 1

# for r in ranges:
#     if (r[1] >= r[2] and r[0] <= r[3]) or (r[3] >= r[0] and r[1] >= r[2]):
#         overlap_only_a_bit += 1

overlap_only_a_bit = sum([
    1 if (r[1] >= r[2] and r[0] <= r[3])
      or (r[3] >= r[0] and r[1] >= r[2])
    else 0
    for r in ranges])

print(f"Part two = {overlap_only_a_bit}")



# Tradition demands it..

print(f"Part one = {sum( 1 if (r[0] >= r[2] and r[1] <= r[3]) or (r[2] >= r[0] and r[3] <= r[1]) else 0 for r in ranges )}\nPart two = {sum( 1 if (r[1] >= r[2] and r[0] <= r[3]) or (r[3] >= r[0] and r[1] >= r[2]) else 0 for r in ranges )}")



# Ok now this is silly

# print("Part one = {0[0]}\nPart two = {0[1]}".format([sum(tup) for tup in zip(*[
#          (1, 1) if ((r[1] >= r[2] and r[0] <= r[3]) or (r[3] >= r[0] and r[1] >= r[2]))
#                and ((r[0] >= r[2] and r[1] <= r[3]) or (r[2] >= r[0] and r[3] <= r[1]))
#     else (1, 0) if  (r[0] >= r[2] and r[1] <= r[3]) or (r[2] >= r[0] and r[3] <= r[1])
#     else (0, 1) if  (r[1] >= r[2] and r[0] <= r[3]) or (r[3] >= r[0] and r[1] >= r[2])
#     else (0, 0)
#     for r in [ parse("{:d}-{:d},{:d}-{:d}", line)
#     for line in open("data/day04.txt").read().splitlines() ]
# ])]))



# Now drop the import ..

print("Part one = {0[0]}\nPart two = {0[1]}".format([sum(tup) for tup in zip(*[
         (1, 1) if ((r[1] >= r[2] and r[0] <= r[3]) or (r[3] >= r[0] and r[2] <= r[1]))
               and ((r[0] >= r[2] and r[1] <= r[3]) or (r[2] >= r[0] and r[3] <= r[1]))
    else (1, 0) if  (r[0] >= r[2] and r[1] <= r[3]) or (r[2] >= r[0] and r[3] <= r[1])
    else (0, 1) if  (r[1] >= r[2] and r[0] <= r[3]) or (r[3] >= r[0] and r[2] <= r[1])
    else (0, 0)
    for r in [ list(map(int, line.replace("-", ",").split(",")))
    for line in open("data/day04.txt").read().splitlines() ]
])]))
