my @sacks = slurp("data/day03.txt").split("\n");

sub priority($char --> Int:D) {
    my $priority = ord($char);
    if $priority >= 64 && $priority <= 90 {
        return $priority - 38 } # upper
        return $priority - 96;  # lower
}

sub in_both($left, $right --> Str:D) {
    return ~($left (&) $right)
}

sub open_sack($sack --> Seq:D) {
    return $sack.comb.batch($sack.chars div 2);
}

say "Part one = ", @sacks.map(-> $sack
    { priority(in_both(|open_sack($sack))) } ).sum;

sub in_all_three($left, $middle, $right --> Str:D) {
    return ~($left.comb (&) $middle.comb (&) $right.comb)
}

say "Part two = ", @sacks.batch(3).map(-> $trio
    { priority(in_all_three(|$trio)) } ).sum;
