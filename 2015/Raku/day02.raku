#!/usr/bin/env raku
use v6.d;

my @dimensions = slurp("../data/day02.txt").lines.map({
    my ($l, $w, $h) = .split('x').map(*.Int);
    ($l, $w, $h)
});

sub part_one(@dimensions) {
    @dimensions.map(-> ($l, $w, $h) {
        # Calculate the sides, and sort the smallest one into $a,
        my ($a, $b, $c) = ($l * $w, $w * $h, $h * $l).sort;
        # adding it again here
        2 * ($a + $b + $c) + $a
    }).sum
}

say part_one(@dimensions);

sub part_two(@dimensions) {
    @dimensions.map(-> ($l, $w, $h) {
        # Drop the largest one by sorting
        my ($a, $b) = ($l, $w, $h).sort;
        # 2x the rest, plus the bow
        2 * ($a + $b) + ($l * $w * $h)
    }).sum
}

say part_two(@dimensions);
