input = File.readlines("data/day04.txt", chomp: true)
boards, part_one_found, i, numbers = [], false, 2, input[0].split(",").map { |e| e.to_i }
while i < input.length do boards.push(input[i...i+5].map { |r| r.split(" ").map { |e| e.to_i } }) and i += 6 end; numbers.each { |n| if boards.length == 1 then [*0..4].map { |r| if boards[0][r].index(n) then boards[0][r][boards[0][r].index(n)] = -1 end } and print("Part two = #{n * boards[0].flatten.map { |c| c == -1 ? 0 : c }.sum}\n") and break end; boards.map { |b| [*0..4].map { |r| if b[r].index(n) then b[r][b[r].index(n)] = -1 end } } and boards.each { |b| if [*0..4].map { |i| b[i].sum == -5 or b.transpose[i].sum == -5 }.reduce(false, :|) then if not part_one_found then part_one_found = true and print("Part one = #{n * b.flatten.map { |c| c == -1 ? 0 : c }.sum}\n") end; boards.delete(b) end } }

# This is a mess!
