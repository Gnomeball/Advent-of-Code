# Read in the file, by line

with open("data/day07.txt") as file:
    equations = [ list(map(int, line.replace(':','').split())) for line in file ]

# print(equations)

# Function to reduce a sum

from operator import add, mul

def concatenate(left, right):
    return int(f"{left}{right}")

def reduce_sum(values, operators):

    # If we've only got one number left

    if len(values) == 2:
        return values[0] == values[1]

    # Otherwise

    total, a, b, *rest = values

    for op in operators:
        if reduce_sum([total, op(a, b)] + rest, operators):
            return total

    return 0

# Part one

print(f"Part one: {sum(reduce_sum(nums, operators=[add, mul]) for nums in equations)}")

# Part two

print(f"Part one: {sum(reduce_sum(nums, operators=[add, mul, concatenate]) for nums in equations)}")
