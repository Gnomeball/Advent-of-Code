input = File.readlines("day13.txt", chomp: true)

split = input.index("")

coordinates = input[0...split].map{ |c| c.split(",").map(&:to_i) }
folds = input[split+1..]

max_x = coordinates.max_by { |c| c[0] }[0]
max_y = coordinates.max_by { |c| c[1] }[1]

grid = Array.new(max_y+1) { Array.new(max_x+1) { "." } }

for c in coordinates
    grid[c[1]][c[0]] = "#"
end

def do_fold(grid, fold)

    axis, size = fold.split("=")
    size = size.to_i

    if axis == "y" then

        index = 0
        for y in size...grid.length
            for x in 0...grid[0].length

                if grid[y][x] == "#" then
                    grid[y - 2*index][x] = "#"
                    grid[y][x] = "."
                end

            end
            index += 1
        end

    end

    if axis == "x" then

        for y in 0...grid.length
            index = 0
            for x in size...grid[0].length

                if grid[y][x] == "#" then
                    grid[y][x - 2*index] = "#"
                    grid[y][x] = "."
                end

                index += 1
            end
        end

    end

end

def count_dots(grid)
    count = 0
    for y in 0...grid.length
        for x in 0...grid[0].length
            if grid[y][x] == "#" then
                count += 1
            end
        end
    end
    return count
end

for f in folds
    do_fold(grid, f.split(" ")[2])
    puts count_dots(grid)
end

# Part one -> first number printed

print grid

# Part two -> redirect grid to a file, read it!