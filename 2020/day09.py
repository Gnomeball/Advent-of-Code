with open("data/day09.txt", "r") as file:
    numbers = [int(n) for n in file.read().splitlines()]

# def pairSum(number, numbers):
#     return [*[True for b in numbers if number - b in numbers] + [False]][0]
#     for n in numbers:
#         if number - n in numbers:
#             return True
#     return False

# Part 1

invalid = [numbers[n] for n in range(25, len(numbers)-1) if not [*[True for b in numbers[n-25:n] if numbers[n] - b in numbers[n-25:n]] + [False]][0]][0]

print(invalid)

# Part 2

weakness = [sum([min(numbers[a:n]), max(numbers[a:n])]) for a in range(0, len(numbers)) for n in range(a, len(numbers)) if sum(numbers[a:n]) == invalid][0]

print(weakness)
