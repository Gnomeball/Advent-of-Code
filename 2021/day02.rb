input = File.readlines("day02.txt", chomp: true).map { |e| e.split(" ") }

# part 1

# c = {"up" => 0, "down" => 0, "forward" => 0}

# input.each { |e| c.store(e[0], c.fetch(e[0]) + e[1].to_i) }

# puts (c.fetch("down") - c.fetch("up")) * c.fetch("forward")

# part 2 - I couldn't be bothered here

depth, forward, down, up = 0, 0, 0, 0

input.each { |e|

    case e[0]
    when "down"
        down += e[1].to_i
    when "up"
        up += e[1].to_i
    when "forward"
        forward += e[1].to_i
        depth += (down-up) * e[1].to_i
    end

}

puts (down-up) * forward
puts forward * depth
