use std::path::Path;
use std::fs;

fn main() {
    let path = Path::new("data/day04.txt");
    let data = fs::read_to_string(path).unwrap();
    let lines: Vec<&str> = data.lines().collect();

    println!("Part one = {}", part_one(&lines));
    println!("Part two = {}", part_two(&lines));
}

fn line_has_dupes(line: &str) -> bool {
    let mut split: Vec<&str> = line.split_ascii_whitespace().collect();
    for _ in 0..split.len() {
        let item = split.pop().unwrap();
        if split.contains(&item) { return false };
    }
    return true;
}

fn part_one(lines: &Vec<&str>) -> u32 {
    let mut count = 0;
    for line in lines {
        if line_has_dupes(&line) {
            count += 1;
        }
    }
    return count;
}

fn line_has_dupes_by_anagram(line: &str) -> bool {
    let mut split: Vec<&str> = line.split_ascii_whitespace().collect();
    let mut split_o: Vec<String> = Vec::new();

    // This feels a bit cheap, I dun lyke it ..
    for _ in 0..split.len() {
        let item = split.pop().unwrap();
        let mut chars: Vec<char> = item.chars().collect();
        chars.sort_by(|a, b| b.cmp(a));
        split_o.push(chars.iter().collect());
    }

    for _ in 0..split_o.len() {
        let item = split_o.pop().unwrap();
        if split_o.contains(&item) { return false };
    }

    return true;
}

fn part_two(lines: &Vec<&str>) -> u32 {
    let mut count = 0;
    for line in lines {
        if line_has_dupes_by_anagram(&line) {
            count += 1;
        }
    }
    return count;
}
