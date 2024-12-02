with open("data/day01.txt") as file:
    codes = file.read().splitlines()

def find_number(code):
    for char in code:
        if ord(char) - 48 in [0,1,2,3,4,5,6,7,8,9]:
            return char

def calibration_number(code):
    return int(find_number(code) + find_number(code[::-1]))

def numberwang(code):
    return code.replace("one", "o1ne").replace("two", "t2wo").replace("three", "t3hree").replace("four", "f4our").replace("five", "f5ive").replace("six", "s6ix").replace("seven", "s7even").replace("eight", "e8ight").replace("nine", "n9ine")

totals = [0, 0]

for code in codes:
    totals[0] += calibration_number(code)
    totals[1] += calibration_number(numberwang(code))

print(f"Part one: {totals[0]}")
print(f"Part two: {totals[1]}")