def parse_snail(string)
    depth = 0
    out = []
    string.chars.each do |char|
        case char
        when "["; depth += 1
        when "]"; depth -= 1
        else
            out << [char.to_i, depth] if char.match?(/\d/)
        end
    end
    return out
end

def explode_snail(snail)
    l_num, r_num = nil, nil
    for i in 0...snail.length
        magnitude = snail[i][1]
        if magnitude >= 5 then
            l_num, r_num = i, i+1
            if l_num != nil then
                snail[l_num-1][0] += snail[l_num][0] if l_num != 0
                snail[l_num] = [0, snail[l_num][1]-1]
            end
            if r_num != nil then
                snail[r_num+1][0] += snail[r_num][0] if r_num != snail.length-1
                snail[r_num] = 0
            end
            break
        end
    end
    return snail.delete_if { |x| x == 0 }
end

def split_snail(snail)
    out = snail.dup
    for i in 0...snail.length
        n = snail[i]
        if n[0] > 9 then
            out.insert(i, [n[0]/2, n[1]+1])
            out.insert(i+1, [(n[0]+1)/2, n[1]+1])
            out.delete_at(i+2)
            break
        end
    end
    return out
end

def add_snails(a, b)
    snail = []
    a.each { |o| snail.push(o.dup) }
    b.each { |o| snail.push(o.dup) }
    snail.each { |n| n[1] += 1 }
    loop do
        explode = (0...snail.length).map { |m| snail[m][1] >= 5 }.reduce(&:|)
        if explode then snail = explode_snail(snail); next end
        split = (0...snail.length).map { |m| snail[m][0] > 9 }.reduce(&:|)
        break if !(explode || split)
        if split then snail = split_snail(snail); next end
    end
    return snail
end

def calculate_magnitude(snail)
    loop do
        max_depth = snail.map { |x| x[1] }.max
        break if max_depth == 0
        index = snail.index { |x| x[1] == max_depth }
        # print("#{index} in #{snail}\n")
        snail[index] = [3 * snail[index][0] + 2 * snail[index+1][0], snail[index][1]-1]
        snail.delete_at(index + 1)
    end
    return snail.first.first
end

input = File.readlines("day18.txt", chomp: true).map { |l| parse_snail(l) }

snail = input[0]

for i in 1...input.length
    snail = add_snails(snail, input[i])
end

print("part one = #{calculate_magnitude(snail)}\n")

p_2 = input.permutation(2).map { |a, b| calculate_magnitude(add_snails(a.dup, b.dup)) }.max

print("part two = #{p_2}\n")
