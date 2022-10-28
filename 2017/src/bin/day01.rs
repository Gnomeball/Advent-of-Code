use std::path::Path;
use std::fs;

use std::collections::VecDeque;

fn main() {
    let path = Path::new("data/day01.txt");
    let data = fs::read_to_string(path).unwrap();
    let nums = build_vector(data);

    println!("part one: {}", part_one(&nums));
    println!("part two: {}", part_two(&nums));
}

fn build_vector(s: String) -> Vec<u32> {
    return s.bytes().map(|b| b as u32 - 48).collect();
}

fn sum_pairs(left: &Vec<u32>, right: VecDeque<u32>) -> u32 {
    let pairs = left.iter().zip(right.iter());
    let mut count = 0;
    for (a, b) in pairs {
        if a == b { count += a } };
    return count;
}

fn part_one(data: &Vec<u32>) -> u32 {
    let mut data_step: VecDeque<u32> = VecDeque::from(data.clone());
    data_step.push_front(data[data.len()-1]);

    return sum_pairs(data, data_step);
}

fn part_two(data: &Vec<u32>) -> u32 {
    let mut data_step: VecDeque<u32> = VecDeque::from(data.clone());
    for i in 0..data.len() / 2 { data_step.push_front(data[data.len()-i-1]) };

    return sum_pairs(data, data_step);
}

#[test]
fn test_day01_part_one() {

    let tests = [
        ("1122", 3),
        ("1111", 4),
        ("1234", 0),
        ("91212129", 9)
    ];

    for (data, expect) in tests {
        let result = part_one(&build_vector(String::from(data)));
        assert_eq!(result, expect);
    }

}

#[test]
fn test_day01_part_two() {

    let tests = [
        ("1212", 6),
        ("1221", 0),
        ("123425", 4),
        ("123123", 12),
        ("12131415", 4)
    ];

    for (data, expect) in tests {
        println!("Testing {} {}", data, expect);
        let result = part_two(&build_vector(String::from(data)));
        assert_eq!(result, expect);
    }

}
