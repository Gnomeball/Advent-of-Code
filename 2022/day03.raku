my @sacks = slurp("data/day03.txt").lines;

# Icky .. but it works 
my $l = "1abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

sub in_both($left, $right --> Str:D) {
    return ~($left (&) $right)
}

sub open_sack($sack --> Seq:D) {
    return $sack.comb.batch($sack.chars div 2);
}

say "Part one = ", @sacks.map(-> $sack
    { $l.index(in_both(|open_sack($sack))) } ).sum;

sub in_all_three($left, $middle, $right --> Str:D) {
    return ~($left.comb (&) $middle.comb (&) $right.comb)
}

say "Part two = ", @sacks.batch(3).map(-> $trio
    { $l.index(in_all_three(|$trio)) } ).sum;
