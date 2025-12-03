with open("data/day3.txt") as file:
    banks = file.read().splitlines()

def index_max_single_joltage(bank):
    # find the first index of the maximum value
    return bank.index(str(max(int(_) for _ in bank)))

def find_max_joltage_from(bank, remaining):
    # if we have nothing left to grab, exit recursion
    if (remaining == 0): return ""
    # for the nth number we only need to check up to the last n-1 digits
    index = index_max_single_joltage(bank[:1 + len(bank) - remaining])
    # return that value, appended with those of the remaining digits, recursively
    return bank[index] + find_max_joltage_from(bank[index + 1:], remaining - 1)

print("Part one = ", sum(int(find_max_joltage_from(bank,  2)) for bank in banks))
print("Part two = ", sum(int(find_max_joltage_from(bank, 12)) for bank in banks))
