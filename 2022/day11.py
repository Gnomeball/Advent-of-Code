def print_simians(simians, rounds = 0):
    print(f"===== Simians after round {rounds} =====")
    for s in simians: print(s)
    print()

def do_business(simians, part_one = False):
    for s in simians: s.business(simians, part_one)

def doo_wop(value, op): # sh'bob
    left, o, right = op.split(" ")
    left = value # left is always the old value
    if right == "old": right = value
    if o == "+": return value + int(right)
    if o == "*": return value * int(right)

def panic_over(simians):
    inspections = sorted([ s.inspections for s in simians ])
    return inspections.pop() * inspections.pop()

class Stuff_Slinging_Simian:

    def __init__(self, text):
        text = [ line.strip() for line in text.split("\n") ]
        self.id = int(text[0][7:-1])
        self.items = [ int(item) for item in text[1][16:].split(",") ]
        self.inspections = 0
        self.op = text[2][17:]
        self.test = int(text[3][19:])
        self.if_true = int(text[4][25:])
        self.if_false = int(text[5][26:])

    def business(self, others, part_one = False):
        for i in range(len(self.items)):
            item = self.items.pop(0)
            self.inspections += 1
            new_value = doo_wop(item, self.op)
            if part_one: new_value = int(new_value / 3)
            boredom = new_value % 9699690 # Speeeeeeed
            pass_to = self.if_true if boredom % self.test == 0 else self.if_false
            others[ pass_to ].items.append(boredom)

    def __repr__(self, full = False):
        if full:
            return f"Monkey {self.id} has items {self.items}, their operation is \"{self.op}\", their test is to div by {self.test}, and will throw to {self.if_true} if true, else {self.if_false}"
        return f"Monkey {self.id} has done {self.inspections} inspections, and now has items {self.items}"

with open("data/day11.txt") as file:
    simians = [ Stuff_Slinging_Simian(s) for s in file.read().split("\n\n") ]
print_simians(simians)

for r in range(1, 21):
    do_business(simians, part_one = True)
    print_simians(simians, r)

print(f"Part one = {panic_over(simians)}")

with open("data/day11.txt") as file:
    simians = [ Stuff_Slinging_Simian(s) for s in file.read().split("\n\n") ]

for r in range(1, 10001):
    do_business(simians)

print(f"Part two = {panic_over(simians)}")