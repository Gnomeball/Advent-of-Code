use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let path = Path::new("data/day02.txt");
    let lines = get_lines(path);
    let grid = build_grid(lines);

    println!("Part one: {}", part_one(&grid));
    println!("Part two: {}", part_two(&grid));
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

fn build_grid(list: Vec<String>) -> Vec<Vec<u32>> {
    let mut grid = Vec::new();
    for element in list {
        let values: Vec<&str> = element.split(" ").collect();
        let row = values.into_iter().map(|x| x.parse::<u32>().unwrap()).collect();
        grid.push(row);
    }
    return grid;
}

#[allow(dead_code)]
fn print_grid(grid: &Vec<Vec<u32>>) {
    for line in grid {
        for element in line {
            print!("{element} ");
        }   println!();
    }
}

fn max_diff_on_line(line: &Vec<u32>) -> u32 {
    let min = line.iter().min().unwrap();
    let max = line.iter().max().unwrap();
    return max - min;
}

fn part_one(grid: &Vec<Vec<u32>>) -> u32 {
    return grid.into_iter().map(|x| max_diff_on_line(x)).sum();
}

fn test_divise(left: f32, right: f32) -> u32 {
    let res = [ left / right, right / left ];
    for r in res { if r == r.trunc() { return r as u32 } };
    return 0;
}

fn divise_line(line: &Vec<u32>) -> u32 {
    for i in 0..line.len() {
        for j in i+1..line.len() {
            let res = test_divise(line[i] as f32, line[j] as f32);
            if res != 0 { return res };
        }
    }
    return 0;
}

fn part_two(grid: &Vec<Vec<u32>>) -> u32 {
    return grid.into_iter().map(|x| divise_line(x)).sum();
}

#[test]
fn test_day02_part_one() {
    let path = Path::new("src/bin/data/day02_p1_test.txt");
    let lines = get_lines(path);
    let grid = build_grid(lines);

    let checksum = part_one(&grid);
    assert_eq!(checksum, 18);
}

#[test]
fn test_day02_part_two() {
    let path = Path::new("src/bin/data/day02_p2_test.txt");
    let lines = get_lines(path);
    let grid = build_grid(lines);

    let checksum = part_two(&grid);
    assert_eq!(checksum, 9);
}
