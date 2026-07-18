use std::path::Path;
use std::fs;

pub fn main() {
    let path = Path::new("data/day10.txt");
    let data = fs::read_to_string(path).unwrap();
    let lengths: Vec<usize> = data.split(",").map(
        |n| n.parse::<usize>().unwrap()).collect();

    let mut rope: Vec<_> = (0..256).collect();
    step(&lengths, &mut rope, 1);
    println!("Part one = {}", rope[0] * rope[1]);

    let hash: String = knot_hash(data);
    println!("Part two = {}", hash);
}

/// Do n steps of the algorithm
fn step(lengths: &[usize], rope: &mut Vec<usize>, rounds: usize) {
    let len = rope.len();
    // Track the skip and the position
    let mut skip = 0;
    let mut pos = 0;
    // For the given number or rounds, do the required swaps
    for _round in 0..rounds { for length in lengths {
        for i in 0..(length / 2) {
            rope.swap((pos + i) % len, (pos + length - i - 1) % len) };
        // Move the position and increment the skip
        pos += length + skip;
        skip += 1;
    }}
}

/// Take in a string, return the knot hash
fn knot_hash(data: String) -> String {
    // Get the lengths array, this time as bytes
    let mut lengths: Vec<usize> = data.bytes().map(|b| b as usize).collect();
    // Extend with the required extension
    lengths.extend(&[17, 31, 73, 47, 23]);
    let mut rope: Vec<_> = (0..256).collect();
    // Do 64 iterations
    step(&lengths, &mut rope, 64);
    // Take the array, chunk it
    let dense: Vec<String> = rope.chunks(16)
        // Then map these chunks to their dense values
        .map(|chunk| chunk.iter().fold(0, |acc, &v| acc ^ v as u8))
        // Then format them back into a string, remembering leading zeros
        .map(|v| format!("{:02x}", v)).collect();
    // Join them together, and return
    return dense.join("") as String;
}
