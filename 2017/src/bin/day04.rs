use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let path = Path::new("data/day04.txt");
    let lines = get_lines(path);

    let split = split_lines(lines);
    for line in split {
        for token in line {
            println!("{}", token);
        }
    }
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

fn split_line(line: &String) -> Vec<str> {
    return line.split_ascii_whitespace().collect();
}

fn split_lines(lines: Vec<String>) -> Vec<Vec<str>>  {
    let mut split_ls = Vec::new();
    for line in lines {
        split_ls.push(split_line(&line));
    }
    return split_ls;
}

// fn line_has_dupes() {

// }