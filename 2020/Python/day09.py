with open("data/day09.txt", "r") as file:
    numbers = [int(n) for n in file.read().splitlines()]

invalid = [numbers[n] for n in range(25, len(numbers)-1) if not [*[True for b in numbers[n-25:n] if numbers[n] - b in numbers[n-25:n]] + [False]][0]][0]

weakness = [sum([min(numbers[a:n]), max(numbers[a:n])]) for a in range(0, len(numbers)) for n in range(a, len(numbers)) if sum(numbers[a:n]) == invalid][0]

print(f"Part one = {invalid}")
print(f"Part two = {weakness}")