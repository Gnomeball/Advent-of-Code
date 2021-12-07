input = File.read("day06.txt").split(",").map { |i| i.to_i }

fish = (0..8).map { |i| input.count(i) }

256.times do
    zero = fish.shift
    fish[8] = zero
    fish[6] += zero
end

puts fish.sum
