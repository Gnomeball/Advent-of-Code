# The first attempt.. clear but possibly ungainly

# elf_sums = []

# with open("data/day01.txt") as file:
#     elf = []
#     for c in file.read().splitlines():
#         if c != "":
#             elf.append(int(c))
#         else:
#             elf_sums.append(sum(elf))
#             elf = []

# print(f"Part one = {max(elf_sums)}")
# print(f"Part two = {sum(sorted(elf_sums)[-3:])}")



# The second attempt.. less clear, and somehow even more ungainly?

# with open("data/day01.txt") as file:
#     calories = file.read().split("\n\n")
#     elfs = [ [ int(snack) for snack in elf.split("\n") ] for elf in calories ]
#     elf_sums = [ sum(snacks) for snacks in elfs ]
#     elf_sums = sorted(elf_sums, reverse = True)

# print(f"Part one = {elf_sums[0]}")
# print(f"Part two = {sum(elf_sums[0:3])}")



# And because am bored.. does this even work?

with open("data/day01.txt") as file:
    elf_sums = sorted(
        [ sum(snacks) for snacks in [
            [ int(snack) for snack in elf.split() ]
                for elf in file.read().split("\n\n")
        ] ], reverse = True
    )[0:3]

# Ideally you would probably map sum(index->end), but I can't workout the one liner
# print(f"Part one = {elf_sums[0]}\nPart two = {sum(elf_sums)}")

in_place_total = [ sum(elf_sums[0:n+1]) for n in range(3) ] # Kinda like that
print(f"Part one = {in_place_total[0]}\nPart two = {in_place_total[2]}")



# Or, here we go - after a nudge :D

# print("Part one = {0[0]}\nPart two = {1}".format(
#     elves := sorted([ sum(snacks) for snacks in [
#         [ int(snack) for snack in elf.split() ]
#         for elf in open("data/day01.txt").read().split("\n\n") ]
#     ], reverse = True), sum(elves[0:3])))
    # This is weirdly a syntax error though


print("Part one = {0[0]}\nPart two = {1}".format(
    elves:= list(sorted(list(*[ map(sum, [ list(map(int, elf.split()))
        for elf in open("data/day01.txt").read().split("\n\n") ] )
    ]))[-3:]), sum(elves)))
