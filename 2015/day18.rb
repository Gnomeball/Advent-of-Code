input = File.readlines("day18.txt", chomp: true)#.map { |i| i.split("") }

def print_grid(input)
    print "Grid:\n\n"
    for r in 0...input.length
        for c in 0...input[0].size
            print input[r][c]
        end
        print "\n"
    end
    print "\n"
end

def count_grid(input)
    score = 0
    for r in 0...input.length
        for c in 0...input[0].size
            if input[c][r] == "#"
                score += 1
            end
        end
    end
    return score
end

def get_neighbours(c, r, min, max)
    neighbours = []
    for x in c-1..c+1
        for y in r-1..r+1
            if x < min || x > max || y < min || y > max || (x == c && y == r)
                next
            end
            neighbours.push([x, y])
        end
    end
    return neighbours
end

def count_on(input, c, r)
    count_on = 0
    neighbours = get_neighbours(c, r, 0, input.size-1)
    for n in neighbours
        if input[n[0]][n[1]] == "#"
            count_on += 1
        end
    end
    return count_on
end

def tick(input)
    output = Array.new(input.size) { Array.new(input.size) }

    for c in 0...input.length
        for r in 0...input[0].size
            if input[c][r] == "#"
                # * A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
                count = count_on(input, c, r)
                if count == 2 || count == 3
                    output[c][r] = "#"
                else
                    output[c][r] = "."
                end
            elsif input[c][r] == "."
                # * A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
                count = count_on(input, c, r)
                if count == 3
                    output[c][r] = "#"
                else
                    output[c][r] = "."
                end
            end
        end
    end

    output[0][0] = "#"
    output[99][0] = "#"
    output[0][99] = "#"
    output[99][99] = "#"

    return output
end

# LOL.. I don't have time to think that one over
# (I might do when I refactor this though)
input[0][0] = "#"
input[99][0] = "#"
input[0][99] = "#"
input[99][99] = "#"

print_grid(input)

100.times do
    input = tick(input)
    # print_grid(input)
end

print_grid(input)

print("Score : #{count_grid(input)}\n")
