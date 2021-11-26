# input = File.readlines("day13.txt", chomp: true)[0..55].map { |x| x.split(" ") }
input = File.readlines("day13.txt", chomp: true).map { |x| x.split(" ") }
# Swap these for each part

def calculate_happyness(pair, pairs)
    happyness = 0
    for i in 0..pair.length-2 do
        happyness += pairs.fetch("#{pair[i]} to #{pair[i+1]}")
        happyness += pairs.fetch("#{pair[i+1]} to #{pair[i]}")
    end
    return happyness
end

people = input.map { |i| i[0] }.uniq!

pairs = {}
input.each do |pair|
    a = pair[0]
    b = pair[10].delete (".")
    happyness = pair[3].to_i
    happyness *= -1 if pair[2] == "lose"
    pairs.store("#{a} to #{b}", happyness)
end

possible_pairs = people.permutation.to_a
possible_pairs.each { |p| p.push(p[0]) }

maximum = possible_pairs.max_by { |x| calculate_happyness(x, pairs) }

print "#{maximum} = #{calculate_happyness(maximum, pairs)}\n"
