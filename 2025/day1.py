with open("data/day1.txt") as file:
    directions = [ ( line[0], int(line[1:]) ) for line in file.read().splitlines() ]

dir_map = { "L": -1, "R": +1 }

current_position = 50

def get_next_position(current, direction, distance):
    return current + dir_map[direction] * distance
    # match direction:
    #     case "L": return current + ( -1 * distance )
    #     case "R": return current + ( +1 * distance )

def check_pass(previous, current, direction):
    return(sum((1 if position % 100 == 0 else 0) for position in range(previous, current, dir_map[direction])))
    # passes = 0
    # for position in range(previous, current, dir_map[direction]):
    #     # print(position, position % 100 == 0)
    #     if (position % 100 == 0) :
    #         passes += 1
    # return passes

# Logic

pass_through_zero = 0
land_on_zero = 0

for direction in directions:
    # track previous
    previous_position = current_position
    # do the move
    current_position = get_next_position(current_position, *direction)
    # print(f"Moving {direction} from {previous_position} to {current_position}")
    # check if move pushed us through zero
    pass_through_zero += check_pass(previous_position, current_position, direction[0])
    # check if we landed on zero
    if current_position % 100 == 0:
        land_on_zero += 1

print("Part one = ", land_on_zero)
print("Part two = ", pass_through_zero)
