# Regex is hard, and weird

sub held_entirely_within($min_a, $max_a, $min_b, $max_b) {
    return ($min_a >= $min_b && $max_a <= $max_b) # A inside B
        || ($min_b >= $min_a && $max_b <= $max_a) # B inside A
}

my $held_within = slurp("../data/day04.txt").lines
    .map(-> $line {comb(/\d+/, $line)})
    .map(-> $range {held_entirely_within(|$range)})
    .grep("True").elems;

say "Part one = $held_within";

sub overlap_only_a_bit($min_a, $max_a, $min_b, $max_b) {
    return ($max_a >= $max_b && $min_a <= $max_b) # Right
        || ($max_a >= $min_b && $min_a <= $max_b) # Left
}

my $overlap = slurp("../data/day04.txt").lines
    .map(-> $line {comb(/\d+/, $line)})
    .map(-> $range {overlap_only_a_bit(|$range)})
    .grep("True").elems;

say "Part two = $overlap";
