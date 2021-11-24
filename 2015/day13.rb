input = File.readlines("day13.txt", chomp: true)[0..55]

# input = File.readlines("day13.txt", chomp: true)
# Swap these for part 2

def calculate_happyness(pair, pairs)
    happyness = 0
    for i in 0..pair.length-2 do
        step_a = "#{pair[i]} to #{pair[i+1]}"
        step_b = "#{pair[i+1]} to #{pair[i]}"
        happyness += pairs.fetch(step_a)
        happyness += pairs.fetch(step_b)
    end
    return happyness
end

people = []
pairs = {}

input.each do |i|
    pair = i.split(" ")

    a = pair[0]
    b = pair[10].delete (".")
    type = pair[2]

    happyness = pair[3].to_i
    if type == "lose"
        happyness -= 2 * happyness
    end

    people.push(a)

    pairs.store("#{a} to #{b}", happyness)
end

people.uniq!

possible_pairs = people.permutation.to_a
possible_pairs.each { |p| p.push(p[0]) }

shortest = possible_pairs.min_by { |x| calculate_happyness(x, pairs) }
longest = possible_pairs.max_by { |x| calculate_happyness(x, pairs) }

print "#{shortest} = #{calculate_happyness(shortest, pairs)}\n"
print "#{longest} = #{calculate_happyness(longest, pairs)}\n"
