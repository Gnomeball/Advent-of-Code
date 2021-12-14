input = File.readlines("day08.txt", chomp: true).map { |l| l.split("|") }

class Display

    attr_accessor :input
    attr_accessor :output
    attr_accessor :mapping
    attr_accessor :value

    def initialize(i, o)
        @input = i.split(" ").map { |s| s.chars.sort.join }.sort_by { |x| x.length }
        @output = o.split(" ").map { |s| s.chars.sort.join }
        @value = 0
        @mapping = {
            "top"          => "",
            "middle"       => "",
            "bottom"       => "",
            "top_left"     => "",
            "top_right"    => "",
            "bottom_left"  => "",
            "bottom_right" => ""
        }
    end

    def map
        one = @input[0]
        four = @input[2]
        seven = @input[1]
        eight = input[9]

        # * bottom and b_l are all in 8 not in 4 or 7
        four.chars.each do |c|
            eight = eight.delete(c)
        end
        seven.chars.each do |c|
            eight = eight.delete(c)
        end
        @mapping.store("bottom", eight)
        @mapping.store("bottom_left", eight)

        # * the extra one in seven not in one is top
        one.chars.each do |c|
            seven = seven.delete(c)
        end
        @mapping.store("top", seven)

        # * middle and top left are what's in 4 not in 1
        one.chars.each do |c|
            four = four.delete(c)
        end
        @mapping.store("middle", four)
        @mapping.store("top_left", four)

        # * whatever is in all of 2, 3, 5 is top, middle, bottom
        two = input[3]
        three = input[4]
        five = input[5]
        shared = ""
        "abcedfg".chars.each do |c|
            if two.include?(c) && three.include?(c) && five.include?(c) then
                shared += c
            end
        end
        shared = shared.delete(@mapping.fetch("top"))
        # * now whatever is in bottom and middle can be known
        shared.chars.each do |c|
            if @mapping.fetch("middle").include?(c) then
                @mapping.store("middle", c)
            end
            if @mapping.fetch("bottom").include?(c) then
                @mapping.store("bottom", c)
            end
        end
        # * and can now solve top_left from t_l+m
        @mapping.store("top_left", @mapping.fetch("top_left").delete(@mapping.fetch("middle")))
        # * and bottom left
        @mapping.store("bottom_left", @mapping.fetch("bottom_left").delete(@mapping.fetch("bottom")))

        # * top_right and bottom_right are both in 1

        for o in 0..3

            if @output[o].length == 2 then
                @output[o] = 1
                next
            elsif @output[o].length == 4 then
                @output[o] = 4
                next
            elsif @output[o].length == 3 then
                @output[o] = 7
                next
            elsif @output[o].length == 7 then
                @output[o] = 8
                next
            end

            # * 6
            if @output[o].include?(@mapping.fetch("top")) &&
               @output[o].include?(@mapping.fetch("middle")) &&
               @output[o].include?(@mapping.fetch("bottom")) &&
               @output[o].include?(@mapping.fetch("top_left")) &&
               @output[o].include?(@mapping.fetch("bottom_left")) then
                # * bottom right is remaining letter
                b_r = @output[o]
                b_r = b_r.delete(@mapping.fetch("top"))
                b_r = b_r.delete(@mapping.fetch("middle"))
                b_r = b_r.delete(@mapping.fetch("bottom"))
                b_r = b_r.delete(@mapping.fetch("top_left"))
                b_r = b_r.delete(@mapping.fetch("bottom_left"))
                @mapping.store("bottom_right", b_r)
                # * and this is a 6
                @output[o] = 6
                next
            end

            # * 2
            if @output[o].include?(@mapping.fetch("top")) &&
                @output[o].include?(@mapping.fetch("middle")) &&
                @output[o].include?(@mapping.fetch("bottom")) &&
                (not @output[o].include?(@mapping.fetch("top_left"))) &&
                @output[o].include?(@mapping.fetch("bottom_left")) then
                 # * top right is remaining letter
                 t_r = @output[o]
                 t_r = t_r.delete(@mapping.fetch("top"))
                 t_r = t_r.delete(@mapping.fetch("middle"))
                 t_r = t_r.delete(@mapping.fetch("bottom"))
                 t_r = t_r.delete(@mapping.fetch("bottom_left"))
                 @mapping.store("top_right", t_r)
                 # * and this is a 2
                 @output[o] = 2
                 next
            end

            # * 5
            if  @output[o].length == 5 &&
                @output[o].include?(@mapping.fetch("top")) &&
                @output[o].include?(@mapping.fetch("middle")) &&
                @output[o].include?(@mapping.fetch("bottom")) &&
                @output[o].include?(@mapping.fetch("top_left")) &&
                (not @output[o].include?(@mapping.fetch("bottom_left"))) then
                 # * top right is remaining letter
                 t_r = @output[o]
                 t_r = t_r.delete(@mapping.fetch("top"))
                 t_r = t_r.delete(@mapping.fetch("middle"))
                 t_r = t_r.delete(@mapping.fetch("bottom"))
                 t_r = t_r.delete(@mapping.fetch("top_left"))
                 @mapping.store("top_right", t_r)
                 # * and this is a 5
                 @output[o] = 5
                 next
            end

            if @output[o].length == 5 then
                @output[o] = 3
                next
            end

            # * 9 and 0
            if not @output[o].include?(@mapping.fetch("middle")) then
                @output[o] = 0
            else
                @output[o] = 9
            end

        end

    end

    def set_value
        @value = @output.join.to_i
    end

end

displays = []

i = 0
while i < input.length
    displays.push(Display.new(input[i][0], input[i][1]))
    i += 1
end

sum = 0
for d in displays
    d.map
    d.set_value
    sum += d.value
    # print d.value, "\n"
    # print("#{d.input} -> #{d.output}\n -> #{d.mapping}\n\n")
end

puts sum