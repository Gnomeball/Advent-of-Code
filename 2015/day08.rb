def part_one(strings)

    def actual_length(string)
        full_length = string.length()+2

        slash_quote = string.scan("\"").length
        string.gsub!("\\\"", "$")

        slash_slash = string.scan("\\\\").length
        string.gsub!("\\\\", "$")

        ascii = string.scan("\\x").length
        string.gsub!(/\\x[0-9a-z][0-9a-z]/, "$")

        # puts full_length.to_s + " " + string.length.to_s + " " + slash_quote.to_s + " " + slash_slash.to_s + " " + ascii.to_s + " " + string
        return full_length - string.length
    end

    total = 0
    strings.each do |s|
        total += actual_length(s[1..-2])
    end
    puts total
end

def part_two(strings)

    def actual_length(string)
        original = string.length

        string.gsub!("\\", "\\\\\\")
        string.gsub!("\"", "\\\\\"")

        string.prepend("\"")
        string << "\""

        # puts (string.bytesize).to_s + " " + original.to_s + " " + string

        return string.bytesize - original
    end

    total = 0
    strings.each do |s|
        total += actual_length(s)
    end
    puts total
end



strings = File.readlines("data/day08.txt", chomp: true)

part_one(strings)
part_two(strings)

# * test
# * 6  - ""         -> "     "\"\""               "
# * 9  - "abc"      -> "     "\"abc\""            "
# * 16 - "aaa\"aaa" -> "     "\"aaa\\\"aaa\""     "
# * 11 - "\x27"     -> "     \"\\x27\"            "
