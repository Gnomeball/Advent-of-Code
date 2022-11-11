use std::path::Path;
use std::fs;

fn main() {
    let path = Path::new("data/day18.txt");
    let data = fs::read_to_string(path).unwrap();
    let lines: Vec<&str> = data.lines().collect();

    let mut registers = [0; 26];
    let mut sound = 0;

    let instructions = build_instructions(&lines);

    parse_instructions(&instructions, &mut registers, &mut sound);

    println!("Part one = {}", sound);
}

/// To make reading this easier
#[derive(Debug)]
struct Instruction {
    opcode:    String,
    register:  char,
    int_value: isize,
    reg_value: String
}

/// From a list of lines, build the instructions array
fn build_instructions(lines: &Vec<&str>) -> Vec<Instruction> {
    let mut instructions = Vec::new();

    // For each line in the input we need to
    for line in lines {
        // first, break up that line into its respective tokens.
        let tokens: Vec<&str> = line.split_ascii_whitespace().collect();

        // Then, check if this insruction has a second value,
        // if so, we use that, otherwise we use the string of zero.
        let str_value = if tokens.len() == 3 { tokens[2] } else { "0" };

        // Now, things get ugly.
        let mut int_v = 0;
        let mut reg_v = str_value;

        // Using 97 because that's the ascii value of 'a',
        if str_value.bytes().nth(0).unwrap() < 97 /* a */ {
            // and any valid number will be less than that.
            int_v = str_value.parse::<isize>().unwrap();
            // We also set this value so that we know when not to use it.
            reg_v = "EMPTY";
        }

        instructions.push(Instruction {
            opcode:    tokens[0].to_string(),
            register:  tokens[1].chars().nth(0).unwrap(),
            int_value: int_v,
            reg_value: String::from(reg_v)
        } );
    }

    return instructions;
}

/// Parse the instructions
fn parse_instructions(instructions: &Vec<Instruction>, registers: &mut [isize], sound: &mut isize) {
    let mut instruction_pointer: usize = 0;

    loop {
        let instruction = &instructions[instruction_pointer];

        // println!("{:?}", instruction);
        // println!("{}", instruction_pointer);

        let opcode: &str = &instruction.opcode[..];

        let register: usize = instruction.register as usize - 97;

        let value = if instruction.reg_value.eq("EMPTY") { instruction.int_value }
        else { registers[(instruction.reg_value.bytes().nth(0).unwrap() - 97) as usize] };

        match opcode {
            "snd" => { *sound = registers[register] },
            "set" => { registers[register] = value },
            "add" => { registers[register] += value },
            "mul" => { registers[register] *= value },
            "mod" => { registers[register] = registers[register] % value },
            "rcv" => { if registers[register] != 0 { return} },
            "jgz" => {
                if registers[register] > 0 {
                    if value >= 0 { instruction_pointer += value as usize }
                    else { instruction_pointer -= (value - (2*value)) as usize };
                    continue;
                };
            },
            &_ => todo!()
        }

        instruction_pointer += 1;
    }
}