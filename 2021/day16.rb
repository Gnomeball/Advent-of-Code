# literal
# input = "D2FE28"

# operator, lt=0
# input = "38006F45291200"

# operator, lt=1
# input = "EE00D40C823060"

# operator, v=16
# input = "8A004A801A8002F478"

# operator, v=12
# input = "620080001611562C8802118E34"

# operator, v=23
# input = "C0015000016115A2E0802F182340"

# operator, v=31
# input = "A0016C880162017C3686B18A3D4780"

input = File.readlines("data/day16.txt", chomp: true)[0]

hex2bin = {
    "0" => "0000", "1" => "0001", "2" => "0010", "3" => "0011",
    "4" => "0100", "5" => "0101", "6" => "0110", "7" => "0111",
    "8" => "1000", "9" => "1001", "A" => "1010", "B" => "1011",
    "C" => "1100", "D" => "1101", "E" => "1110", "F" => "1111"
}

binary = ""

for c in input.chars
    binary << hex2bin.fetch(c)
end

class Packet

    attr_accessor :version, :type, :length, :data
    @@depth = 0

    def initialize(v, t, l, d)
        @version = v
        @length = l
        @type = t
        @data = d
    end

    def sum
        case @type
        when "100"
            return @version.to_i(2)
        else
            out = @version.to_i(2)
            @data.each { |d| out += d.sum }
            return out
        end
    end

    def resolve
        case @type
        when "000" # * 0 -> sum
            return @data.map { |d| d.resolve }.reduce(&:+)
        when "001" # * 1 -> product
            return @data.map { |d| d.resolve }.reduce(&:*)
        when "010" # * 2 -> minimum
            return @data.map { |d| d.resolve }.min
        when "011" # * 3 -> maximum
            return @data.map { |d| d.resolve }.max
        when "100" # * 4 -> literal
            return (@data.join("")).to_i(2)
        when "101" # * 5 -> greater than
            return @data[0].resolve > @data[1].resolve ? 1 : 0
        when "110" # * 6 -> less than
            return @data[0].resolve < @data[1].resolve ? 1 : 0
        when "111" # * 7 -> equal
            return @data[0].resolve == @data[1].resolve ? 1 : 0
        end
    end

    def to_s
        case @type
        when "100"
            return "[ v : #{@version} , t : #{@type} , d : #{(@data.join("")).to_i(2)} ]"
        else
            out = "[ v : #{version} , t : #{@type} , l : #{@length} , d : \n"

            @data.each do |d|
                @@depth += 4
                out << " " * @@depth << "#{d.to_s}\n"
                @@depth -= 4
            end

            out << " " * @@depth << "]"
        end
    end

end

def next_packet_type(bin)
    case bin[3...6]
    when "100"
        return "literal"
    else
        return "operator"
    end
end

def read_literal(bin)
    index = 0
    # * version
    version = bin[index...index+=3]
    # * type
    type = bin[index...index+=3]
    # * data
    data = []
    loop do
        chunk = bin[index...index+=5]
        data.push(chunk[1..])
        break if chunk[0] == "0"
    end
    $packets.push(Packet.new(version, type, 0, data))
    # * return lengthLowercase:tm:
    return index
end

def read_operator(bin)
    index = 0
    # * version
    version = bin[index...index+=3]
    # * type
    type = bin[index...index+=3]
    # * length
    length = bin[index...index+=1]
    # * sub packets
    case length
    when "0"
        sub_packet_length = bin[index...index+=15].to_i(2)
        sub_packet_string = bin[index...index+=sub_packet_length]
        sub_packets = []
        pointer = 0
        loop do
            break if pointer >= sub_packet_length
            spt = next_packet_type(sub_packet_string[pointer..])
            case spt
            when "literal" ;  pointer += read_literal(sub_packet_string[pointer..])
            when "operator" ;  pointer += read_operator(sub_packet_string[pointer..])
            end
            sub_packets.push($packets.pop)
        end
    when "1"
        sub_packet_count = bin[index...index+=11].to_i(2)
        sub_packets = []
        sub_packet_count.times do
            spt = next_packet_type(bin[index..])
            case spt
            when "literal" ;  index += read_literal(bin[index..])
            when "operator" ;  index += read_operator(bin[index..])
            end
            sub_packets.push($packets.pop)
        end
    end
    $packets.push(Packet.new(version, type, length, sub_packets))
    # * return length
    return index
end

$packets = []

index = 0
while index < binary.length
    type = next_packet_type(binary[index..])
    if type == "literal" then
        index += read_literal(binary[index..])
    elsif type == "operator"
        index += read_operator(binary[index..])
    end
    # * round up
    while index % 4 != 0 do index += 1 end
    # * skip empty bytes
    loop do
        byte = binary[index...index+4]
        break if byte != "0000"
        index += 4
    end
end

print("part one = #{$packets[0].sum}\n")
print("part two = #{$packets[0].resolve}\n")
