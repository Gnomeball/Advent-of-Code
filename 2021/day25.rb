input = File.readlines("day25.txt", chomp: true).map { |l| l.split("") }

def print_grid(grid)
    for y in 0...grid.length
        for x in 0...grid[y].length
            print("#{grid[y][x]}")
        end
        print("\n")
    end
end


def step(grid)
    moves = 0

    out_right = Array.new(grid.length) { Array.new(grid[0].length) { "." } }

    # * >
    for y in 0...grid.length
        for x in 0...grid[y].length
            if grid[y][x] == ">" then
                if grid[y][(x+1) % grid[y].length] == "." then
                    out_right[y][(x+1) % grid[y].length] = ">" and out_right[y][x] = "."
                    moves += 1
                else
                    out_right[y][x] = ">"
                end
            elsif grid[y][x] == "v" then
                out_right[y][x] = "v"
            end
        end
    end

    out_down = Array.new(grid.length) { Array.new(grid[0].length) { "." } }

    # * v
    for y in 0...out_right.length
        for x in 0...out_right[y].length
            if out_right[y][x] == "v" then
                if out_right[(y+1) % out_right.length][x] == "." then
                    out_down[(y+1) % out_right.length][x] = "v" and out_down[y][x] = "."
                    moves += 1
                else
                    out_down[y][x] = "v"
                end
            elsif out_right[y][x] == ">" then
                out_down[y][x] = ">"
            end
        end
    end

    return out_down, moves
end


# print("Initial:\n")
# print_grid(input)

moves = 1
i = 0
loop do
    input, moves = step(input)
    i += 1
    break if moves == 0
end

print("After #{i} steps:\n")
print_grid(input)