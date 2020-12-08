with open("day08.txt", "r") as file:
    instructions = [(i[:3],int(i[4:])) for i in file.read().splitlines()]

def run_instructions(instructions):
    seen = []
    pointer = 0
    accumulator = 0

    while pointer not in seen:
        seen.append(pointer)
        instruction = instructions[pointer] if pointer in range(len(instructions)) else exit("EOF: " + str(accumulator))
        inc = 1
        if instruction[0] == "acc":
            accumulator += instruction[1]
        elif instruction[0] == "jmp":
            inc = instruction[1]
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

# nops = [i for i in range(len(instructions)) if instructions[i][0] == "nop"]
# jmps = [i for i in range(len(instructions)) if instructions[i][0] == "jmp"]

# for i in nops:
#     instructions_copy = [i for i in instructions]
#     instructions_copy[i] = ("jmp", instructions[i][1])
#     run_instructions(instructions_copy)

# # 327
# for i in jmps:
#     instructions_copy = [i for i in instructions]
#     instructions_copy[i] = ("nop", instructions[i][1])
#     run_instructions(instructions_copy)
