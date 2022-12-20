my @masses = slurp("data/day01.txt").split("\n");

sub counter_upper ($mass --> Int:D) {
    return (+$mass div 3) - 2;
}

# my $fuels = map(&counter_upper, @masses).sum;
# my $fuels = sum(map(&counter_upper, @masses));
map(&counter_upper, @masses) ==> sum() ==> my $fuels;
# my $fuels <== sum() <== map(&counter_upper, @masses);

say "Part one = $fuels";

sub double-checker ($mass --> Int:D) {
    my $fuel-required = counter_upper($mass);
    my $extra-mass = $fuel-required;
    while counter_upper($extra-mass) > 0 {
        # Oh noes, I'm doing it twice!
        $extra-mass = counter_upper($extra-mass);
        $fuel-required += $extra-mass;
    }
    return $fuel-required;
}

$fuels = map(&double-checker, @masses).sum;

say "Part two = $fuels";