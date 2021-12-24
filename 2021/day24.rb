input = File.readlines("day24.txt", chomp: true).map(&:split)

n_s = Array.new(18) { [] }
for ins in input
    index = 0 if ins == ["inp", "w"]
    n_s[index].push(ins) and index += 1
end

for n in [4, 5, 15]
    print "["
    for i in n_s[n]
        print "% 3d " % i[2]
    end
    print "]\n"
end

#      1   2   3   4   5   6   7   8   9  10  11  12  13  14
# v [  1   1   1  26   1   1   1  26   1  26  26  26  26  26 ]
# t [ 14  10  13  -8  11  11  14 -11  14  -1  -8  -5 -16  -6 ]
# b [ 12   9   8   3   0  11  10  13   3  10  10  14   6   5 ]

# where v[i] == 1 && v[i+1] == 26

# 3 -> 4
# i[4] = i[3] + 8 - 8   = i[3]

# 7 -> 8
# i[8] = i[7] + 10 - 11 = i[7] - 1

# 9 -> 10
# i[10] = i[9] + 3 - 1  = i[9] + 2

# the others, outwards

# 6 -> 11
# i[11] = i[6] + 11 - 8 = i[6] + 3

# 5 -> 12
# i[12] = i[5] + 0 - 5  = i[5] - 5

# 2 -> 13
# i[13] = i[2] + 9 - 16 = i[2] - 7

# 1 -> 14
# i[14] = i[1] + 12 - 6 = i[1] + 6

# Highest

#     1  2  3  4  5  6  7  8  9 10 11 12 13 14
#   [ 3  9  9  9  9  6  9  8  7  9  9  4  2  9 ]

# 39999698799429

# Lowest

#     1  2  3  4  5  6  7  8  9 10 11 12 13 14
#   [ 1  8  1  1  6  1  2  1  1  3  4  1  1  7 ]

# 18116121134117