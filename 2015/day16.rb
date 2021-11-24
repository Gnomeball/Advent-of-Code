input = File.readlines("day16.txt", chomp: true)

data = {
    "cats" => 7,
    "trees" => 3,
    "pomeranians" => 3,
    "goldfish" => 5,
    "children" => 3,
    "samoyeds" => 2,
    "akitas" => 0,
    "vizslas" => 0,
    "cars" => 2,
    "perfumes" => 1
}

sues = {}

input.each do |i|
    details = i.split(" ")
    name = (details[1].delete! ":").to_i
    var_1 = (details[2].delete! ":")
    val_1 = (details[3].delete! ",").to_i
    var_2 = (details[4].delete! ":")
    val_2 = (details[5].delete! ",").to_i
    var_3 = (details[6].delete! ":")
    val_3 = (details[7]).to_i
    sue = {
        var_1 => val_1,
        var_2 => val_2,
        var_3 => val_3
    }
    sues.store(name, sue)
end

def score_sue(sue, data)
    score = 0

    if sue.key? "cats"
        if sue.fetch("cats") > data.fetch("cats")
            score += 1
        end
        sue.delete("cats")
    end

    if sue.key? "trees"
        if sue.fetch("trees") > data.fetch("trees")
            score += 1
        end
        sue.delete("trees")
    end

    if sue.key? "pomeranians"
        if sue.fetch("pomeranians") < data.fetch("pomeranians")
            score += 1
        end
        sue.delete("pomeranians")
    end

    if sue.key? "goldfish"
        if sue.fetch("goldfish") < data.fetch("goldfish")
            score += 1
        end
        sue.delete("goldfish")
    end

    data.keys.each do |k|
        if sue.key? k
            if sue.fetch(k) == data.fetch(k)
                score += 1
            end
        end
    end

    return score
end

the_sue = [*1..500].max_by { |sue| score_sue(sues.fetch(sue), data) }

print "The Sue = #{the_sue}\n"
