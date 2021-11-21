def part_one(instructions)
    grid = Array.new(1000) {Array.new(1000) {false}}

    instructions.each do | instruction |
        words = instruction.split()

        first, second = words[-3], words[-1]
        x_from, y_from = first.split(",").map(&:to_i)
        x_to, y_to = second.split(",").map(&:to_i)

        for x in x_from..x_to do
            for y in y_from..y_to do
                if words[0] == "toggle"
                    grid[y][x] = !grid[y][x]
                else
                    if words[1] == "on"
                        grid[y][x] = true
                    elsif words[1] == "off"
                        grid[y][x] = false
                    end
                end
            end
        end
    end

    total = 0
    for x in 0..999 do
        for y in 0..999 do
            if grid[y][x]
                total += 1
            end
        end
    end

    return total
end

def part_two(instructions)
    grid = Array.new(1000) {Array.new(1000) {0}}

    instructions.each do | instruction |
        words = instruction.split()

        first, second = words[-3], words[-1]
        x_from, y_from = first.split(",").map(&:to_i)
        x_to, y_to = second.split(",").map(&:to_i)

        lights_affected = (x_to - x_from) * (y_to - y_from)

        for x in x_from..x_to do
            for y in y_from..y_to do
                if words[0] == "toggle"
                    grid[y][x] += 2
                else
                    if words[1] == "on"
                        grid[y][x] += 1
                    elsif words[1] == "off"
                        if grid[y][x] > 0
                            grid[y][x] -= 1
                        end
                    end
                end
            end
        end
    end

    total = 0
    for x in 0..999 do
        for y in 0..999 do
            total += grid[y][x]
        end
    end

    return total
end

instructions = File.readlines("day06.txt")

puts part_one(instructions)
puts part_two(instructions)
