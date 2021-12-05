input = File.readlines("day05.txt", chomp: true).map { |i|
    i.split(" -> ").map { |e| e.split(",").map { |i| i.to_i } }.flatten }

grid = Array.new(1000) { Array.new(1000) { 0 } }

def add_wire(grid, x1, x2, y1, y2)
    for x in [x1, x2].min..[x1, x2].max
        for y in [y1, y2].min..[y1, y2].max
            grid[x][y] += 1
        end
    end
    return grid
end

def add_diagonal(grid, x1, x2, y1, y2)
    # print("#{x1} #{x2} #{y1} #{y2}\n")

    if x1 < x2 and y1 < y2 then
        # * / up
        while x1 <= x2 do
            grid[x1][y1] += 1
            x1 += 1
            y1 += 1
        end
    elsif x1 < x2 and y1 > y2 then
        # * \ down
        while x1 <= x2 do
            grid[x1][y1] += 1
            x1 += 1
            y1 -= 1
        end
    elsif x1 > x2 and y1 > y2 then
        # * / down
        while x1 >= x2 do
            grid[x1][y1] += 1
            x1 -= 1
            y1 -= 1
        end
    elsif x1 > x2 and y1 < y2 then
        # * \ up
        while x1 >= x2 do
            grid[x1][y1] += 1
            x1 -= 1
            y1 += 1
        end
    end

    return grid
end

for i in input
    # [ [ 1, 2, 3, 4 ] ]
    x1, y1, x2, y2 = i

    if x1 == x2 or y1 == y2 then
        grid = add_wire(grid, x1, x2, y1, y2)
    end

    if (x1 - x2).abs == (y1 - y2).abs then
        prid = add_diagonal(grid, x1, x2, y1, y2)
    end

end

for x in [*0..99].reverse
    for y in [*0..99].reverse
        print grid[x][y]
    end
    print "\n"
end

result = grid.flatten.count { |i| i >= 2 }
print("result = #{result}\n")
