
# Trying to write ths after sherry was a bad idea ..
# took me ages to find the bug :D

# Anyway ..

SNAFU = { 0: ("0", "0"), # Encodes,      and decodes
          1: ("0", "1"), -1: ("0", "-"),   "=": -2,
          2: ("0", "2"), -2: ("0", "="),   "-": -1,
          3: ("1", "="), -3: ("-", "2"),   "0":  0,
          4: ("1", "-"), -4: ("-", "1"),   "1":  1,
          5: ("1", "0"), -5: ("-", "0"),   "2":  2 }

with open("data/day25.txt") as file:
    snafus = file.read().splitlines()

# Put the first number into our accumulator
ACC = snafus.pop(0).rjust(32, "0")

# Set the carry
carry = "0"

for snafu in snafus:
    # Get the snafu, and pad it to the length of our regiser
    snafu = snafu.rjust(32, "0")

    # Wait, register?

    # Yep, we just add them!
    result = ""

    # For each char, going right to left
    for c in range(-1, -32, -1):
        # Sum the two chars, and the carry
        snafu_sum = sum([ SNAFU[ACC[c]], SNAFU[snafu[c]], SNAFU[carry] ])
        # Map the result through our enode-decode map
        carry, next_snafu = SNAFU.get(snafu_sum, ("0", str(snafu_sum)))
        # And sum these together into the result
        result = next_snafu + result

    # Update our accumulator
    ACC = result

print(f"Part one = {ACC.lstrip('0')}")
