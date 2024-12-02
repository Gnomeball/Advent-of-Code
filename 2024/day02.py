# Read in the data, line by line, collecting the reports as lists

with open("data/day02.txt") as file:
    reports = [[int(x) for x in report.split()] for report in file.read().splitlines()]

# Function to check if a report is safe

def report_is_safe(report) -> bool:

    # The levels are either all increasing *or* all decreasing.

    def numbers_all_increase(report) -> bool:
        return report == sorted(report)

    def numbers_all_decrease(report) -> bool:
        return report == sorted(report, reverse=True)

    # Any two adjacent levels differ by at least one and at most three.

    def numbers_differ_correctly(report) -> bool:
        diffs = [abs(x-y) for x,y in zip(report, report[1:])]
        for d in diffs:
            if d not in range(1, 4):
                return False
        return True

    # Check if safe

    if numbers_all_increase(report) or numbers_all_decrease(report):
        return numbers_differ_correctly(report)

    return False

# Function that removes items from a list, to check if a safe match can be found

def remove_then_check(report) -> bool:

    report_length = len(report)

    # Create a list of reports, each one a copy of the original report, but with one item removed
    report_copies = [report.copy() for _ in range(report_length)]

    for i in range(report_length):
        report_copies[i].pop(i)

    return [report_is_safe(report) for report in report_copies].count(True) >= 1

# Part one: Count up reports that are safe

count = sum([report_is_safe(report) for report in reports])

print(f"Part one: {count}")

# Part two: When removing only one item, count up reports that become safe

count = sum([remove_then_check(report) for report in reports])

print(f"Part two: {count}")
