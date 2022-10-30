use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let path = Path::new("data/day05.txt");

    let mut nums = get_lines(path);
    println!("Part one = {}", run_loop(&mut nums, true));

    nums = get_lines(path);
    println!("Part two = {}", run_loop(&mut nums, false));
}

fn get_lines<P>(path: P) -> Vec<i32> where P: AsRef<Path> {

    fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
    where P: AsRef<Path> {
        let file = File::open(filename)?;
        return Ok(io::BufReader::new(file).lines());
    }

    let mut lines = Vec::new();

    if let Ok(data) = read_lines(path) {
        for line in data {
            if let Ok(ip) = line {
                lines.push(ip.parse::<i32>().unwrap());
            }
        }
    }

    return lines;
}

#[allow(dead_code)]
fn print_nums(nums: &Vec<i32>) {
    for num in nums { print!("{} ", num) };
    println!();
}

fn run_loop(nums: &mut Vec<i32>, p1: bool) -> u32 {
    let mut steps = 0;

    let mut index: i32 = 0;
    let mut current_instruction: i32 = nums[index as usize];

    while 0 <= index && index < (nums.len() as i32) {
        // println!("{}", index);
        steps += 1;

        nums[index as usize] +=
            if p1 || nums[index as usize] < 3 { 1 } else { -1 };

        index += current_instruction;
        if index < 0 || index >= (nums.len() as i32) { break };

        current_instruction = nums[index as usize];
    }

    // print_nums(nums);
    return steps;
}

