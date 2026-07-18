# Read in the input file

with open('data/day11.txt') as file:
    stones = list(map(int, file.read().split()))

# print(stones)

import functools # First time using this

@functools.cache
def count(stone, n_blinks, limit):
    # If we're done
    if n_blinks == limit:
        return 1

    # Otherwise

    # Zero becomes one
    if stone == 0:
        return count(1, n_blinks+1, limit)

    # Stones of even length are split into two
    stone_string = str(stone)
    stone_len = len(stone_string)

    if stone_len & 1 == 0:
        left  = int(stone_string[ : stone_len // 2   ])
        right = int(stone_string[   stone_len // 2 : ])
        return (count(left, n_blinks+1, limit) + count(right, n_blinks+1, limit))

    # Every other stone is multiplied by 2024
    return count(stone * 2024, n_blinks+1, limit)

print("Part one:", sum(count(stone, 0, 25) for stone in stones))
print("Part two:", sum(count(stone, 0, 75) for stone in stones))
