# my @program = slurp("data/day02.txt").split(",");

my $debug = False;

sub debug_three($op, $a, $b, $c, $d) {
    say "$op [ $a ] and [ $b ] for [ $c ] into [ $d ]";
}

sub initialise($noun, $verb) {
    my @prgm = slurp("data/day02.txt").split(",");
    @prgm[1] = $noun;
    @prgm[2] = $verb;
    return @prgm;
}

sub add($ptr, @prgm) {
    my $left   = @prgm[@prgm[$ptr + 1]];
    my $right  = @prgm[@prgm[$ptr + 2]];
    my $result = $left + $right;
    if $debug {
        debug_three("Adding", $left, $right, $result, @prgm[@prgm[$ptr + 3]]);
    }
    @prgm[@prgm[$ptr + 3]] = $result;
    return $ptr + 4
}

sub mult($ptr, @prgm) {
    my $left   = @prgm[@prgm[$ptr + 1]];
    my $right  = @prgm[@prgm[$ptr + 2]];
    my $result = $left * $right;
    if $debug {
        debug_three("Multiplying", $left, $right, $result, @prgm[@prgm[$ptr + 3]]);
    }
    @prgm[@prgm[$ptr + 3]] = $result;
    return $ptr + 4
}

sub run(@state) {
    my $ip = 0;
    my @prgm = initialise(@state[0], @state[1]);
    while @prgm[$ip] != 99 {

        given @prgm[$ip] {
            when 1 {
                say "Found [ ADD ] at [ $ip ]" if $debug;
                $ip = add($ip, @prgm) }
            when 2 {
                say "Found [ MULT ] at [ $ip ]" if $debug;
                $ip = mult($ip, @prgm) }
            default { say "uh oh" }
        }
    }
    return @prgm;
}

my @prgm = run([ 12, 2 ]);

say "Part one = @prgm[0]";

my @noun = reverse(1..99);
my @verb = 1..99;

my $found = False;

for @noun -> $n {
    for @verb -> $v {
        @prgm = run([$n, $v]);
        if @prgm[0] == 19690720 {
            say "Part two = ", $n * 100 + $v;
            $found = True;
            last;
        }
    }
    if $found { last }
}

