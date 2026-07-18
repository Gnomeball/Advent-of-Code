# Read in the input file

import re

with open('data/day14.txt') as file:
    robots = [ list(map(int, re.findall(r'-?\d+', robot_raw))) for robot_raw in file.read().splitlines() ]

# def print_grid(seconds):

#     grid = [ ]
#     for y in range(height):
#         grid += [ [ 0 for x in range(width)]  ]

#     # For each robot
#     for x, y, dx, dy in robots:

#         # Move the robot
#         x = (x + dx * seconds) % width
#         y = (y + dy * seconds) % height

#         # Add them to a grid
#         grid[y][x] += 1

#     # Then print the grid
#     for line in grid:
#         print("".join("." if cell == 0 else str(cell) for cell in line))

width = 101
height = 103

# width = 11
# height = 7

def move_robots(seconds):
    t_r = b_r = t_l = b_l = 0

    # For each robot
    for px, py, vx, vy in robots:

        # Move the robot
        px = (px + vx * seconds) % width
        py = (py + vy * seconds) % height

        # Count up quadrant totals on this tick
        t_r += px > width//2 and py > height//2
        b_r += px > width//2 and py < height//2
        t_l += px < width//2 and py > height//2
        b_l += px < width//2 and py < height//2

    # Return product of quadrant totals
    return t_r * b_r * t_l * b_l

print(f"Part one: {move_robots(100)}")

# I am assuming that the tre is drawn almost wholly in one of the quadrants, and that
# the other two/three are very empty of robots, causing the product of totals to have
# multiple very small numbers in it, and thus the tree to appear when that sum is at
# it's minimum value .. I am also assuming it will happn within some finite time

print(f"Part two: {min(range(7500), key=move_robots)}")

# print_grid(6355) # the tree (for me)
