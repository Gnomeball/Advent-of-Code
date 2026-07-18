with open("data/day03.txt") as file:
    sacks = file.read().splitlines()

def open_sack(sack):
    length = int(len(sack) / 2)
    return sack[:length], sack[length:]

def in_both(left, right):
    return [ l for l in left if l in right ]

def priority(letter):
    # priority = ord(letter)
    # if priority >= 65 and priority <= 90:
    #     # upper
    #     return priority - 38
    # if priority >= 97 and priority <= 122:
    #     # lower
    #     return priority - 96
    return ord(letter) - 38 if ord(letter) >= 65 and ord(letter) <= 90 else ord(letter) - 96;

# The various iterations of this stupid one liner..

# total_p = sum([ priority(in_both(*open_sack(sack))[0]) for sack in sacks ])
# total_p = sum([ priority(in_both( sack[:int(len(sack)/2)], sack[int(len(sack)/2):] )[0]) for sack in sacks ])
# total_p = sum([ priority([ l for l in sack[:int(len(sack)/2)] if l in sack[int(len(sack)/2):] ][0]) for sack in sacks ])

# print(f"Part one = {total_p}")

print(f"Part one = {sum([ ord([ l for l in sack[:int(len(sack)/2)] if l in sack[int(len(sack)/2):] ][0]) - 38 if ord([ l for l in sack[:int(len(sack)/2)] if l in sack[int(len(sack)/2):] ][0]) >= 65 and ord([ l for l in sack[:int(len(sack)/2)] if l in sack[int(len(sack)/2):] ][0]) <= 90 else ord([ l for l in sack[:int(len(sack)/2)] if l in sack[int(len(sack)/2):] ][0]) - 96 for sack in sacks ])}")

# i = 0
# total_r = 0

# for i in range(int(len(sacks)/3)):
#     in_1_2 = in_both(sacks[i*3], sacks[i*3+1])
#     in_all = in_both(in_1_2, sacks[i*3+2])
#     total_r += priority(in_all[0])

# total_r = sum([ priority(in_both(in_both(sacks[i*3], sacks[i*3+1]), sacks[i*3+2])[0]) for i in range(int(len(sacks)/3)) ])

# print(f"Part two = {total_r}")

print(f"Part two = {sum([ ord([ l for l in [ l for l in sacks[i*3] if l in sacks[i*3+1] ] if l in sacks[i*3+2] ][0]) - 38 if ord([ l for l in [ l for l in sacks[i*3] if l in sacks[i*3+1] ] if l in sacks[i*3+2] ][0]) >= 65 and ord([ l for l in [ l for l in sacks[i*3] if l in sacks[i*3+1] ] if l in sacks[i*3+2] ][0]) <= 90 else ord([ l for l in [ l for l in sacks[i*3] if l in sacks[i*3+1] ] if l in sacks[i*3+2] ][0]) - 96 for i in range(int(len(sacks)/3)) ])}")

# And because tradition

# print(f"Part one = {sum([ ord([ l for l in sack[:int(len(sack)/2)] if l in sack[int(len(sack)/2):] ][0]) - 38 if ord([ l for l in sack[:int(len(sack)/2)] if l in sack[int(len(sack)/2):] ][0]) >= 65 and ord([ l for l in sack[:int(len(sack)/2)] if l in sack[int(len(sack)/2):] ][0]) <= 90 else ord([ l for l in sack[:int(len(sack)/2)] if l in sack[int(len(sack)/2):] ][0]) - 96 for sack in sacks ])}\nPart two = {sum([ ord([ l for l in [ l for l in sacks[i*3] if l in sacks[i*3+1] ] if l in sacks[i*3+2] ][0]) - 38 if ord([ l for l in [ l for l in sacks[i*3] if l in sacks[i*3+1] ] if l in sacks[i*3+2] ][0]) >= 65 and ord([ l for l in [ l for l in sacks[i*3] if l in sacks[i*3+1] ] if l in sacks[i*3+2] ][0]) <= 90 else ord([ l for l in [ l for l in sacks[i*3] if l in sacks[i*3+1] ] if l in sacks[i*3+2] ][0]) - 96 for i in range(int(len(sacks)/3)) ])}")