with open("data/day08.txt", "r") as file:
    instructions = [(i[:3],int(i[4:])) for i in file.read().splitlines()]

def run_instructions(instructions):
    seen, pointer, accumulator = [], 0, 0
    while pointer not in seen:
        seen.append(pointer)
        instruction = instructions[pointer] if pointer in range(len(instructions)) else exit("EOF: " + str(accumulator))
        accumulator += instruction[1] if instruction[0] == "acc" else 0
        inc = instruction[1] if instruction[0] == "jmp" else 1
        pointer += inc
    return accumulator

# Part 1

print(run_instructions(instructions))

# Part 2

nopjmps = [i for i in range(len(instructions)) if instructions[i][0] in "nop jmp"]

for i in nopjmps:
    instructions_copy = [i for i in instructions]
    if instructions_copy[i][0] == "jmp":
        instructions_copy[i] = ("nop", instructions[i][1])
    elif instructions_copy[i][0] == "nop":
        instructions_copy[i] = ("jmp", instructions[i][1])
    run_instructions(instructions_copy)
