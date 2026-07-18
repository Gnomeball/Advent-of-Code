use std::path::Path;
use std::fs;

fn main() {
    let path = Path::new("data/day15.txt");
    let data = fs::read_to_string(path).unwrap();
    // I modified the data file to contain only "a b" and no other text
    let a_b: Vec<usize> = data.split_ascii_whitespace()
        .map(|n| n.parse::<usize>().unwrap()).collect();

    println!("Part one = {}", part_one(a_b[0], a_b[1]));
    println!("Part two = {}", part_two(a_b[0], a_b[1]));
}

/// Kinda like ronseal
fn next_factor(num: usize, factor: usize) -> usize {
    // We can use mod here because for this number it's optimised >:)
    return (num * factor) % 2147483647
}

/// Part one
///
/// Ok, so for part one this is rather trivial, we just
/// need to loop the same function forty million times.
///
/// The trick here is not really fancy, just that you ought to not use the modulus
/// operator because it's usually slow.  Except, because we're using Rust here,
/// and underneath it uses C, for the number in question it s actually optimised;
/// and as such acts kind of like a look up table - handy.
fn part_one(mut a: usize, mut b: usize) -> usize {
    let mut matches: usize = 0;
    // The aforementioned loop
    for _ in 0..=40_000_000 {
        // Anyway, get the next factors for A and B
        a = next_factor(a, 16807);
        b = next_factor(b, 48271);
        // Then comes another trick for equivalence, we can do a Binary AND on
        // 0xFFFF to  keep only the 16 bottom bits, making the == operation faster
        if (a & 0xFFFF) == (b & 0xFFFF) {
            // And if they match, we just increment the counter
            matches += 1
        };
    }
    return matches;
}

/// Less like ronseal
fn next_factor_with_limit(num: usize, factor: usize, limit: usize) -> usize {
    // It's a do-while!
    let mut value = next_factor(num, factor);
    while value % limit != 0 {
        value = next_factor(value, factor) };
    return value;
}

/// Part two
///
/// Once again, no trick, just a loop.
///
/// This time only five million iterations though.
///
/// Due to the way the generators in this question are waylaid by their
/// extra constraits this is expected to "catch out" slower algorithms.
fn part_two(mut a: usize, mut b: usize) -> usize {
    let mut matches: usize = 0;
    // The aforementioned loop
    for _i in 0..=5_000_000 {
        // Anyway, get the next factors for A and B
        a = next_factor_with_limit(a, 16807, 4);
        b = next_factor_with_limit(b, 48271, 8);
        // Then comes another trick for equivalence, we can do a Binary AND on
        // 0xFFFF to  keep only the 16 bottom bits, making the == operation faster
        if (a & 0xFFFF) == (b & 0xFFFF) {
            // And if they match, we just increment the counter
            matches += 1
        };
    }
    return matches;
}
