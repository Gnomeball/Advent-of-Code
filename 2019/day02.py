with open("data/day02.txt") as file:
    program = list(map(int, file.read().split(",")))

def debug_three(op, a, b, c, d):
    print(f"{op} [ {a} ] and [ {b} ] for [ {c} ] into [ {d} ]")

def initialise(noun, verb, prgm):
    prgm[1] = noun
    prgm[2] = verb
    return prgm

def add(ptr, prgm):
    left = prgm[prgm[ptr + 1]]
    right = prgm[prgm[ptr + 2]]
    result = left + right
    if DEBUG: debug_three("Adding", left, right, result, prgm[ptr+3])
    prgm[prgm[ptr + 3]] = result
    return ptr + 4, prgm

def multiply(ptr, prgm):
    left = prgm[prgm[ptr + 1]]
    right = prgm[prgm[ptr + 2]]
    result = left * right
    if DEBUG: debug_three("Multiplying", left, right, result, prgm[ptr+3])
    prgm[prgm[ptr + 3]] = result
    return ptr + 4, prgm

def run(state, prgm):
    ip = 0

    prgm = initialise(*state, prgm)

    while prgm[ip] != 99:

        if DEBUG: print(f"Found {prgm[ip]}", end = "")

        if prgm[ip] == 1:
            if DEBUG: print(f" [ ADD ] at [ {ip} ]")
            ip, prgm = add(ip, prgm)
        elif prgm[ip] == 2:
            if DEBUG: print(f" [ MULTIPLY ] at [ {ip} ]")
            ip, prgm = multiply(ip, prgm)

        if DEBUG: print(f"State = {prgm}\n")

    if DEBUG: print(f"Program finished!\n\nResult = {prgm}\n")

    return prgm

DEBUG = True

state = [ 12, 2 ]
result = run(state, program.copy())
print(f"Part one = {result[0]}")

# The below is spam central
DEBUG = False

# I have a feeling the noun will be toward the upper end ...
states = [ [ noun, verb ] for noun in reversed(range(100)) for verb in range(100) ]

for state in states:
    result = run(state, program.copy())
    if result[0] == 19690720: break

noun, verb = state
print(f"Part two = {100 * noun + verb}")
