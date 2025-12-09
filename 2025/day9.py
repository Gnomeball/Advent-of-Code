from itertools import combinations, pairwise

# To make it nicer to read

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"({self.x},{self.y})"

with open("data/day9.txt") as file:
    red = [ Point(*map(int, line.split(","))) for line in file.read().splitlines() ]

# Function to order points

def order_points(points):
    return [ ( Point(min(left.x, right.x), min(left.y, right.y)),
               Point(max(left.x, right.x), max(left.y, right.y)) ) for left, right in points ]

green = order_points(pairwise(red))

largest_red = 0
largest_internal_red = 0

for red_left, red_right in order_points(combinations(red, 2)):
    size = (red_right.x - red_left.x +1) * (red_right.y - red_left.y +1)

    if size > largest_internal_red:
        for green_left, green_right in green:
            if ( green_left.x < red_right.x and green_left.y < red_right.y
             and green_right.x > red_left.x and green_right.y > red_left.y ):
                break
        else:
            largest_internal_red = size

    if size > largest_red:
        largest_red = size

print("Part one =", largest_red)
print("Part two =", largest_internal_red)