input = File.readlines("data/day11.txt", chomp: true).map { |l| l.split("").map(&:to_i) }

for l in input
    l.unshift(-100)
    l.push(-100)
end

input.unshift(Array.new(input[0].length) { -100 } )
input.push(Array.new(input[0].length) { -100 } )

$flashes = 0

def print_grid(grid, tick)
    puts("After #{tick} steps:")
    for y in 1...grid.length-1
        for x in 1...grid[0].length-1
            print("#{grid[y][x]}")
        end
        print("\n")
    end
    print("\n")
end

def increment(grid)
    for y in 1...grid.length-1
        for x in 1...grid[0].length-1
            grid[y][x] += 1
        end
    end
end

def flash(grid, tick)

    flashes_this_tick = []
    flashes_added = 1

    while flashes_added > 0

        flashes_added = 0

        for y in 1...grid.length-1
            for x in 1...grid[0].length-1

                if grid[y][x] >= 10 then
                    if not flashes_this_tick.include?([y, x]) then
                        flashes_this_tick.push([y, x])
                        flashes_added += 1
                        (y-1..y+1).map { |y1| (x-1..x+1).map { |x1| grid[y1][x1] += 1 } }
                    end
                end

            end
        end

        $flashes += flashes_added

    end

    # * reset
    flashes_this_tick.each { |f| grid[f[0]][f[1]] = 0 }

    if tick == 100 then
        print_grid(grid, tick)
        print("part one = #{$flashes}\n")
    end

    if flashes_this_tick.length == 100 then
        print("part two = #{tick}\n")
        exit
    end

end

tick = 0

300.times do
    tick += 1
    increment(input)
    flash(input, tick)
end
