input = File.readlines("day15.txt", chomp: true).map { |l| l.split("").map(&:to_i) }

def flatten(part, grid)
    grid[0][0] = 0
    w = grid.length

    diagonals = []
    for e in 0..w
        line = []
        x, y = 0, e
        while x <= e do
            line.push([x+1, y+1])
            x += 1
            y -= 1
        end
        diagonals.push(line)
        diagonals.push(line.map { |v| [v[0]+w-e, v[1]+w-e] })
    end

    diagonals.pop
    diagonals.sort_by! { |v| v[0].sum }

    # pad

    for l in grid
        l.unshift(1000)
        l.push(1000)
    end

    grid.unshift(Array.new(grid[0].length) { 1000 } )
    grid.push(Array.new(grid[0].length) { 1000 } )

    # end pad

    for l in 1...diagonals.length
        line = diagonals[l]
        for pos in 0...line.length
            x, y = line[pos]
            grid[y][x] += [ grid[y-1][x], grid[y][x-1] ].min
        end
    end

    print("part #{part} = #{grid[-2][-2]}\n")
end

full_grid = Array.new(input.length * 5) { Array.new(input.length * 5) { 0 } }
for y in 0...full_grid.length
    for x in 0...full_grid.length
        full_grid[y][x] = (
            input[y % input.length][x % input.length] + (y/input.length) + (x/input.length)
            )
        if full_grid[y][x] > 9 then full_grid[y][x] -= 9 end
    end
end

flatten("one", input)

# * Doesn't work on all inputs, assumes best route is only down / right
flatten("two", full_grid)
