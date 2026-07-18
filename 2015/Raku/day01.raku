
my @directions = slurp("../data/day01.txt").comb;

# Part one:

# Map +/- 1 over the array and return the sum
say @directions.map({ if $_ eq '(' { 1 } else { -1 } }).sum;

# Part two:

my $floor = 0;
my $position = 0;

# Enumerate the array,
for @directions.kv -> $pos, $dir {
    $floor += $dir eq '(' ?? 1 !! -1;
    # exiting as soon as the floor hits -1
    last if $floor < 0;
    $position = $pos
}

say ($position + 1);
