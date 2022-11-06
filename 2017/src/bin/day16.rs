use std::path::Path;
use std::fs;

/// We import this for the programs, it allows them to party like it's 1999.
use std::collections::VecDeque;

fn main() {
    let path = Path::new("data/day16.txt");
    let data = fs::read_to_string(path).unwrap();
    let commands: Vec<&str> = data.split(",").collect();

    let mut programs: VecDeque<String> = "abcdefghijklmnop".chars()
        .map(|c| String::from(c)).collect();

    // For part one, we only need to run the commands once
    run_commands(&commands, &mut programs, 1);
    println!("Part one = {}", Vec::from(programs.clone()).join(""));

    // But, for part two, we need to run them ONE BEEELLION times!
    // But wait, what if there's a cycle?
    let cycle_length = find_cycle_length(&commands, &mut programs);
    // Oh look at that, there is!

    // We now know after how many cycles we return back to the starting position.
    // And as such, only need to run it 1,000,000,000 % cycle length times further.
    run_commands(&commands, &mut programs, 1_000_000_000 % cycle_length);
    println!("Part two = {}", Vec::from(programs.clone()).join(""));
}

/// Find the cycle length.
///
/// This is, how many times we have to wun through the commands list,
/// before we end up back where we started.
fn find_cycle_length(commands: &Vec<&str>, programs: &mut VecDeque<String>) -> usize {
    // To do this, we first set up a counter to track our iterations.
    let mut cycle_length: usize = 0;
    // Then, we run the commands again, and again, until we find a match;
    loop {
        // Run the commands exactly once,
        run_commands(&commands, programs, 1);
        // and increment our counter.
        cycle_length += 1;
        // If after this iteration our programs equal the starting state,
        // we have found a cycle, and can break the loop.  But..
        if Vec::from(programs.clone()).join("") == "abcdefghijklmnop" {
            // We need to add one to account for the cycle during part one.
            cycle_length += 1;
            // Ok, now we can break .. such an ugly keyword
            break;
        }
    }
    // We now know the cycle length, and may use some simple maths
    // to skip quite a lot of computation :)
    return cycle_length;
}

/// Run through the commands n times
fn run_commands(commands: &Vec<&str>, programs: &mut VecDeque<String>, times: usize) {
    for _ in 0..times { for c in commands { run_command(c, programs) } };
}

/// Parse and run a single command
fn run_command(command: &str, programs: &mut VecDeque<String>) {
    // Get the command identifier, this is one of {s, p, x},
    let identifier: (&str, &str) = command.split_at(1);
    // and split the remainder of the command into an iterator.
    let indexes = identifier.1.split("/");
    // Now, try to match the identifier to a process;
    match identifier.0 {
        "s" => { // Spin the programs
            let index: usize = identifier.1.parse::<usize>().unwrap();
            spin(programs, index); },
        "x" => { // Swap two programs by index
            let index: Vec<usize> = indexes.map(
                |i| i.parse::<usize>().unwrap()).collect();
            swap_indexes(programs, index[0], index[1]); },
        "p" => { // Swap two programs by label
            let index: Vec<&str> = indexes.collect();
            swap_programs(programs, index[0], index[1]); },
        _   => return // can't happen
    }
}

/// Spin the programs n times
fn spin(programs: &mut VecDeque<String>, n: usize) {
    // N times.. rotate!
    programs.rotate_right(n)
}

/// Swap two programs by index
fn swap_indexes(programs: &mut VecDeque<String>, a: usize, b: usize) {
    // I did write a manual "temp = a, a = b, b = temp" thing ..
    // .. but then I found this
    programs.swap(a, b);
}

/// Swap two programs by label
fn swap_programs(programs: &mut VecDeque<String>, a: &str, b: &str) {
    // Rather than do anything special here, we work out the indexes,
    let index_a: usize = programs.iter().position(|r| r == a).unwrap();
    let index_b: usize = programs.iter().position(|r| r == b).unwrap();
    // and delegate to the swap by index function.
    swap_indexes(programs, index_a, index_b);
}
