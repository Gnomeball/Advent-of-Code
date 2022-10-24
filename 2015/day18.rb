input = File.readlines("data/day18.txt", chomp: true)

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
    score = input.flatten.map { |c| c == "#" ? 1 : 0 }.sum
    return score
end

def get_neighbours(c, r, min, max)
    all_neighbours = [*c-1..c+1].product([*r-1..r+1]).select { |x, y| [x, y] }
    valid_neighbours = all_neighbours.delete_if {
        |x, y| x < min || x > max || y < min || y > max || (x == c && y == r) }
    return valid_neighbours
end

def count_on(input, c, r)
    neighbours = get_neighbours(c, r, 0, input.size-1)
    count = neighbours.map { |n| input[n[0]][n[1]] == "#" ? 1 : 0 }.sum
    return count
end

def tick(input)
    output = Array.new(input.size) { Array.new(input.size) }

    for c in 0...input.length
        for r in 0...input[0].size
            if input[c][r] == "#"
                # * A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
                count = count_on(input, c, r)
                output[c][r] = count == 3 || count == 2 ? "#" : "."
            elsif input[c][r] == "."
                # * A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
                count = count_on(input, c, r)
                output[c][r] = count == 3 ? "#" : "."
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
end

print_grid(input)

print("Score : #{count_grid(input)}\n")
