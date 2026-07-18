instructions = File.readlines("data/day23.txt", chomp: true)

n_instructions = instructions.size
current_instruction = 0

registers = { "a" => 0, "b" => 0 }

while current_instruction >= 0 && current_instruction < n_instructions
    # print(instructions[current_instruction])
    i = instructions[current_instruction].split(" ")

    case i[0].to_s
    when "inc"
        registers.store(i[1], registers.fetch(i[1]) + 1)
    when "hlf"
        registers.store(i[1], registers.fetch(i[1]) / 2)
    when "tpl"
        registers.store(i[1], registers.fetch(i[1]) * 3)
    when "jmp"
        current_instruction += i[1].to_i
        next
    when "jie"
        reg = registers.fetch(i[1].delete(","))
        if reg.even?
            current_instruction += i[2].to_i
            next
        end
    when "jio"
        reg = registers.fetch(i[1].delete(","))
        if reg == 1
            current_instruction += i[2].to_i
            next
        end
    end

    current_instruction += 1

end

puts registers
