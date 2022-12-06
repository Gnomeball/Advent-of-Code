from parse import *

def get_stacks():

    with open("data/day05.txt") as file:
        data = file.read().splitlines()
        # gap = data.index("")

        # v_stacks = [ stack.ljust(len(data[gap-2])) for stack in data[:gap] ]
        # h_stacks = [ list(reversed(stack)) for stack in list(zip(*v_stacks)) ]
        # stacks = [ [ c for c in "".join(h_stacks[i])[1:].strip() ] for i in range(1, len(data[gap-2]), 4) ]

    # return stacks, moves

    # return [ [ c for c in "".join([ list(reversed(stack)) for stack in list(zip(*[ stack.ljust(len(data[data.index("")-2])) for stack in data[:data.index("")] ])) ][i])[1:].strip() ] for i in range(1, len(data[data.index("")-2]), 4) ], [ parse("move {:d} from {:d} to {:d}", move) for move in data[data.index("")+1:] ]

    return [ [ c for c in "".join([ list(reversed(stack))
                 for stack in list(zip(*[ stack.ljust(len(data[data.index("")-2]))
                 for stack in data[:data.index("")] ])) ][i])[1:].strip()
             ]   for i in range(1, len(data[data.index("")-2]), 4)
           ], [
             parse("move {:d} from {:d} to {:d}", move)
             for move in data[data.index("")+1:]
           ]

# def read_stacks(stacks):
#     return "".join(stack[len(stack)-1] for stack in stacks[1:])

def part_one(stacks, moves):

    # for move in moves:
    #     for _ in range(move[0]):
    #         container = stacks[move[1]].pop()
    #         stacks[move[2]].append(container)

    [ [ stacks[move[2]-1].append(stacks[move[1]-1].pop()) for _ in range(move[0]) ] for move in moves ]

    # return read_stacks(stacks)
    return "".join(stack[len(stack)-1] for stack in stacks)

def part_two(stacks, moves):

    for move in moves:
        # pile = []
        # for _ in range(move[0]):
        #     container = stacks[move[1]].pop()
        #     pile.insert(0, container)
        # stacks[move[2]] += pile
        stacks[move[2]-1] += reversed([ stacks[move[1]-1].pop() for _ in range(move[0]) ])

    # return read_stacks(stacks)
    return "".join(stack[len(stack)-1] for stack in stacks)

print(f"Part one = {part_one(*get_stacks())}")
print(f"Part two = {part_two(*get_stacks())}")
