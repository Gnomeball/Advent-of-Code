input = File.readlines("data/day01.txt", chomp: true).map { |e| e.to_i }

# Part 1

# larger = 0

# for i in 1..input.size
#     e = input[i].to_i
#     l = input[i-1].to_i
#     larger += 1 if e > l
# end

# puts larger

puts input.map.with_index { |e,i| e > input[i-1] }.count(true)

# Part 2

puts input.map.with_index { |e,i| e > input[i-3] }.count(true)

# larger = 0

# for i in 3..input.size
#     e = input[i].to_i
#     c = input[i-3].to_i
#     larger += 1 if e > c
# end

# puts larger