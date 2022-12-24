my @sacks = slurp("data/day03.txt").split("\n");

sub open_sack ($sack --> Array:D) {
    my $length = $sack.chars;
    my $middle = $length / 2;
    return [ $sack.substr(      0, $middle),   # Left
             $sack.substr($middle, $length) ]; # Right
}

sub in_both (@compartments --> Str:D) {
    for @compartments.first.comb -> $char {
        if @compartments.tail.contains($char) {
            return $char } }
}

sub priority ($char --> Int:D) {
    my $priority = ord($char);
    if $priority >= 64 && $priority <= 90 {
        return $priority - 38 } # upper
        return $priority - 96;  # lower
}

say "Part one = ", @sacks.map(-> $sack
    { priority(in_both(open_sack($sack))) }).sum;

# part two will have to wait, my battery is on 1% (oops)

