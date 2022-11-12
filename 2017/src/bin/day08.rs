use std::path::Path;
use std::fs;

use std::collections::HashMap;

fn main() {
    let path = Path::new("data/day08.txt");
    let data = fs::read_to_string(path).unwrap();
    let lines: Vec<String> = data.lines().map(|l| String::from(l)).collect();

    let mut registers = get_registers(&lines);
    run_instructions(&lines, &mut registers);
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