my @games = slurp("../data/day02.txt").split("\n");

my %p_1 = "A X" => 4, "A Y" => 8, "A Z" => 3,
          "B X" => 1, "B Y" => 5, "B Z" => 9,
          "C X" => 7, "C Y" => 2, "C Z" => 6;

my %p_2 = "A X" => 3, "A Y" => 4, "A Z" => 8,
          "B X" => 1, "B Y" => 5, "B Z" => 9,
          "C X" => 2, "C Y" => 6, "C Z" => 7;

say "Part one = ", @games.map(-> $game {%p_1{$game}}).sum;
say "Part two = ", @games.map(-> $game {%p_2{$game}}).sum;
