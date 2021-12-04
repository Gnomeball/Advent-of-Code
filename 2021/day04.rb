input = File.readlines("day04.txt", chomp: true)

numbers = input[0].split(",").map { |e| e.to_i }

class Bingo

    def initialize(b)
        @board = b
    end

    def print_board
        for r in 0..4 do
            @board[r].map { |c| print("% 3d" % c) }
            print("\n")
        end
    end

    def remove_number(n)
        for r in 0..4 do
            index = @board[r].index(n) and if index then @board[r][index] = -1 end
        end
    end

    def has_bingo
        for i in 0..4
            return true if @board[i].sum == -5
            return true if @board.transpose[i].sum == -5
        end
        # for i in 0..4
        # end
        return false
        # lines = [*0..4].map { |i| @board[i].sum == -5 or @board.transpose[i].sum == -5 }
        # return lines.reduce(false, :|)
    end

    def score_board(last)
        unmarked = @board.flatten.map { |c| c == -1 ? 0 : c }.sum
        return unmarked * last
    end

end

boards = []

i = 2
while i < input.length do
    board = input[i...i+5].map { |r| r.split(" ").map { |e| e.to_i } }
    boards.push(Bingo.new(board))
    i += 6
end

part_one_found = false

for n in numbers

    if boards.length == 1 then
        # print("\n")
        # boards[0].print_board
        # print("\n")
        boards[0].remove_number(n)
        print("Part two = #{boards[0].score_board(n)}\n")
        break
    end

    boards.map { |b| b.remove_number(n) }

    for b in boards
        if b.has_bingo then
            if not part_one_found then
                # print("\n")
                # b.print_board
                print("Part one = #{b.score_board(n)}\n")
                part_one_found = true
            end
            boards.delete(b)
        end
    end

end

# for n in numbers
#     boards.map { |b| b.remove_number(n) }
#     for b in boards
#         if b.has_bingo then
#             found = true
#             print("Part one = #{b.score_board(n)}\n")
#         end
#     end
#     break if found
# end

# for n in numbers
#     boards.map { |b| b.remove_number(n) }
#     if boards.length == 1 then
#         boards[0].remove_number(n)
#         print("Part two = #{boards[0].score_board(n)}\n")
#         break
#     end
#     boards.map { |b| if b.has_bingo then boards.delete(b) end }
# end
