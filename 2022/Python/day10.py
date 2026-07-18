with open("data/day10.txt") as file:
    reg, cycles = 1, []
    for i in file.read().splitlines():
        cycles.append(reg)
        if i == "noop": continue
        cycles.append(reg)
        reg += int(i[5:])

def sprite(n): return [ n-1, n, n+1 ]

interesting_signals, display = [], "\n\n"

for start, stop in [[0,40], [40,80], [80,120], [120,160], [160,200], [200,240]]:
    for cycle in range(start, stop):
        if (cycle - 20) % 40 == 0: interesting_signals.append(cycle * cycles[cycle-1])
        display += "##" if cycle % 40 in sprite(cycles[cycle]) else "  "
    display += "\n"

print(f"Part one = {sum(interesting_signals)}")
print(f"Part two = {display}")
