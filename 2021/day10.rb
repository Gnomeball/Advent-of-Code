input = File.readlines("day10.txt", chomp: true).map { |l| l.split("") }

$corrupt_scores = { ")" => 3, "]" => 57, "}" => 1197, ">" => 25137 }
$incomplete_score = { ")" => 1, "]" => 2, "}" => 3, ">" => 4 }
$chars = { "(" => ")", "[" => "]", "{" => "}", "<" => ">" }

def score_corrupted(line)
    stack = []
    for c in line
        if "([{<".include?(c) then
            stack.push(c)
        else # * it's a closing
            if $chars.fetch(stack.last) == c then
                stack.pop
            else
                return $corrupt_scores.fetch(c)
            end
        end
    end
    return 0
end

part_one = 0
incomplete_lines = []

for i in input
    score = score_corrupted(i)
    part_one += score
    if score == 0 then incomplete_lines.push(i) end
end

puts("part one = #{part_one}")

def score_incomplete(line)
    stack = []
    for c in line
        if "([{<".include?(c) then
            stack.push(c)
        else # * it's a closing
            stack.pop
        end
    end
    score = 0
    for char in stack.reverse
        c = $chars.fetch(char)
        score *= 5
        score += $incomplete_score.fetch(c)
    end
    return score
end

part_two = []

for i in incomplete_lines
    score = score_incomplete(i)
    part_two.push(score)
end

part_two.sort!
result = part_two[(part_two.length-1)/2]

puts("part two = #{result}")
