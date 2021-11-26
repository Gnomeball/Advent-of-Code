require 'digest'

string = "ckczppom"
start = 1

while true do
    puzzle = string + start.to_s
    digest = Digest::MD5.hexdigest(puzzle)
    if digest.to_s[0...5] == "00000"
        puts(digest)
        puts(start)
    end
    if digest.to_s[0...6] == "000000"
        puts(digest)
        puts(start)
        exit
    end
    start += 1
end
