from parse import *

def get_stacks():

    def build_stacks(stacks_in):
        stacks_out = [[], [], [], [], [], [], [], [], [], []]
        for stack in stacks_in:
            i, s = 1, 0
            while i < width:
                s += 1 # Next stack
                container = stack[i]
                i += 4
                if container == ' ': continue
                else: stacks_out[s].insert(0, container)
        # We don't pop this to save us from off by one errors later
        # stacks_out.pop(0)
        return stacks_out

    with open("data/day05.txt") as file:
        data = file.read().splitlines()
        # I don't like how these are hard-coded
        width  = len(data[7])
        stacks = [ stack.ljust(width) for stack in data[:8] ]
        moves  = [ parse("move {:d} from {:d} to {:d}", move)
                   for move in data[10:] ]

    stacks = build_stacks(stacks)
    return stacks, moves

def read_stacks(stacks):
    return "".join(stack[len(stack)-1] for stack in stacks[1:])

def part_one(stacks, moves):

    for move in moves:
        for _ in range(move[0]):
            container = stacks[move[1]].pop()
            stacks[move[2]].append(container)
        # [ stacks[move[2]].append(
        #   stacks[move[1]].pop()) for _ in range(move[0]) ]

    return read_stacks(stacks)

def part_two(stacks, moves):

    for move in moves:
        pile = []
        for _ in range(move[0]):
            container = stacks[move[1]].pop()
            pile.insert(0, container)
        stacks[move[2]] += pile
        # stacks[move[2]] += reversed(
        #   [ stacks[move[1]].pop() for _ in range(move[0]) ])

    return read_stacks(stacks)

print(f"Part one = {part_one(*get_stacks())}")
print(f"Part two = {part_two(*get_stacks())}")
