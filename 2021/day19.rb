input = File.read("day19.txt", chomp: true).split("\n\n").map { |s| s.split("\n") }
$scanners = (0...input.length).map { |s| input[s][1..].map { |o| o.split(",").map(&:to_i) } }

def orientations_of(pos)
    x, y, z = pos
    orientations =  [
        [ x,  y,  z ], [ x, -y, -z ], [ -x, -y,  z ], [ -x,  y, -z ],
        [ x,  z, -y ], [ x, -z,  y ], [ -x,  z,  y ], [ -x, -z, -y ]
    ]
    out = []
    for o in orientations
        3.times do
            out.push(o.dup)
            o.rotate!
        end
    end
    return out
end

def get_orientation(o, scanner)
    out = []
    for pos in scanner
        out.push(pos[o].dup)
    end
    return out
end

def get_positions_relative_to(pos, scanner)
    out = []
    x, y, z = scanner[pos]
    for b in scanner
        out.push([ b[0]-x, b[1]-y, b[2]-z ])
    end
    return out
end

def count_overlap(scanner_a, scanner_b)
    count = 0
    for a in scanner_a
        for b in scanner_b
            if a == b then
                count += 1
                return count if count > 12
            end
        end
    end
    return count
end

def get_location_offset(base, offset)
    location = [0, 0, 0]
    for i in 0...3
        location[i] = base[i] - offset[i]
    end
    return location
end

def manhattan(a, b)
    return (a[0]-b[0]).abs + (a[1]-b[1]).abs + (a[2]-b[2]).abs
end

def try_align(index, s_o = 0, s_r = 0, s_rp = 0)

    found = false

    for r_p in s_rp...$beacon_locations.length
        r_ps = get_positions_relative_to(r_p, $beacon_locations)
        # p r_p

        for o in s_o..23
            for r in s_r...$scanners[index].length
                b = get_positions_relative_to(r, get_orientation(o, $scanners[index]))
                overlap = count_overlap(r_ps, b)
                if overlap >= 12 then
                    print("Overlap between base and #{index} at o = #{o} and r = #{r} and r_p = #{r_p}\n")
                    location = get_location_offset($beacon_locations[r_p], $scanners[index][r][o])
                    orientation = o
                    found = true
                    break
                end
                break if found
            end
            break if found
        end
        break if found

    end

    if found then
        $scanner_locations[index] = location
        beacons = get_orientation(orientation, $scanners[index])
        for beacon in beacons
            (0..2).map { |i| beacon[i] += $scanner_locations[index][i] }
            $beacon_locations.push(beacon.dup)
        end
        $beacon_locations.uniq!
    end

    print("#{index} : #{found}\n") if !found
    return found
end

for s in 0...$scanners.length
    for i in 0...$scanners[s].length
        $scanners[s][i] = orientations_of($scanners[s][i])
    end
end

$scanner_locations = Array.new($scanners.length) { [] }
$scanner_locations[0] = [0, 0, 0]
$beacon_locations = []
for beacon in get_orientation(0, $scanners[0])
    $beacon_locations.unshift(beacon.dup)
end

solved = [0]
unsolved = [*1...$scanners.length]


# * order found after running the below loop the first time (which took ages)
order = [
    [ 6,  5,  6,   0], [9,  13,  3,   0], [18,  6,  3,   1], [22, 17, 20,   0], [24, 10, 23,  14],
    [28, 11,  3,  40], [31,  7, 22,   1], [36, 19, 14,   1], [ 1, 18, 19,  53], [ 5,  9,  1,   1],
    [ 8,  8,  9,  53], [13, 20, 19, 131], [14,  4,  5, 135], [15, 15,  2, 121], [19,  7, 21, 142],
    [20, 11, 23,  67], [23,  1, 20,  55], [26, 13, 19,  81], [29, 19, 10, 123], [30,  8,  1,  71],
    [34,  7,  3,  81], [37,  3,  4, 121], [ 3,  3, 14,  59], [12, 10, 24, 191], [17, 22, 17, 200],
    [27, 22, 11, 153], [ 2, 14, 14, 159], [ 7, 21,  8, 305], [10, 19, 24, 267], [21,  2, 23, 159],
    [ 4, 12, 26, 342], [11, 23,  2, 315], [16, 16,  8, 342], [32, 16,  9, 315], [33,  2, 17, 342],
    [35,  6,  7, 315], [25, 12, 12, 384], [38,  9,  7, 316]
]
for o in order
    if try_align(o[0], o[1], o[2], o[3]) then
        unsolved.delete(o[0])
        solved.push(o[0])
    end
end

# while unsolved.length != 0
#     index = unsolved.shift
#     if try_align(index) then
#         solved.push(index)
#         p solved
#         p $scanner_locations
#     else
#         unsolved.push(index)
#     end
# end

print("locations = #{$scanner_locations}\n")
print("part one = #{$beacon_locations.length}\n")

distances = $scanner_locations.permutation(2).map { |a,b| manhattan(a, b) }
print("part two = #{distances.max}\n")
