input = File.readlines("day16.txt", chomp: true)

data = {
    "cats"        => 7,
    "trees"       => 3,
    "pomeranians" => 3,
    "goldfish"    => 5,
    "children"    => 3,
    "samoyeds"    => 2,
    "akitas"      => 0,
    "vizslas"     => 0,
    "cars"        => 2,
    "perfumes"    => 1
}

@nuclear_decay = {"cats" => true, "trees" => true}
@modial_interaction = {"pomeranians" => true, "goldfish" => true}

sues = {}

input.each do |i|
    details = i.delete(":,").split(" ")
    sues.store(details[1].to_i, {
        details[2] => details[3].to_i,
        details[4] => details[5].to_i,
        details[6] => details[7].to_i
    })
end

def score_sue(sue, data)
    return sue.keys.map { |k|
        if @nuclear_decay.key? k
            sue.fetch(k) > data.fetch(k)
        elsif @modial_interaction.key? k
            sue.fetch(k) < data.fetch(k)
        elsif sue.fetch(k) == data.fetch(k)
            true
        end
    }.count(true)
end

the_sue = [*1..500].max_by { |sue| score_sue(sues.fetch(sue), data) }

print "The Sue = #{the_sue}\n"
