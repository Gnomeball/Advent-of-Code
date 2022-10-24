with open("data/day11.txt", "r") as file:
    seats = [[seat for seat in row] for row in file.read().splitlines()]

HEIGHT = len(seats)
WIDTH = len(seats[0])

EMPTY_SEAT = "L"
FLOOR = "."
OCCUPIED_SEAT = "#"

def getNeighbours(thing, x, y):
    neighbours = []
    for i, j in [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,-1), (-1,1)]:
        this_x, this_y = x + i, y + j
        if not (this_x < 0 or this_x >= WIDTH or this_y < 0 or this_y >= HEIGHT):
            neighbours.append(thing[this_y][this_x])
    return neighbours

def updateSeat(thing, x, y):
    seat = thing[y][x]
    neighbours = getNeighbours(thing, x, y)
    if seat == EMPTY_SEAT:
        return OCCUPIED_SEAT if OCCUPIED_SEAT not in neighbours else EMPTY_SEAT
    elif seat == OCCUPIED_SEAT:
        return EMPTY_SEAT if neighbours.count(OCCUPIED_SEAT) >= 4 else OCCUPIED_SEAT
    else:
        return seat

def updateSeats(thing):
    next = [[seat for seat in row] for row in thing]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            next[y][x] = updateSeat(thing, x, y)
    return next

def countOccupiedSeats(thing):
    return sum(row.count('#') for row in thing)

def partOne():
    next = [[seat for seat in row] for row in seats]
    while True:
        last = [[seat for seat in row] for row in next]
        next = updateSeats(last)
        if last == next:
            break
    print(countOccupiedSeats(next))

# Part 1

partOne()
