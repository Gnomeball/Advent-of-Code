def vowel_count(s: str) -> int:
    total = 0
    for c in s:
        if c in ['a', 'e', 'i', 'o', 'u']:
            total += 1
    return total

def double_letter(s: str) -> bool:
    for c in range(1, len(s)):
        if s[c] == s[c-1]:
            return True

def part_one(strings: [str]) -> int:
    nice = 0
    for string in strings:
        bad = False
        for x in ["ab", "cd", "pq", "xy"]:
            if x in string:
                bad = True
        if bad:
            continue
        if vowel_count(string) >= 3 and double_letter(string):
            nice += 1
    return nice

def double_double(s: str) -> bool:
    for i in range(len(s) - 3):
        chunk = s[i:i+2]
        rest = s[i+2:]
        if chunk in rest:
            return True

def seperated_double(s: str) -> bool:
    for c in range(2, len(s)):
        if s[c] == s[c-2]:
            return True

def part_two(strings: [str]) -> int:
    nice = 0
    for string in strings:
        if double_double(string) and seperated_double(string):
            nice += 1
    return nice

with open("data/day05.txt", "r") as file:
    strings = file.read().splitlines()
    print(part_one(strings))
    print(part_two(strings))
