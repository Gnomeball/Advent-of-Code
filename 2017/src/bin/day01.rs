use std::path::Path;
use std::fs;

fn main() {
    let path = Path::new("data/day01.txt");
    let data = fs::read_to_string(path).unwrap();

    println!("part one: {}", part_one(&data.as_bytes()));
    println!("part two: {}", part_two(&data.as_bytes()));
}

fn part_one(data: &[u8]) -> u32 {
    let mut count: u32 = 0;

    for i in 0..data.len()-1 {
        if data[i] == data[i+1] { count += (data[i] as u32) - 48 };
    }
    
    if data[0] == data[data.len()-1] { count += (data[0] as u32) - 48 };

    return count;
}

fn part_two(data: &[u8]) -> u32 {
    let mut count: u32 = 0;

    for i in 0..data.len() {
        let mut other_index = i + data.len() / 2;
        if other_index >= data.len() { other_index -= data.len() };
        if data[i] == data[other_index] { count += (data[i] as u32) - 48 };
    }

    return count;
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
        let result = part_one(&data.as_bytes());
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
        let result = part_two(&data.as_bytes());
        assert_eq!(result, expect);
    }

}
