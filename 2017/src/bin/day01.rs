use std::path::Path;
use std::fs;

fn main() {
    let path = Path::new("data/day01.txt");
    let data = fs::read_to_string(path).unwrap();

    // This still probably isn't the best way ..
    let nums: Vec<char> = data.chars().collect();

    // Part one asks us to sum all those numbers which match the next one
    // so we call this function with an offset of 1
    println!("part one: {}", sum_pairs_with_offset(&nums, 1));

    // Part two however, asks us to sum those numbers which match their antipodal
    // value, so this time we call it with an offset of length / 2
    println!("part two: {}", sum_pairs_with_offset(&nums, nums.len() / 2));
}

/// Given a list of characters, sum those that match with their pair by offset.
///
/// Offset values simply point to a value N ahead of the current one,
/// for example in the array ['a', 'b', 'c'], an offset of 1 provides
/// the array ['b', 'c', 'a'], and an offset of 3 would be ['a', 'b', 'c'].
fn sum_pairs_with_offset(array: &Vec<char>, offset: usize) -> usize {
    // In order do collect the sum we first need a calue to store it.
    let mut count: usize = 0;
    // To make things less verbose, we also take a reference to the length.
    let length = &array.len();
    // Now, we loop over the array,
    for i in 0..*length {
        // at each value checking if it matches it's pair by offset,
        if array[i] == array[(i + offset) % *length] {
            // and if they equal, we simply increment the sum.
            count += array[i] as usize - 48 } };
    // And now we return the sum.
    return count;
}