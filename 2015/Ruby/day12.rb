input = File.readlines("data/day12.json", chomp: true)

numbers = []

input.each do |line|
    line.strip!
    blocks = line.split(" ")
    blocks.each do |b|
        b.delete! ","
        if b.to_i.to_s == b
            numbers.push(b.to_i)
        end
    end
end

print numbers.reduce(0, :+), "\n"

# Who even needs json?
# (This only works because my editor formetted the JSON first)

# Part 2 - oshit..

# require 'json'

# input = File.read("day12.json", chomp: true)
# input = JSON.parse(input)
