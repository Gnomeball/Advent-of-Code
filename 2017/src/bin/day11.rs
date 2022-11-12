use std::path::Path;
use std::fs;

fn main() {
    let path = Path::new("data/day11.txt");
    let data = fs::read_to_string(path).unwrap();
    let instructions = build_instructions(data);
    let distances = resolve_distance(instructions);
    // I really don't like how tuples have a .1 syntax ..
    // It too closely looks like a a numeric variable name
    println!("Part one = {:?}", distances.0);
    println!("Part two = {:?}", distances.1);
}

/// Convert a string of comma seperated instructions into a vector
///
/// This is probably a bit verbose, there must be a better way..
fn build_instructions(data: String) -> Vec<String> {
    let data = data.replace(",", " ");
    let tokens: Vec<&str> = data.split_ascii_whitespace().collect();
    let mut instructions: Vec<String> = Vec::new();
    for token in tokens { instructions.push(String::from(token)) };
    return instructions;
}

/// Parse the instructions
///
/// Simply track the current position, imagining the grid as 2d;
///  - North and South are +- 2 on Y
///  - Diagonal moves are +- 1 on X and Y respectively
///
/// After a move, we can use the current location to work out its
/// distance by doing some simple maths
fn resolve_distance(instructions: Vec<String>) -> (isize, isize) {
    // Track the current position
    let mut x: isize = 0;
    let mut y: isize = 0;
    // Track the maximum distance
    let mut max_distance: isize = 0;
    // Loop over each instruction
    for ins in instructions {
        match &ins as &str {
            "n"  => { y += 2; },
            "ne" => { x += 1; y += 1; },
            "se" => { x += 1; y -= 1; },
            "s"  => { y -= 2; },
            "sw" => { x -= 1; y -= 1; },
            "nw" => { x -= 1; y += 1; },
            _    => panic!() // can't happen
        }
        // Calculate the current distance, updating the maximum if required
        let dist = calculate_distance(x.abs(), y.abs());
        if dist > max_distance { max_distance = dist };
    }
    // Return a tuple of (current distance, max distance)
    return (calculate_distance(x.abs(), y.abs()), max_distance);
}

/// Sigh ... I didn't foresee this (sadface)
fn calculate_distance(x: isize, y: isize) -> isize {
    // We are in the right hand segment, so we return the diagonal length
    if x > y { return x };
    // Else, we are in the top right segment, so we
    // Get the distance down to the diagonal
    let diff = (y - x) / 2;
    // And return that, plus the length of the diagonal
    return diff + x;
}