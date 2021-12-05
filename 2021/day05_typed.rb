input = File.readlines("day05.txt", chomp: true).map { |i|
    i.split(" -> ").map { |e| e.split(",").map { |i| i.to_i } }.flatten }

grid = Array.new(1000) { Array.new(1000) { 0 } }

class Line

    def initialize(x1, y1, x2, y2)
        @start_x = x1
        @start_y = y1
        @stop_x = x2
        @stop_y = y2
        @diagonal = (@start_x - @stop_x).abs == (@start_y - @stop_y).abs
        @straight = (@start_x == @stop_x) || (@start_y == @stop_y)
    end

    def points
        if !@straight and !@diagonal then return [] end
        xs = [*[@start_x, @stop_x].min..[@start_x, @stop_x].max]
        ys = [*[@start_y, @stop_y].min..[@start_y, @stop_y].max]
        if @straight then
            out = []
            xs.each { |x| ys.each { |y| out.push([x, y]) }}
            return out
        end
        if @diagonal then
            if @start_x > @stop_x then xs.reverse! end
            if @start_y > @stop_y then ys.reverse! end
            return xs.zip(ys)
        end
    end

end

for i in input
    x1, y1, x2, y2 = i
    line = Line.new(x1, y1, x2, y2)
    line.points.each { |q| grid[q[0]][q[1]] += 1 }
end

result = grid.flatten.count { |i| i >= 2 }
print("result = #{result}\n")
