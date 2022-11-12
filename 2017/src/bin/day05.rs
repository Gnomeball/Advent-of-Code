use std::path::Path;
use std::fs;

fn main() {
    let path = Path::new("data/day05.txt");
    let data = fs::read_to_string(path).unwrap();

    let mut nums: Vec<isize> = data.lines().map(
        |i| i.parse::<isize>().unwrap()).collect();
    println!("Part one = {}", run_loop(&mut nums, true));

    let mut nums: Vec<isize> = data.lines().map(
        |i| i.parse::<isize>().unwrap()).collect();
    println!("Part two = {}", run_loop(&mut nums, false));
}

#[allow(dead_code)]
fn print_nums(nums: &Vec<i32>) {
    for num in nums { print!("{} ", num) };
    println!();
}

fn run_loop(nums: &mut Vec<isize>, p1: bool) -> usize {
    let mut steps = 0;

    let mut index: isize = 0;
    let mut current_instruction = nums[index as usize];

    while 0 <= index && index < (nums.len() as isize) {
        steps += 1;

        nums[index as usize] +=
            if p1 || nums[index as usize] < 3 { 1 } else { -1 };

        index += current_instruction;
        if index < 0 || index >= (nums.len() as isize) { break };

        current_instruction = nums[index as usize];
    }

    // print_nums(nums);
    return steps;
}

