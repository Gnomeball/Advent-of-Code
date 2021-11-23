def say_what_you_see(input)
    output = ""
    input_array = input.split("")

    # print output, input_array, "\n"

    while input_array.length > 0
        first = input_array[0]
        i = 0
        i += 1 until input_array[i] != first
        output << i.to_s << first
        input_array = input_array[i..input_array.length-1]
        # print output, input_array, "\n"
    end

    return output
end


input = File.readlines("day10.txt", chomp: true)[0]

for i in 1..50
    input = say_what_you_see(input)
    puts input.length
end

# puts input
