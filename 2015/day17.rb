input = File.readlines("data/day17.txt", chomp: true).map { |x| x.to_i }

combinations = []
[*1..10].each { |i| input.combination(i).each { |c| combinations.push(c) } }

one_fiddy = combinations.find_all { |c| c.sum == 150 }
more_eggnog = one_fiddy.find_all { |c| c.size == one_fiddy.first.size }

puts one_fiddy.size
puts more_eggnog.size
