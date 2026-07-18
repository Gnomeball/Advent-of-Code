from functools import cmp_to_key

with open("data/day13.txt") as file:
    packets = [ eval(l) for l in file.readlines() if l.strip() ]
    pairs = zip(packets[::2], packets[1::2])

def comparator(left, right):
    return 1 if right > left else -1 if right < left else 0

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return comparator(left, right)
    else:
        if isinstance(right, int): right = [right]
        if isinstance(left, int): left = [left]

        for value in (compare(le, re) for le, re in zip(left, right)):
            if value != 0: return value

        return comparator(len(left), len(right))

print("Part one =", sum(index + 1 for index, (left, right) in enumerate(pairs) if compare(left, right) >= 0))

markers = [[[6]], [[2]]]
packets = list(reversed(sorted(packets + markers, key = cmp_to_key(compare))))
left, right = [ packets.index(m) + 1 for m in markers ]

print("Part two =", left * right)