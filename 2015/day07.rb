instructions = File.readlines("data/day07.txt")

gates = {}

while instructions.length > 0
    used = false
    index = 0

    for i in 0..instructions.length-1 do
        input, output = instructions[i].strip().split(" -> ")

        input_l = ""
        type = ""
        input_r = ""

        # * Get the inputs
        inputs = input.split(" ")
        if instructions[i].include?("NOT")
            input_l = inputs[1]
            type = "NOT"
            input_r = ""
        elsif instructions[i].include?("AND")
            input_l = inputs[0]
            type = "AND"
            input_r = inputs[2]
        elsif instructions[i].include?("OR")
            input_l = inputs[0]
            type = "OR"
            input_r = inputs[2]
        elsif instructions[i].include?("LSHIFT")
            input_l = inputs[0]
            type = "LSHIFT"
            input_r = inputs[2].to_i
        elsif instructions[i].include?("RSHIFT")
            input_l = inputs[0]
            type = "RSHIFT"
            input_r = inputs[2].to_i
        else
            if inputs[0].to_i.to_s == inputs[0]
                input_l = inputs[0]
                type = "DECLARATION"
                input_r = ""
            else
                input_l = inputs[0]
                type = "WIRE"
                input_r = ""
            end
        end

        # * Do the thing
        case type
        when "DECLARATION"
            gates.store(output, input_l.to_i)
            used = true
            index = i
        when "WIRE"
            if gates.has_key?(input_l)
                gates.store(output, gates.fetch(input_l))
                used = true
                index = i
            end
        when "NOT"
            if gates.has_key?(input_l)
                gates.store(output, ~gates.fetch(input_l))
                used = true
                index = i
            end
        when "OR"
            if gates.has_key?(input_l) && gates.has_key?(input_r)
                gates.store(output, gates.fetch(input_l) | gates.fetch(input_r))
                used = true
                index = i
            end
        when "AND"
            # * AND can have a number on the left
            if gates.has_key?(input_r)
                if input_l.to_i.to_s == input_l # ! It's an int
                    gates.store(output, input_l.to_i & gates.fetch(input_r))
                    used = true
                    index = i
                elsif gates.has_key?(input_l)
                    gates.store(output, gates.fetch(input_l) & gates.fetch(input_r))
                    used = true
                    index = i
                end
            end
        when "LSHIFT"
            if gates.has_key?(input_l)
                gates.store(output, gates.fetch(input_l) << input_r.to_i)
                used = true
                index = i
            end
        when "RSHIFT"
            if gates.has_key?(input_l)
                gates.store(output, gates.fetch(input_l) >> input_r.to_i)
                used = true
                index = i
            end
        end

        # * Check if we did a thing
        if used
            puts "Used " + instructions[index].strip() + " as " + type
            instructions.delete_at(index)
            break
        elsif index == instructions.length-1
            puts "End of list"
        else
            puts "Didn't use " + instructions[i]
        end
    end
end

# * And.. magic!
puts gates.fetch("a")

# This question took me over 6 hours..
# but my solution to part 1 juat worked for part 2.. so yay
