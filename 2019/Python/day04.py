START, END = 273025, 767253

def is_still_valid(n):
    return 2 in [ n.count(str(t)) for t in range(10) ]

def number_is_valid(n):
    return n == "".join(sorted(n)) and len(n) != len(set(n))

    # if n != "".join(sorted(n)): return False
    # if len(n) == len(set(n)): return False
    # return True

valid_initially = [ n for n in range(START, END + 1) if number_is_valid(str(n)) ]
still_valid = [ n for n in valid_initially if is_still_valid(str(n)) ]

print(f"Part one = {len(valid_initially)}")
print(f"Part one = {len(still_valid)}")
