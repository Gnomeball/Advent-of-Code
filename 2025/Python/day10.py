# Used in part two

from numpy import transpose, ones_like
from scipy.optimize import linprog as linprog

with open("data/day10.txt") as file:
    states = []
    for line in file.read().splitlines():
        parts = line.split()
        states.append([
            tuple( int(x == '#') for x in parts[0].strip('[]') ),
            [ list(map(int, part.strip('()').split(','))) for part in parts[1:-1] ],
            list(map(int, parts[-1].strip('{}').split(',')))
        ])

# Function to press a button, and return the state after the press

def press_button(state, buttons):
    out_state = list(state)
    for b in buttons:
        out_state[b] = 1 - out_state[b]
    return tuple(out_state)

# Function to work out the presses for a line, returning the total number of presses

def solve(goal, buttons):
    start_state = tuple([0] * len(goal))
    button_presses = 0

    queue = [start_state]
    seen = set(queue)

    # While we have states to check
    while queue:
        # Collect up potential new states
        new_states = []
        # For each state we need to check for a path
        for state in queue:
            # If this state is the goal, we return
            if state == goal:
                return button_presses
            # Otherwise, we simulate pressing every button
            for button in buttons:
                next_state = press_button(state, button)
                # And if we haven't seen that state before, we add it to check next time
                if next_state not in seen:
                    seen.add(next_state)
                    new_states.append(next_state)
        # We set new states to check next time
        queue = new_states
        # And increase the number of buttons thus far presses
        button_presses += 1
    # If we run into any issues
    exit("Uh oh!")

# Keep track of overall presses required
presses_required = []

# For each state
for state in states:
    # Split the state into it's constituent parts
    goal, buttons, _ = state
    # Work out how many presses we need
    presses = solve(goal, buttons)
    # Accumulate the required presses
    presses_required.append(presses)

print("Part one =", sum(presses_required))

presses_required = []

# For each state
for state in states:

    # Split the state into it's constituent parts
    _, buttons, joltages = state

    # Abuse some Linear Programming (only a little)
    buttons_t = transpose([ [ 0 if i not in button else 1 for i in range(len(joltages)) ] for button in buttons])
    # This required a nudge, I don't really use scipy ever
    result = linprog(ones_like(buttons_t[0]), A_eq = buttons_t, b_eq = joltages, integrality = 1)

    solution = list(map(round, result.x))
    presses_required.append(sum(solution))

print("Part two =", sum(presses_required))
