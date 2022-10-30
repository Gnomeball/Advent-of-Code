use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

use std::collections::HashMap;

fn main() {
    let path = Path::new("data/day08.txt");
    let lines = get_lines(path);

    let mut registers = get_registers(&lines);
    run_instructions(&lines, &mut registers);
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

/// Read in the file, return a HashMap of the mentioned registers
///
/// Simple read each line, adding any mentioned register, if such a register
/// already exists, we're only updating the value, this is not a problem.
fn get_registers(lines: &Vec<String>) -> HashMap<String, isize> {
    let mut registers = HashMap::new();

    for line in lines {
        let tokens: Vec<&str> = line.split_ascii_whitespace().collect();
        registers.insert(String::from(tokens[0]), 0);
        registers.insert(String::from(tokens[4]), 0);
    }

    return registers;
}

/// Parse a condition
///
/// Read in post IF condition, return a boolean
fn parse_condition(reg: &str, op: &str, value: &str, registers: &HashMap<String, isize>) -> bool {
    let reg = *registers.get(reg).unwrap();
    let value = value.parse::<isize>().unwrap();
    match op {
        ">" => return reg > value,
        ">=" => return reg >= value,
        "==" => return reg == value,
        "!=" => return reg != value,
        "<=" => return reg <= value,
        "<" => return reg < value,
        _ => return false // can't happen
    }
}

/// Run instructions
fn run_instructions(instructions: &Vec<String>, registers: &mut HashMap<String, isize>) {
    let mut max_during_run: isize = 0;

    for ins in instructions {
        let tokens: Vec<&str> = ins.split_ascii_whitespace().collect();

        let reg = tokens[0];
        let dec = if tokens[1] == "dec" { true } else { false };
        let val = tokens[2].parse::<isize>().unwrap();

        if parse_condition(tokens[4], tokens[5], tokens[6], &registers) {
            // println!("{} {} by {}", tokens[1], reg, val);
            registers.insert(String::from(reg),
                *registers.get(reg).unwrap() + if dec { -val } else { val } );
            // println!("{:?}", registers);

            let current_max = find_max_value(&registers);
            if current_max > max_during_run { max_during_run = current_max };
        }
    }

    println!("Part one = {}", find_max_value(&registers));
    println!("Part two = {}", max_during_run);
}

/// Find the maximal value
fn find_max_value(registers: &HashMap<String, isize>) -> isize {
    let mut assumed_max: isize = 0;
    for reg in registers.iter() {
        if *reg.1 > assumed_max { assumed_max = *reg.1 };
    }
    return assumed_max;
}