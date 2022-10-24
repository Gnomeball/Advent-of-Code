input = File.readlines("data/day20.txt", chomp: true)

mapping = input[0]

grid = input[2..].map { |l| l.split("") }

def count_pixels(grid, pad)
    count = 0
    for y in pad...grid.length-pad
        for x in pad...grid[0].length-pad
            count += grid[y][x] == "#" ? 1 : 0
        end
    end
    return count
end

def pad_grid(grid, length, char)
    length.times do
        grid.push( Array.new(grid[0].length) { char } )
        grid.unshift( Array.new(grid[0].length) { char } )
        grid.map { |l| l.unshift(char).push(char) }
    end
    return grid
end

def step(grid, mapping)
    pad_grid(grid, 1, ".")
    out = Array.new(grid.length) { Array.new(grid[0].length) { "." } }
    for y in 1...out.length-1
        for x in 1...out[0].length-1
            position = [ grid[y-1][x-1..x+1], grid[y][x-1..x+1], grid[y+1][x-1..x+1] ].flatten
            binary = position.map { |c| c == "#" ? 1 : 0 }.join("").to_i(2)
            out[y][x] = mapping[binary]
        end
    end
    return out
end

pad = grid.length
pad_grid(grid, pad, ".")

2.times do
    grid = step(grid, mapping)
end
print("part one = #{count_pixels(grid, pad)}\n")
# 5489

48.times do
    grid = step(grid, mapping)
end
print("part two = #{count_pixels(grid, pad)}\n")
# 19066
