with open("data/day13.txt") as file:
    program = list(map(int, file.read().split(",")))

for _ in range(1000):
    program.append(0)

# Debug

DEBUG_OPS = False
DEBUG_STATE = False

# Classes

from enum import Enum

class Parameter(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2

class OpCode:

    def __init__(self, opcode):
        op_str = str(opcode).zfill(5)
        self.code = int(op_str[3:5])
        op_str = list(reversed(op_str))
        self.modes = [ int(_) for _ in op_str[2:5] ]

    def __str__(self):
        return f"OpCode : {self.code} {self.modes}"

class IntCodeVM:

    RELATIVE_BASE = 0

    automated_input = False
    INPUT_DATA = []

    SILENT_INPUT = False
    SILENT_OUTPUT = False

    OUTPUT_DATA = []

    # Game variables

    ball = []
    paddle = []

    score = []

    # Init

    def automated_input(self, data, silent_in=False, silent_out=False):
        if data != []:
            self.automated_input = True
            self.INPUT_DATA = data
            self.SILENT_INPUT = silent_in
            self.SILENT_OUTPUT = silent_out

    def add_to_input(self, value):
        self.INPUT_DATA.append(value)
        # print("Current Input Data :", self.INPUT_DATA)

    def toggle_silent_input(self):
        self.SILENT_INPUT = not self.SILENT_INPUT

    def toggle_silent_output(self):
        self.SILENT_INPUT = not self.SILENT_INPUT

    def silence(self):
        self.SILENT_INPUT = True
        self.SILENT_OUTPUT = True

    def get_output(self):
        return self.OUTPUT_DATA

    # Op Codes

    def add(self, op, ptr, prgm):
        """
        Opcode 1 adds together numbers read from two positions and stores the result in a third position.

        The three integers immediately after the opcode tell you these three positions:
        - the first two indicate the positions from which you should read the input values
        - the third indicates the position at which the output should be stored
        """

        mode_left = op.modes[0]
        mode_right = op.modes[1]
        mode_result = op.modes[2]

        # left = prgm[prgm[ptr + 1]] if mode_left == Parameter.POSITION.value else prgm[ptr + 1]

        match mode_left:
            case Parameter.POSITION.value:
                left = prgm[prgm[ptr + 1]]
            case Parameter.IMMEDIATE.value:
                left = prgm[ptr + 1]
            case Parameter.RELATIVE.value:
                left = prgm[self.RELATIVE_BASE + prgm[ptr + 1]]

        # right = prgm[prgm[ptr + 2]] if mode_right == Parameter.POSITION.value else prgm[ptr + 2]

        match mode_right:
            case Parameter.POSITION.value:
                right = prgm[prgm[ptr + 2]]
            case Parameter.IMMEDIATE.value:
                right = prgm[ptr + 2]
            case Parameter.RELATIVE.value:
                right = prgm[self.RELATIVE_BASE + prgm[ptr + 2]]

        result = left + right
        # if DEBUG: debug_three("Adding", left, right, result, prgm[ptr+3])

        # prgm[prgm[ptr + 3]] = result

        match mode_result:
            case Parameter.POSITION.value:
                prgm[prgm[ptr + 3]] = result
            # case Parameter.IMMEDIATE.value:
            #     prgm[ptr + 3] = result
            case Parameter.RELATIVE.value:
                prgm[self.RELATIVE_BASE + prgm[ptr + 3]] = result

        return ptr + 4, prgm

    def multiply(self, op, ptr, prgm):
        """
        Opcode 2 multiplies together numbers read from two positions and stores the result in a third position.

        The three integers immediately after the opcode tell you these three positions:
        - the first two indicate the positions from which you should read the input values
        - the third indicates the position at which the output should be stored
        """

        mode_left = op.modes[0]
        mode_right = op.modes[1]
        mode_result = op.modes[2]

        # left = prgm[prgm[ptr + 1]] if mode_left == Parameter.POSITION.value else prgm[ptr + 1]

        match mode_left:
            case Parameter.POSITION.value:
                left = prgm[prgm[ptr + 1]]
            case Parameter.IMMEDIATE.value:
                left = prgm[ptr + 1]
            case Parameter.RELATIVE.value:
                left = prgm[self.RELATIVE_BASE + prgm[ptr + 1]]

        # right = prgm[prgm[ptr + 2]] if mode_right == Parameter.POSITION.value else prgm[ptr + 2]

        match mode_right:
            case Parameter.POSITION.value:
                right = prgm[prgm[ptr + 2]]
            case Parameter.IMMEDIATE.value:
                right = prgm[ptr + 2]
            case Parameter.RELATIVE.value:
                right = prgm[self.RELATIVE_BASE + prgm[ptr + 2]]

        result = left * right
        # if DEBUG: debug_three("Multiplying", left, right, result, prgm[ptr+3])

        # prgm[prgm[ptr + 3]] = result

        match mode_result:
            case Parameter.POSITION.value:
                prgm[prgm[ptr + 3]] = result
            # case Parameter.IMMEDIATE.value:
            #     prgm[ptr + 3] = result
            case Parameter.RELATIVE.value:
                prgm[self.RELATIVE_BASE + prgm[ptr + 3]] = result

        return ptr + 4, prgm

    def take_input(self, op, ptr, prgm):
        """
        Opcode 3 takes a single integer as input and saves it to the position given by its only parameter.

        - For example, the instruction 3,50 would take an input value and store it at address 50
        """

        if self.automated_input == True:
            value = self.INPUT_DATA.pop(0)
            if not self.SILENT_INPUT: print(f"OpCode 3, taken automated input value : {value}")
        else:
            value = int(input("OpCode 3, expecting input : ").strip())

        mode = op.modes[0]

        match mode:
            case Parameter.POSITION.value:
                position = prgm[ptr + 1]
                if DEBUG_OPS: print(f"Storing {value} into position {position}")
            case Parameter.IMMEDIATE.value:
                position = prgm[ptr + 1]
                if DEBUG_OPS: print(f"Storing {value} into immediate position {position}")
            case Parameter.RELATIVE.value:
                position = self.RELATIVE_BASE + prgm[ptr + 1]
                if DEBUG_OPS: print(f"Storing {value} into relative position {position}")


        prgm[position] = value
        return ptr + 2, prgm

    def give_output(self, op, ptr, prgm):
        """
        Opcode 4 outputs the value of its only parameter.

        - For example, the instruction 4,50 would output the value at address 50
        """

        mode = op.modes[0]

        match mode:
            case Parameter.POSITION.value:
                position = prgm[ptr + 1]
                value = prgm[position]
                if DEBUG_OPS: print(f"Outputting {value} from position {position}")
            case Parameter.IMMEDIATE.value:
                value = prgm[ptr + 1]
                if DEBUG_OPS: print(f"Outputting {value} immediately")
            case Parameter.RELATIVE.value:
                position = self.RELATIVE_BASE + prgm[ptr + 1]
                value = prgm[position]
                if DEBUG_OPS: print(f"Outputting {value} from relative position {position}")

        self.OUTPUT_DATA.append(value)

        if not self.SILENT_OUTPUT: print(f"OpCode 4, providing output : {value}")
        return ptr + 2, prgm

    def jump_if_true(self, op, ptr, prgm):
        """
        Opcode 5 is jump-if-true
        - if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter
        - otherwise, it does nothing
        """

        mode_first = op.modes[0]
        mode_second = op.modes[1]

        # first = prgm[prgm[ptr + 1]] if mode_first == Parameter.POSITION.value else prgm[ptr + 1]

        match mode_first:
            case Parameter.POSITION.value:
                first = prgm[prgm[ptr + 1]]
            case Parameter.IMMEDIATE.value:
                first = prgm[ptr + 1]
            case Parameter.RELATIVE.value:
                first = prgm[self.RELATIVE_BASE + prgm[ptr + 1]]

        # second = prgm[prgm[ptr + 2]] if mode_second == Parameter.POSITION.value else prgm[ptr + 2]

        match mode_second:
            case Parameter.POSITION.value:
                second = prgm[prgm[ptr + 2]]
            case Parameter.IMMEDIATE.value:
                second = prgm[ptr + 2]
            case Parameter.RELATIVE.value:
                second = prgm[self.RELATIVE_BASE + prgm[ptr + 2]]

        if first != 0:
            ptr = second
            return ptr, prgm
        else:
            return ptr + 3, prgm

    def jump_if_false(self, op, ptr, prgm):
        """
        Opcode 6 is jump-if-false
        - if the first parameter is zero, it sets the instruction pointer to the value from the second parameter
        - otherwise, it does nothing
        """

        mode_first = op.modes[0]
        mode_second = op.modes[1]

        # first = prgm[prgm[ptr + 1]] if mode_first == Parameter.POSITION.value else prgm[ptr + 1]

        match mode_first:
            case Parameter.POSITION.value:
                first = prgm[prgm[ptr + 1]]
            case Parameter.IMMEDIATE.value:
                first = prgm[ptr + 1]
            case Parameter.RELATIVE.value:
                first = prgm[self.RELATIVE_BASE + prgm[ptr + 1]]

        # second = prgm[prgm[ptr + 2]] if mode_second == Parameter.POSITION.value else prgm[ptr + 2]

        match mode_second:
            case Parameter.POSITION.value:
                second = prgm[prgm[ptr + 2]]
            case Parameter.IMMEDIATE.value:
                second = prgm[ptr + 2]
            case Parameter.RELATIVE.value:
                second = prgm[self.RELATIVE_BASE + prgm[ptr + 2]]

        if first == 0:
            ptr = second
            return ptr, prgm
        else:
            return ptr + 3, prgm

    def less_than(self, op, ptr, prgm):
        """
        Opcode 7 is less than
        - if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter
        - otherwise, it stores 0
        """

        mode_first = op.modes[0]
        mode_second = op.modes[1]
        mode_third = op.modes[2]

        # first = prgm[prgm[ptr + 1]] if mode_first == Parameter.POSITION.value else prgm[ptr + 1]

        match mode_first:
            case Parameter.POSITION.value:
                first = prgm[prgm[ptr + 1]]
            case Parameter.IMMEDIATE.value:
                first = prgm[ptr + 1]
            case Parameter.RELATIVE.value:
                first = prgm[self.RELATIVE_BASE + prgm[ptr + 1]]

        # second = prgm[prgm[ptr + 2]] if mode_second == Parameter.POSITION.value else prgm[ptr + 2]

        match mode_second:
            case Parameter.POSITION.value:
                second = prgm[prgm[ptr + 2]]
            case Parameter.IMMEDIATE.value:
                second = prgm[ptr + 2]
            case Parameter.RELATIVE.value:
                second = prgm[self.RELATIVE_BASE + prgm[ptr + 2]]

        match mode_third:
            case Parameter.POSITION.value:
                prgm[prgm[ptr + 3]] = 1 if first < second else 0
            # case Parameter.IMMEDIATE.value:
            #     prgm[ptr + 3] = 1 if first < second else 0
            case Parameter.RELATIVE.value:
                prgm[self.RELATIVE_BASE + prgm[ptr + 3]] = 1 if first < second else 0

        return ptr + 4, prgm

    def equal(self, op, ptr, prgm):
        """
        Opcode 8 is equals
        - if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter
        - otherwise, it stores 0
        """

        mode_first = op.modes[0]
        mode_second = op.modes[1]
        mode_third = op.modes[2]

        # first = prgm[prgm[ptr + 1]] if mode_first == Parameter.POSITION.value else prgm[ptr + 1]

        match mode_first:
            case Parameter.POSITION.value:
                first = prgm[prgm[ptr + 1]]
            case Parameter.IMMEDIATE.value:
                first = prgm[ptr + 1]
            case Parameter.RELATIVE.value:
                first = prgm[self.RELATIVE_BASE + prgm[ptr + 1]]

        # second = prgm[prgm[ptr + 2]] if mode_second == Parameter.POSITION.value else prgm[ptr + 2]

        match mode_second:
            case Parameter.POSITION.value:
                second = prgm[prgm[ptr + 2]]
            case Parameter.IMMEDIATE.value:
                second = prgm[ptr + 2]
            case Parameter.RELATIVE.value:
                second = prgm[self.RELATIVE_BASE + prgm[ptr + 2]]

        match mode_third:
            case Parameter.POSITION.value:
                prgm[prgm[ptr + 3]] = 1 if first == second else 0
            # case Parameter.IMMEDIATE.value:
            #     prgm[ptr + 3] = 1 if first == second else 0
            case Parameter.RELATIVE.value:
                prgm[self.RELATIVE_BASE + prgm[ptr + 3]] = 1 if first == second else 0

        return ptr + 4, prgm

    def adjust_relative_base(self, op, ptr, prgm):
        """
        Opcode 9 adjusts the relative base by the value of its only parameter.

        - the relative base increases (or decreases, if the value is negative) by the value of the parameter
        """

        mode = op.modes[0]

        match mode:
            case Parameter.POSITION.value:
                value = prgm[prgm[ptr + 1]]
            case Parameter.IMMEDIATE.value:
                value = prgm[ptr + 1]
            case Parameter.RELATIVE.value:
                value = prgm[self.RELATIVE_BASE + prgm[ptr + 1]]

        self.RELATIVE_BASE += value

        return ptr + 2, prgm

    # Run

    def run(self, prgm):
        ip = 0

        # prgm = initialise(*state, prgm)

        while prgm[ip] != 99:

            if DEBUG_OPS: print(f"Found {prgm[ip]}", end = "")

            op = OpCode(prgm[ip])

            # print(op)

            match op.code:
                case 1:
                    if DEBUG_OPS: print(f" [ ADD ] at [ {ip} ]")
                    ip, prgm = self.add(op, ip, prgm)
                case 2:
                    if DEBUG_OPS: print(f" [ MULTIPLY ] at [ {ip} ]")
                    ip, prgm = self.multiply(op, ip, prgm)
                case 3:
                    if DEBUG_OPS: print(f" [ INPUT ] at [ {ip} ]")

                    # print(f"Ball position : {self.ball[:2]}")
                    # print(f"Paddle position : {self.paddle[:2]}")

                    potential = self.ball[0] - self.paddle[0]
                    # print(f"Move could be? : {potential}")

                    if len(self.INPUT_DATA) == 0:
                        self.add_to_input(potential)

                    ip, prgm = self.take_input(op, ip, prgm)
                case 4:
                    if DEBUG_OPS: print(f" [ OUTPUT ] at [ {ip} ]")
                    ip, prgm = self.give_output(op, ip, prgm)

                    if len(self.OUTPUT_DATA) % 3 == 0:
                        previous_state = self.OUTPUT_DATA[-3:]
                        if previous_state[2] == 3: # paddle
                            self.paddle = previous_state
                        if previous_state[2] == 4: # ball
                            self.ball = previous_state
                        if previous_state[0] == -1: # score
                            self.score = previous_state
                            # print(f"Current score : {self.score[2]}")
                        # print("previous state :", self.OUTPUT_DATA[-3:])

                case 5:
                    if DEBUG_OPS: print(f" [ JMP IF TRUE ] at [ {ip} ]")
                    ip, prgm = self.jump_if_true(op, ip, prgm)
                case 6:
                    if DEBUG_OPS: print(f" [ JMP IF FALSE ] at [ {ip} ]")
                    ip, prgm = self.jump_if_false(op, ip, prgm)
                case 7:
                    if DEBUG_OPS: print(f" [ LESS THAN ] at [ {ip} ]")
                    ip, prgm = self.less_than(op, ip, prgm)
                case 8:
                    if DEBUG_OPS: print(f" [ EQUAL ] at [ {ip} ]")
                    ip, prgm = self.equal(op, ip, prgm)
                case 9:
                    if DEBUG_OPS: print(f" [ ADJUST_RELATIVE_BASE ] at [ { ip } ]")
                    ip, prgm = self.adjust_relative_base(op, ip, prgm)
                    if DEBUG_OPS: print("Relative base is now :", self.RELATIVE_BASE)
                case _:
                    print(f"\nUnexpected OpCode found at [ {ip} ]")
                    print("State at exit :", prgm)
                    exit()

            if DEBUG_STATE: print(f"State = {prgm}\n")

        if DEBUG_STATE: print(f"Program finished!\n\nFinal State = {prgm}\n")

        return prgm

# Tasks

vm = IntCodeVM()
vm.automated_input([0,0,0])
vm.silence()
vm.run(program.copy())

out = vm.get_output()


states = [ out[i:i + 3] for i in range(0, len(out), 3) ]

# print(len(states))

initial_state = states[:1035]
updates = states[1035:]

# print(initial_state)
# print(updates)

max_x = 0
max_y = 0

# 0 is an empty tile. No game object appears in this tile.
empty = set()
# 1 is a wall tile. Walls are indestructible barriers.
walls = set()
# 2 is a block tile. Blocks can be broken by the ball.
blocks = set()
# 3 is a horizontal paddle tile. The paddle is indestructible.
paddle = set()
# 4 is a ball tile. The ball moves diagonally and bounces off objects.
ball = set()

# ?
scores = []

for state in initial_state:
    # print(state)
    x, y, t = state

    # get play area size
    if x > max_x: max_x = x
    if y > max_y: max_y = y

    if x == -1 and y == 0:
        scores.append(state)

    # collect tiles
    match t:
        case 0: empty.add((x, y))
        case 1: walls.add((x, y))
        case 2: blocks.add((x, y))
        case 3: paddle.add((x, y))
        case 4: ball.add((x, y))

# print("Part one =", len(blocks))

# print(empty)
# print(walls)
# print(blocks)
# print(paddle)
# print(ball)

play_area = [ [ "." for x in range(0, max_x+1) ] for y in range(0, max_y+1) ]

# print(play_area)

for e in empty:
    x, y = e
    play_area[y][x] = " "

for w in walls:
    x, y = w
    play_area[y][x] = "#"

for b in blocks:
    x, y = b
    play_area[y][x] = "@"

for p in paddle:
    x, y = p
    play_area[y][x] = "-"

for b in ball:
    x, y = b
    play_area[y][x] = "*"

# print(play_area)

# for line in play_area:
#     print("".join(line))

# print("Score tracker = ", scores)

# print(states)

# initial_score = updates.pop(0)
final_score = updates.pop()

# print(updates)

# state_changes = [ updates[i:i + 2] for i in range(0, len(updates), 2) ]

# print(state_changes)

# for line in play_area:
#     print("".join(line))

# for change in state_changes:
#     try:
#         prev, new = change
#         if new[2] == 3:
#             # paddle
#             play_area[prev[1]][prev[0]] = " "
#             play_area[new[1]][new[0]] = "-"
#         if new[2] == 4:
#             # ball
#             play_area[prev[1]][prev[0]] = " "
#             play_area[new[1]][new[0]] = "*"
#         if new[0] == -1:
#             # score
#             play_area[prev[1]][prev[0]] = " "
#         print(change)
#         for line in play_area:
#             print("".join(line))
#     except ValueError:
#         print(change)

print("Final score =", final_score[2])
