$players = [[1, 0], [3, 0]]
$rolls = 0
$dice = 0

def roll
    roll = $dice + 1
    $dice = (($dice + 1) % 100)
    $rolls += 1
    return roll
end

def turn(player)
    r = (0..2).map { |i| roll }.sum
    player[0] = ((player[0] + r) % 10)
    player[0] = 10 if player[0] == 0
    player[1] += player[0]
    player = [player[0], player[1]]
end

loop do
    turn($players[0])
    break if $players[0][1] >= 1000
    turn($players[1])
    break if $players[1][1] >= 1000
end

# print("player 1 l:s = #{$players[0][0]} : #{$players[0][1]}, ")
# print("player 2 l:s = #{$players[1][0]} : #{$players[1][1]}\n")

loosing_score = [$players[0][1], $players[1][1]].min
print("part one = #{loosing_score * $rolls}\n")

def part_two(player_pos, other_pos, player_score, other_score)
    return 1, 0 if player_score >= 21
    return 0, 1 if other_score >= 21

    # * Array of [total score from 3 rolls, n combinations]
    dirac = [[3, 1], [4, 3], [5, 6], [6, 7], [7, 6], [8, 3], [9, 1]]

	total_player_wins = 0
	total_other_wins = 0

	for sum, count in dirac
		new_pos = (player_pos + sum) % 10
		new_score = player_score + new_pos + 1

		other_wins, player_wins = part_two(
            other_pos, new_pos, other_score, new_score)

		total_player_wins += player_wins * count
		total_other_wins += other_wins * count
    end

	return total_player_wins, total_other_wins
end

result = part_two(0, 2, 0, 0)
print("part one = #{result.max}\n")