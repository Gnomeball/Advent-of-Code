use std::path::Path;
use std::fs;

fn main() {
    let path = Path::new("data/day02.txt");
    let data = fs::read_to_string(path).unwrap();
    let lines: Vec<&str> = data.lines().collect();

    let grid = build_grid(lines);

    println!("Part one: {}", part_one(&grid));
    println!("Part two: {}", part_two(&grid));
}

/// The very existance of this function annoys me
fn build_grid(list: Vec<&str>) -> Vec<Vec<usize>> {
    let mut grid = Vec::new();
    for element in list {
        let values: Vec<&str> = element.split(" ").collect();
        let row = values.into_iter()
            .map(|x| x.parse::<usize>().unwrap()).collect();
        grid.push(row);
    }
    return grid;
}

/// Given a line, an array of ints, return the difference
/// between the maximal and minimum values.
fn max_diff_on_line(line: &Vec<usize>) -> usize {
    let min = line.iter().min().unwrap();
    let max = line.iter().max().unwrap();
    return max - min;
}

fn part_one(grid: &Vec<Vec<usize>>) -> usize {
    return grid.into_iter().map(|x| max_diff_on_line(x)).sum();
}

/// Work out if a line has two numbers that divide evenly
fn divise_line(line: &Vec<usize>) -> usize {
    // For each value pair,
    for left in line { for right in line {
        // first check if they're the same,
        if left == right {
            // if so, skip,
            continue };
        // else, check if they divide evenly,
        if left % right == 0 {
            // and if they do, return that,
            return left / right };
    } }
    // else, return zero.
    return 0;
}

fn part_two(grid: &Vec<Vec<usize>>) -> usize {
    return grid.into_iter().map(|x| divise_line(x)).sum();
}
