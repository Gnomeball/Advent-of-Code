# For reasons of "lets make this nonsense somewhat readable shall we?"

class Room:
    def __init__(self, rate, exits):
        self.rate = rate; self.exits = exits

# Part one

def find_best_total_flow(current_room, time, seen, target_rooms):
    # Given the current room, time_r, and what we've seen so far,
    # work out the best flow from that room
    seen = seen | {current_room}
    target_rooms = target_rooms - seen
    best_flow = 0

    for target in target_rooms:
        # Time left is time_r, less the distance to this room, less 1 for the valve
        remaining_time = time - distances[ (current_room, target) ] - 1
        if remaining_time > 0:
            # Because this valve remains open, it's start value must be flow * time_r
            flow = rooms[target].rate * remaining_time
            # Then simply add the best flow from ths point, recursively
            flow += find_best_total_flow(target, remaining_time, seen, target_rooms)
            if flow > best_flow: best_flow = flow

    return best_flow

def find_distances(rooms):
    # Using BFS, build a map of all important distances
    # ( This is every room to every other room where we
    #   don't care about paths that lead to no flow rate )
    target_rooms = {r for r in rooms if rooms[r].rate > 0 or r == "AA"}
    distances = {}

    for start_room in rooms:
        # if start_room not in target_rooms: continue
        current_room, next_room, dist = set([ start_room ]), set(), 0
        # distances[ (start_room, start_room) ] = 0
        while current_room:
            dist += 1
            for pos in current_room:
                for newpos in rooms[pos].exits:
                    if (start_room, newpos) not in distances:
                        distances[ (start_room, newpos) ] = dist
                        next_room.add(newpos)
            current_room, next_room = next_room, set()

    return distances, target_rooms

# Part two

def find_and_record(current_room, current_flow, time, seen, target_rooms):
    # Much like part one, but this time we start with less time,
    # and record every path to endpoint we see, to be filled in later
    seen = seen | {current_room}
    target_rooms = target_rooms - seen

    torecord = frozenset(seen - {"AA"})
    if torecord in ENDPOINTS:
          ENDPOINTS[torecord] = max(ENDPOINTS[torecord], current_flow)
    else: ENDPOINTS[torecord] = current_flow

    best_flow = 0
    for target in target_rooms:
        remaining_time = time - distances[(current_room, target)] - 1
        if remaining_time > 0:
            newflow = rooms[target].rate * remaining_time
            newflow += find_and_record(target, current_flow + newflow, remaining_time, seen, target_rooms)
            if newflow > best_flow: best_flow = newflow
    return best_flow

def fill_in_endpoints(current_room):
    if current_room not in ENDPOINTS:
        best_flow = 0
        for endpoint in current_room:
            subset = current_room - { endpoint }
            new_flow = fill_in_endpoints(subset)
            if new_flow > best_flow: best_flow = new_flow
        ENDPOINTS[current_room] = best_flow
    return ENDPOINTS[current_room]

# Parsing

def parse_that_nonsense(please):
    rooms = {}
    for line in please:
        line = line.replace("=", " ").replace(",", "").replace(";", "").split()
        source, rate, exits = line[1], int(line[5]), line[10:]
        rooms[source] = Room(rate, exits)
    return rooms

with open("data/day16.txt") as file:
    please = file.read().splitlines()
    rooms = parse_that_nonsense(please)

# And go

distances, target_rooms = find_distances(rooms)

best_flow = find_best_total_flow("AA", 30, set(), target_rooms)

print("Part one =", best_flow)

global ENDPOINTS
ENDPOINTS = {} # Empty, filled in below
best_flow = find_and_record("AA", 0, 26, set(), target_rooms)
not_used = fill_in_endpoints(frozenset(target_rooms - {"AA"}))

best_flow = 0
for human in ENDPOINTS:
    elephant = frozenset(target_rooms - {"AA"} - human)
    total_flow = ENDPOINTS[human] + ENDPOINTS[elephant]
    if total_flow > best_flow:
        best_flow = total_flow

print("Part two =", best_flow)
