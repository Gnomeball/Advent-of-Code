# Read in both input files, each by line

with open("data/day05-rules.txt") as file:
    rules = sorted([ tuple(map(int, line.split("|"))) for line in file.read().splitlines() ])

with open("data/day05-updates.txt") as file:
    updates = [ list(map(int, line.split(","))) for line in file.read().splitlines() ]

# Function to verify an update

def verify_update(update, rules) -> bool:

    for rule in rules:
        left, right = rule
        if left in update and right in update:
            if update.index(left) > update.index(right):
                return False

    return True

# Split the updates in to correct and incorrect

correct, incorrect = [], []

for update in updates:
    if verify_update(update, rules):
        correct.append(update)
    else:
        incorrect.append(update)

# Function to print middle item from an update

def get_middle(update) -> int:
    return update[int((len(update)-1)/2)]

# Part one; accumulate the middles of correct updates

total = sum([ get_middle(update) for update in correct ])

print(f"Part one: {total}")

# Part two; reorder incorrect updates to make them correct, then accumulate the middles

rules_that_apply = []

for update in incorrect:
    applicable_rules = []
    for rule in rules:
        left, right = rule
        if left in update and right in update:
            applicable_rules.append(rule)
    rules_that_apply.append(applicable_rules)
    # print(update)

# for rta in rules_that_apply:
#     print(rta)

# Function to swap two pages in an update list

def swap(update, index_l, index_r):
    temp = update[index_l]
    update[index_l] = update[index_r]
    update[index_r] = temp
    return update

# Function to reorder an update to match applicable rules

def reorder_update(update, rules):

    # print(update)
    # print(rules)

    while not verify_update(update, rules): # I dun lyke this!
        for rule in rules:
            left, right = rule
            if update.index(left) > update.index(right):
                update = swap(update, update.index(left), update.index(right))

    # print(update)

    return update

reordered_updates = [ reorder_update(incorrect[i], rules_that_apply[i]) for i in range(0, len(incorrect)) ]

# for update in reordered_updates:
#     print(update)

# Print result

total = sum([ get_middle(update) for update in reordered_updates ])

print(f"Part two: {total}")
