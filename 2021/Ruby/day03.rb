input = File.readlines("data/day03.txt", chomp: true)

gamma   = Array.new(input[0].length) {0}
epsilon = Array.new(input[0].length) {0}
result  = Array.new(input[0].length) {0}

# part 1

input.each { |e| [*0...e.length-1].each { |i| result[i] += e[i].to_i }  }

result.each_with_index { |e,i| if e > input.length/2 then gamma[i] = 1 else epsilon[i] = 1 end }

# part 2

def do_part_two(remaining, index)
    for i in 0...remaining[0].length do
        count_one  = remaining.count { |e| e[i].to_i == 1 }
        count_zero = remaining.count { |e| e[i].to_i == 0 }
        common = index[count_one <=> count_zero]
        remaining = remaining.find_all { |e| e[i].to_i == common }
        break if remaining.length == 1
    end
    return remaining[0].to_i(2)
end

oxygen = do_part_two(input.dup, [1, 1, 0])
carbon = do_part_two(input.dup, [0, 0, 1])

print("Gamma     = #{gamma.join.to_i(2)}\n")
print("Epsilon   = #{epsilon.join.to_i(2)}\n")

print("Oxygen    = #{oxygen}\n")
print("Carbon    = #{carbon}\n")

part_1 = gamma.join.to_i(2) * epsilon.join.to_i(2)
print("Part one  = #{part_1}\n")

part_2 = oxygen * carbon
print("Part two  = #{part_2}\n")
