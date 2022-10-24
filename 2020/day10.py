with open("data/day10.txt", "r") as file:
    adapters = sorted([int(a) for a in file.read().splitlines()])

# Part 1 -- This is not clean nor is it good

thing = sorted(["3"] + [str(z[1] - z[0]) for z in zip([0] + adapters, adapters)])

print(int(len(thing) - "".join(thing).count('1')) * int("".join(thing).count('1')))

# Part 2 -- This confused the heck out of me for hours

def chains(adapters: list):
    arrangements = 1
    combinations = {1: 1, 2: 1, 3: 2, 4: 4, 5: 7}
    current_rating = 0

    for i, jolts in enumerate(adapters[:-1], start = 1):
        if adapters[i] - jolts == 3:
            # Multiply by how many adapters it has been since a gap of 3
            arrangements *= combinations[i - current_rating]
            # print(f"{i} - {current_rating} = {i - current_rating} <--")
            current_rating = i

    return(arrangements)

print(chains([0] + adapters + [max(adapters) + 3]))
