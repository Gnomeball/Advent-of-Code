# target_x = [*20..30]
# target_y = [*-10..-5]

target_x = [*48..70]
target_y = [*-189..-148]

def simulate(x, y, x_range, y_range)
    pos = [0, 0]
    tick = 0
    while tick < 500
        # x
        pos[0] += x
        x -= 1 if x > 0
        # y
        pos[1] += y
        y -= 1
        return true if x_range.include?(pos[0]) && y_range.include?(pos[1])
        break if pos[0] > x_range.last
        break if pos[1] < y_range.first
        tick += 1
    end
    return false
end

good_ts = []
max_ys = []

for x in 1..target_x.last
    for y in target_y[0]..target_y[0].abs
        if simulate(x, y, target_x, target_y) then
            good_ts.push([x, y])
            max_ys.push((1..y).sum)
        end
    end
end

print("part one = #{max_ys.max}\n")
print("part two = #{good_ts.length}\n")