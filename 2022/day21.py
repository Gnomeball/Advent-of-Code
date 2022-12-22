with open('data/day21.txt') as file:
    minkeys = file.readlines()

KNOWN, GIBBERISH = dict(), dict()

# We begin by spliting input between
#  - Minkeys yelling KNOWN data
#  - and those yelling gibberish
for minkey in minkeys:
    minkey = minkey.strip().split()
    if len(minkey) == 2:
          KNOWN[minkey[0][:-1]] = minkey[1]
    else: GIBBERISH[minkey[0][:-1]] = (minkey[1], minkey[3], minkey[2])

# These are for part two
LEFT, RIGHT = None, None

def do_the_thing(KNOWN, GIBBERISH):
    global LEFT, RIGHT
    while 'root' not in KNOWN:
        for index, element in GIBBERISH.items():
            if element[0] in KNOWN and element[1] in KNOWN:
                # The aforementioned part two
                if index == 'root':
                    LEFT = complex(KNOWN[element[0]])
                    RIGHT = complex(KNOWN[element[1]])
                KNOWN[index] = eval( str(KNOWN[element[0]]) + str(element[2]) + str(KNOWN[element[1]]) )
    return KNOWN['root']

# Part one
print(f"Part one = {int( do_the_thing(KNOWN.copy(), GIBBERISH.copy()) )}")

# Part two
KNOWN['humn'] = 1j
do_the_thing(KNOWN, GIBBERISH)

print(f"Part two = {int( (RIGHT.real - LEFT.real) / (LEFT.imag - RIGHT.imag) )}")
