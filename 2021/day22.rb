require 'set'

input = File.readlines("data/day22.txt", chomp: true)

def combine(new_cube, cubes)

    state, x1, x2, y1, y2, z1, z2 = new_cube

    cubes_to_remove = Set[]
    cubes_to_add = Set[]

    added = false

    for cube in cubes

        s1, xx1, xx2, yy1, yy2, zz1, zz2 = cube

        if not (xx1 <= x2 && x1 <= xx2 && yy1 <= y2 && y1 <= yy2 && zz1 <= z2 && z1 <= zz2) then
            # * doesn't intersect
            next
        end

        # * common positions
        nx1 = [xx1, x1].max; nx2 = [xx2, x2].min
        ny1 = [yy1, y1].max; ny2 = [yy2, y2].min
        nz1 = [zz1, z1].max; nz2 = [zz2, z2].min

        # * delete old cube in it's entirety
        cubes_to_remove.add(cube)
        added = true

        # x sections
        if xx1 < nx1 then
            cubes_to_add.add([s1, xx1, nx1-1, yy1, yy2, zz1, zz2])
        end

        if nx2 < xx2 then
            cubes_to_add.add([s1, nx2+1, xx2, yy1, yy2, zz1, zz2])
        end

        # y sections
        if yy1 < ny1 then
            cubes_to_add.add([s1, nx1, nx2, yy1, ny1-1, zz1, zz2])
        end

        if ny2 < yy2 then
            cubes_to_add.add([s1, nx1, nx2, ny2+1, yy2, zz1, zz2])
        end

        # z sections
        if zz1 < nz1 then
            cubes_to_add.add([s1, nx1, nx2, ny1, ny2, zz1, nz1-1])
        end

        if nz2 < zz2 then
            cubes_to_add.add([s1, nx1, nx2, ny1, ny2, nz2+1, zz2])
        end

        cubes_to_add.add([state, [nx1,x1].min, [nx2,x2].max, [ny1,y1].min, [ny2,y2].max, [nz1,z1].min, [nz2,z2].max])

    end

    for td in cubes_to_remove
        cubes.delete(td)
    end

    for ta in cubes_to_add
        cubes.add(ta)
    end

    if !added then
        cubes.add(new_cube)
    end

end

cubes = Set[]

for line in input
    value, ranges = line.split(" ")
    x, y, z = ranges.split(",").map { |o| o[2..].split("..").map(&:to_i) }
    combine([value, x[0], x[1], y[0], y[1], z[0], z[1]], cubes)
end

part_one = 0
part_two = 0

for cube in cubes
    cstate, cx1, cx2, cy1, cy2, cz1, cz2 = cube
    if cstate == "on" then
        for x in [-50, cx1].max..[50, cx2].min
            for y in [-50, cy1].max..[50, cy2].min
                for z in [-50, cz1].max..[50, cz2].min
                    part_one += 1
                end
            end
        end
        part_two += (cx2-cx1+1).abs * (cy2-cy1+1).abs * (cz2-cz1+1).abs
    end
end

print("part one = #{part_one}\n")
print("part two = #{part_two}\n")