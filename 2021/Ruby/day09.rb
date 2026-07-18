input = File.readlines("data/day09.txt", chomp: true).map { |l| l.split("").map(&:to_i) }

for l in input
    l.unshift(9)
    l.push(9)
end

input.unshift(Array.new(input[0].length) { 9 } )
input.push(Array.new(input[0].length) { 9 } )

def neighbours(x, y)
    return [ [x, y-1], [x+1, y], [x, y+1], [x-1, y] ]
end

low_points = []

for y in 1...input.length-1
    for x in 1...input[0].length-1
        low = neighbours(x, y).map { |n| input[y][x] < input[n[1]][n[0]] }.reduce(&:&)
        if low then
            low_points.push([x, y])
        end
    end
end

puts("part one = #{low_points.map { |l| input[l[1]][l[0]] + 1 }.sum}\n")

$visited = Array.new(input.length) { Array.new(input[0].length) { false } }

def basin(grid, y, x)

    if $visited[y][x] == true then
        # print "this is fucking dumb", "\n"
        return 0
    end

    if grid[y][x] == 9 then
        # print "this is also fucking dumb", "\n"
        $visited[y][x] = true
        return 0
    end

    if x == 0 || y == 0 || x == grid.length-1 || y == grid[0].length-1 then
        # print "this is fucking dumb too", "\n"
        $visited[y][x] = true
        return 0
    end

    $visited[y][x] = true

    up = basin(grid, y-1, x)
    dn = basin(grid, y+1, x)
    lf = basin(grid, y, x-1)
    rt = basin(grid, y, x+1)
    return 1 + up + dn + lf + rt

end

basins = []

for l in low_points
    b = basin(input, l[1], l[0])
    # print input[l[1]][l[0]], ", ", b, "\n"
    basins.push(b)
end

print("part two = #{basins.sort[-3..].reduce(&:*)}\n")