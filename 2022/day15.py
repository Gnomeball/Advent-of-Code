# For reasons of "lets make this nonsense somewhat readable shall we?"

class Sensor:

    def __init__(self, x, y, b):
        self.x = x; self.y = y; self.dist = abs(x - b.x) + abs(y - b.y)

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __repr__(self):
        return f"Sensor at ({self.x}, {self.y}), with range [ {self.dist} ]"

class Beacon:

    def __init__(self, x, y):
        self.x = x; self.y = y

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __repr__(self):
        return f"Beacon at ({self.x}, {self.y})"

# Part one

# def manhattan(sensor, beacon):
#     return abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)

# def get_x_bounds(sensors):
#     min_x = min(s.x for s in sensors)
#     max_x = max(s.x for s in sensors)
#     return min_x, max_x

# def can_be_beacon(beacon, beacons, sensors):
#     # If this is already a beacon ..
#     if beacon in beacons: return True
#     # Else, for each sensor;
#     for sensor in sensors:
#         # we see if it's closer than something else;
#         if manhattan(sensor, beacon) <= sensor.dist:
#             return False # returning false if so
#     # If nothing closer is found, this can be a beacon
#     return True

# Part two

def ranges_overlap(a, b):
    return b[0] >= a[0] and b[0] <= a[1]

def merge_ranges(scan_ranges):
    # Attempt to merge overlapping sensor scan ranges
    # We have to sort, to prevent things like this being an issue
    # this = [ [1..5], [10..15], [3..12] ]
    scan_ranges.sort()
    merged_list = [ scan_ranges[0] ]
    for i in range(1, len(scan_ranges)):
        scan_range = merged_list.pop()
        if ranges_overlap(scan_range, scan_ranges[i]):
            # Because they overlap, we merge the items into one range
            merged_list.append((scan_range[0], max(scan_range[1], scan_ranges[i][1])))
        else:
            # Otherwise we just add it
            merged_list.append(scan_range)
            merged_list.append(scan_ranges[i])
    return merged_list

def get_scan_range(x, distance, offset):
    return x - (distance - offset), x + (distance - offset)

def get_scan_ranges(sensors, y):
    # Sensor ranges that are possibly overlapping
    scan_ranges = []
    for sensor in sensors:
        y_offset = abs(y - sensor.y)
        if y_offset <= sensor.dist:
            scan_ranges.append(get_scan_range(sensor.x, sensor.dist, y_offset))
        # if y_offset > dist the sensor can't reach this row

    # Merge the scan ranges covered by this row, and return
    return merge_ranges( [ (0, 0) ] + scan_ranges + [ (4000000, 4000000) ] )

def find_gap(sensors):
    # Loop through all possible y values (backwards)
    for y in range(4000000, -1, -1):
        # Get sensor scan ranges for this row
        scan_ranges = get_scan_ranges(sensors, y)
        # If it has gaps (more than one range), we've found what we want
        if len(scan_ranges) > 1:
            # Return the end of the first scan range, plus one;
            # this will be the "gap" in that row's scan ranges
            return (scan_ranges[0][1] +1, y)

# Parsing

def parse_that_nonsense(please):
    # There must be a better way
    sensors, beacons = [], []
    for line in please:
        d = line.replace(":", "").replace(",", "").replace("=", " ").split()
        s_x, s_y, b_x, b_y = map(int, [ d[3], d[5], d[11], d[13] ])
        b = Beacon(b_x, b_y); s = Sensor(s_x, s_y, b)
        sensors.append( s ); beacons.append( b )
    return sensors, beacons

with open("data/day15.txt") as file:
    please = file.read().splitlines()
    sensors, beacons = parse_that_nonsense(please)

# And go

# min_x, max_x = get_x_bounds(sensors)
# max_d = max(s.dist for s in sensors)

# start_x = min_x - max_d - 1
# end_x = max_x + max_d + 1

# possible_beacons = [ can_be_beacon( Beacon(pos_x, 2000000), beacons, sensors)
#                      for pos_x in range(start_x, end_x +1) ]

# print(f"Part one = {possible_beacons.count(False)}")

[(x, y)] = get_scan_ranges(sensors, 2000000)
print(f"Part one = {y - x}")

x, y = find_gap(sensors)
print(f"Part two = {y + (x * 4000000)}")
