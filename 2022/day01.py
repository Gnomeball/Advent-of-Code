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

with open("data/day01.txt") as file:
    calories = file.read().split("\n\n")
    elfs = [ [int(snack) for snack in elf.split("\n")] for elf in calories]
    elf_sums = [ sum(snacks) for snacks in elfs ]
    elf_sums = sorted(elf_sums, reverse=True)

print(f"Part one = {elf_sums[0]}")
print(f"Part two = {sum(elf_sums[0:3])}")