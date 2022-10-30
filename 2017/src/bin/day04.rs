use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let path = Path::new("data/day04.txt");
    let lines = get_lines(path);

    println!("Part one = {}", part_one(&lines));
    println!("Part two = {}", part_two(&lines));
}

fn get_lines<P>(path: P) -> Vec<String> where P: AsRef<Path> {

    fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
    where P: AsRef<Path> {
        let file = File::open(filename)?;
        return Ok(io::BufReader::new(file).lines());
    }

    let mut lines = Vec::new();

    if let Ok(data) = read_lines(path) {
        for line in data {
            if let Ok(ip) = line {
                lines.push(ip);
            }
        }
    }

    return lines;
}

fn line_has_dupes(line: &String) -> bool {
    let mut split: Vec<&str> = line.split_ascii_whitespace().collect();
    for _ in 0..split.len() {
        let item = split.pop().unwrap();
        if split.contains(&item) { return false };
    }
    return true;
}

fn part_one(lines: &Vec<String>) -> u32 {
    let mut count = 0;
    for line in lines {
        if line_has_dupes(&line) {
            count += 1;
        }
    }
    return count;
}

fn line_has_dupes_by_anagram(line: &String) -> bool {
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

fn part_two(lines: &Vec<String>) -> u32 {
    let mut count = 0;
    for line in lines {
        if line_has_dupes_by_anagram(&line) {
            count += 1;
        }
    }
    return count;
}
