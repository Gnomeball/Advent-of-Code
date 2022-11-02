use std::path::Path;
use std::fs;

/// This one is fairly simple so can probably be done in a single loop
///
/// For each character, match it against
///  - {, Open Group
///  - }, Close Group
///  - <, Start Garbage
///  - \>, Close Gargage
///  - !, Skip Next
///
/// We don't actually need to track the group or the garbage, merely keep a
/// count of the current group level, score, if we are inside garbage, and if
/// we need to skip the next character.
fn main() {
    let path = Path::new("data/day09.txt");
    let data = fs::read_to_string(path).unwrap();

    // Track the current level, score, garbage, and skip
    let mut current_level: isize = 0;
    let mut score: isize = 0;
    let mut in_garbage: bool = false;
    let mut skip: bool = false;

    // Count up valid garbage characters
    let mut valid_garbage: usize = 0;

    // The loop
    for c in data.chars() {
        // If skip, we go to next char
        if skip { skip = false; continue; }
        // If we are currently in garbage, we count this char
        // Note: the above condition prevents us counting skipped characters
        if in_garbage { valid_garbage += 1 };
        // If we get to here, we need to make a decision
        match c {
            // Open a group, if not in garbage, increment level
            '{' => { if !in_garbage { current_level += 1 } },
            // Close a group, if not in garbage, decrement level,
            // and add ths group's level to the score
            '}' => { if !in_garbage { score += current_level; current_level -= 1 } },
            // Start garbage, nothing special
            '<' => { in_garbage = true },
            // End garbage, and do not count this character as valid garbage
            '>' => { in_garbage = false; valid_garbage -= 1; },
            // Skip next char, and also do not count this character as valid garbage
            '!' => { skip = true; valid_garbage -= 1; },
            // Any other char, skip because we don't care
            _ => continue
        }
    }

    println!("Part one = {}", score);
    println!("Part two = {}", valid_garbage);
}
