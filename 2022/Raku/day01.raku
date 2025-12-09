# First attempt, with a loop

# my @elfs = [];

# for slurp("data/day01.txt").split("\n\n")
#     .map(-> $elf {$elf.split("\n")}) -> $snacks {
#         @elfs.append($snacks.sum) }

# @elfs.=sort.=reverse;

# say "Part one = ", @elfs[0];
# say "Part two = ", @elfs[0..2].sum;

# Remembered I can do this..
# And oh wait, batch() exists

my $elfs = slurp("../data/day01.txt").split("\n\n")
    .map(-> $elf {$elf.split("\n")})
    .map(-> $snacks {$snacks.sum})
    .sort.reverse.batch(3).first;

say "Part one = ", $elfs[0];
say "Part two = ", $elfs.sum;
