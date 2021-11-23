input = File.read("day11.txt", chomp: true)

def part_one(input)

    def has_increasing_straight(input)
        for i in 0...input.length-3 do
            chunk = input[i..i+2]
            if chunk[0].ord+1 == chunk[1].ord and chunk[1].ord == chunk[2].ord-1
                return true
            end
        end
        return false
    end

    def has_double_double(input)
        doubles = {}
        for i in 0...input.length do
            chunk = input[i..i+1]
            if chunk[0] == chunk[1]
                doubles.store(chunk, true)
            end
        end
        return doubles.size >= 2
    end

    def has_bad_letters(input)
        (["i", "l", "o"].map {|i| input.include? i }).reduce(false, :|)
    end

    def locate_bad_letter(input)
        (["i", "l", "o"].map {|i| if input.include? i then input.index i else input.size end }).min
    end

    found = false
    i = 0

    input.next!

    for _ in 0.. do

        if has_bad_letters(input)
            index = locate_bad_letter(input)
            input[index] = input[index].next!
            input[index+1..] = "a" * (7 - index)
        else
            input.next!
        end

        found = has_increasing_straight(input) && has_double_double(input) && !has_bad_letters(input)

        if found
            print input, " ", has_increasing_straight(input), " ", has_double_double(input), " ", !has_bad_letters(input), "\n"
            break
        end

    end

end

part_one(input)
