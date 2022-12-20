with open("data/day01.txt") as file:
    masses = [ int(n) for n in file.readlines() ]

def counter_upper(mass):
    return int(mass / 3) - 2

print(f"Part one = {sum(map(counter_upper, masses))}")

def double_checker(mass):
    extra_mass = fuel_required = counter_upper(mass)
    while counter_upper(extra_mass) > 0:
        # Oh noes I'm doing it twice!
        extra_mass = counter_upper(extra_mass)
        fuel_required += extra_mass
    return fuel_required

print(f"Part two = {sum(map(double_checker, masses))}")