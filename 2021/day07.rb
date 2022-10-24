input = File.read("data/day07.txt").split(",").map { |i| i.to_i }

min = input.min
max = input.max

factorial = [0] and (1..max).each { |f| factorial.push(factorial[-1] + f) }

part_one = []
part_two = []

for f in min..max
    p_1 = input.map { |i| (f-i).abs }.sum
    p_2 = input.map { |i| factorial[(f-i).abs] }.sum
    part_one.push(p_1)
    part_two.push(p_2)
    # print("#{f} = #{p_1}, #{p_2}\n")
end

print("part one = #{part_one.min}\n")
print("part two = #{part_two.min}\n")


# And a slower way


values = (0..max).map { |v| input.count(v) }

part_one = []
part_two = []

for f in min..max
    p_1 = 0
    p_2 = 0
    values.each_with_index do |c,l|
        # l = location, c = num of crab
        next if c == 0
        p_1 += (f-l).abs * c
        p_2 += factorial[(f-l).abs] * c
    end
    part_one.push(p_1)
    part_two.push(p_2)
end

print("part one = #{part_one.min}\n")
print("part two = #{part_two.min}\n")

