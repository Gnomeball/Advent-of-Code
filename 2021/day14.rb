input = File.readlines("day14.txt", chomp: true)

polymer = input[0]
rules_a = input[2..].map { |l| l.split(" -> ") }

rules = {}
for r in rules_a
    rules.store(r[0], r)
end

chunks = {}
for r in rules_a
    chunks.store(r[0], 0)
end
for i in 1...polymer.length
    chunks.store(polymer[i-1..i], chunks.fetch(polymer[i-1..i]) + 1)
end

$counts = {}
["B", "C", "F", "H", "K", "O", "N", "P", "S", "V"].map { |c| $counts.store(c, polymer.count(c)) }

def tick(chunks, rules)

    out_chunks = {}
    for r in rules.keys
        out_chunks.store(r, 0)
    end

    for k in chunks.keys
        v = chunks.fetch(k)

        if v == 0 then
            # * skip if not present
            next
        end

        rule = rules.fetch(k)
        a = rule[0][0] + rule[1]
        b = rule[1] + rule[0][1]

        # * +v a and b
        out_chunks.store(a, out_chunks.fetch(a) + v)
        out_chunks.store(b, out_chunks.fetch(b) + v)

        # * counts
        $counts.store(rule[1], $counts.fetch(rule[1]) + v)

    end
    return out_chunks
end

# print $counts, "\n"

10.times do
    new_chunks = tick(chunks, rules)
    chunks = new_chunks
end

c = $counts.values.flatten
print("part one = #{c.max - c.min}\n")

30.times do
    new_chunks = tick(chunks, rules)
    chunks = new_chunks
end

c = $counts.values.flatten
print("part two = #{c.max - c.min}\n")