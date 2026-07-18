with open("data/day09.txt") as file:
    program = list(map(int, file.read().split(",")))

for _ in range(1000):
    program.append(0)

# Debug

DEBUG = False

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
    DATA = []

    # Init

    def automated_input(self, data):
        if data != []:
            self.automated_input = True
            self.DATA = data

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
            value = self.DATA.pop(0)
            print(f"OpCode 3, taken automated input value : {value}")
        else:
            value = int(input("OpCode 3, expecting input : ").strip())

        mode = op.modes[0]

        match mode:
            case Parameter.POSITION.value:
                position = prgm[ptr + 1]
                if DEBUG: print(f"Storing {value} into position {position}")
            case Parameter.IMMEDIATE.value:
                position = prgm[ptr + 1]
                if DEBUG: print(f"Storing {value} into immediate position {position}")
            case Parameter.RELATIVE.value:
                position = self.RELATIVE_BASE + prgm[ptr + 1]
                if DEBUG: print(f"Storing {value} into relative position {position}")


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
                if DEBUG: print(f"Outputting {value} from position {position}")
            case Parameter.IMMEDIATE.value:
                value = prgm[ptr + 1]
                if DEBUG: print(f"Outputting {value} immediately")
            case Parameter.RELATIVE.value:
                position = self.RELATIVE_BASE + prgm[ptr + 1]
                value = prgm[position]
                if DEBUG: print(f"Outputting {value} from relative position {position}")

        print(f"OpCode 4, providing output : {value}")
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

            if DEBUG: print(f"Found {prgm[ip]}", end = "")

            op = OpCode(prgm[ip])

            # print(op)

            match op.code:
                case 1:
                    if DEBUG: print(f" [ ADD ] at [ {ip} ]")
                    ip, prgm = self.add(op, ip, prgm)
                case 2:
                    if DEBUG: print(f" [ MULTIPLY ] at [ {ip} ]")
                    ip, prgm = self.multiply(op, ip, prgm)
                case 3:
                    if DEBUG: print(f" [ INPUT ] at [ {ip} ]")
                    ip, prgm = self.take_input(op, ip, prgm)
                case 4:
                    if DEBUG: print(f" [ OUTPUT ] at [ {ip} ]")
                    ip, prgm = self.give_output(op, ip, prgm)
                case 5:
                    if DEBUG: print(f" [ JMP IF TRUE ] at [ {ip} ]")
                    ip, prgm = self.jump_if_true(op, ip, prgm)
                case 6:
                    if DEBUG: print(f" [ JMP IF FALSE ] at [ {ip} ]")
                    ip, prgm = self.jump_if_false(op, ip, prgm)
                case 7:
                    if DEBUG: print(f" [ LESS THAN ] at [ {ip} ]")
                    ip, prgm = self.less_than(op, ip, prgm)
                case 8:
                    if DEBUG: print(f" [ EQUAL ] at [ {ip} ]")
                    ip, prgm = self.equal(op, ip, prgm)
                case 9:
                    if DEBUG: print(f" [ ADJUST_RELATIVE_BASE ] at [ { ip } ]")
                    ip, prgm = self.adjust_relative_base(op, ip, prgm)
                    if DEBUG: print("Relative base is now :", self.RELATIVE_BASE)
                case _:
                    print(f"\nUnexpected OpCode found at [ {ip} ]")
                    print("State at exit :", prgm)
                    exit()

            if DEBUG: print(f"State = {prgm}\n")

        if DEBUG: print(f"Program finished!\n\nFinal State = {prgm}\n")

        return prgm

# Tasks

vm = IntCodeVM()

# vm.automated_input([2])

vm.run(program.copy())

# state = [ program[1], program[2] ]
# result = run(program.copy())
