# If this is a jungle.. why no Lizard?

with open("data/day02.txt") as file:
    moves = file.read().splitlines()

# First attempt, clean-ish, if not a wee bit cheaty?

# scores_1 = dict({
#     "A X" : 3 + 1, "A Y" : 6 + 2, "A Z" : 0 + 3,
#     "B X" : 0 + 1, "B Y" : 3 + 2, "B Z" : 6 + 3,
#     "C X" : 6 + 1, "C Y" : 0 + 2, "C Z" : 3 + 3
# })

# my_score = sum([ scores_1[move] for move in moves ])
# print(f"Part one = {my_score}")

# scores_2 = dict({
#     "A X" : 0 + 3, "A Y" : 3 + 1, "A Z" : 6 + 2,
#     "B X" : 0 + 1, "B Y" : 3 + 2, "B Z" : 6 + 3,
#     "C X" : 0 + 2, "C Y" : 3 + 3, "C Z" : 6 + 1
# })

# my_score = sum([ scores_2[move] for move in moves ])
# print(f"Part two = {my_score}")

# And as a one-liner (minus IO)

print("Part one = {}".format(sum(list(map(lambda move: dict({ "A X" : 4, "A Y" : 8, "A Z" : 3, "B X" : 1, "B Y" : 5, "B Z" : 9, "C X" : 7, "C Y" : 2, "C Z" : 6 })[move], moves)))), "\nPart two = {}".format(sum(list(map(lambda move: dict({ "A X" : 3, "A Y" : 4, "A Z" : 8, "B X" : 1, "B Y" : 5, "B Z" : 9, "C X" : 2, "C Y" : 6, "C Z" : 7 })[move], moves)))))