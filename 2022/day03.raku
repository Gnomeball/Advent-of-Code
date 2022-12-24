my @sacks = slurp("data/day03.txt").split("\n");

sub open_sack ($sack --> Array:D) {
    my $length = $sack.chars;
    my $middle = $length / 2;
    return [ $sack.substr(      0, $middle),   # Left
             $sack.substr($middle, $length) ]; # Right
}

sub in_both (@compartments --> Str:D) {
    # Probably a way to do this functionally ..
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
    { priority(in_both(open_sack($sack))) } ).sum;

# part two will have to wait, my battery is on 1% (oops)

sub in_all_three ($left, $middle, $right --> Str:D) {
    # Probably a way to do this functionally ..
    my @in_first_two = [];
    for $left.comb -> $char {
        if $middle.contains($char) {
            @in_first_two.append($char) } }
    return in_both([~@in_first_two, $right]);
}

say "Part two = ", @sacks.batch(3).map(-> $trio
    { priority(in_all_three(|$trio)) } ).sum;
