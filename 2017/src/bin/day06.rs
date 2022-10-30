use std::fs;
use std::path::Path;

fn main() {
    let path = Path::new("data/day06.txt");
    let data = fs::read_to_string(path).unwrap();

    let array: Vec<usize> = data.split_ascii_whitespace().map(
        |x| x.parse::<usize>().unwrap()).collect();

    run(array);
}

#[allow(dead_code)]
fn print_array(array: &Vec<usize>) {
    let mut output = String::new();
    output.push_str("[ ");
    for num in array { output.push_str(&format!("{:0>2} ", num)) };
    output.push_str("]");
    println!("{}", output);
}

/// Collapse the array into a String
///
/// We do this so we can track which states we have seen before.
///
/// Done by simply writing the array values, seperated by a hyphen, into a String.
///
/// We seperate by hyphen to prevent the arrays [ 11 0 ] and [ 1 10 ] appearing equal.
fn collapse_array(array: &Vec<usize>) -> String {
    let mut output = String::new();
    for num in array { output.push_str(&format!("{}-", num)) };
    return output;
}

/// Find the index of the maximal value in the array.
///
/// If two values are equal to this maximum, we should return the index of the first one.
///
/// First, we make the assumption that the highest value lives at index 0.
///
/// Then, we then loop through the array, updating our assumption only when we find a value
/// that is greater than our current assumption.  We do not use >= as this would return the
/// last index of any given maximum, not the first.
///
/// Finally, the assumption is now the index of the maximum value, so we return it.
fn find_max_index(array: &Vec<usize>) -> usize {
    // Our initial assumption
    let mut max_index = 0;
    // Loop
    for index in 0..array.len() {
        if array[index] > array[max_index] {
            max_index = index;
        }
    }
    return max_index;
}

/// Distribute a value across all other values in the array.
///
/// The value we select should be the maximum value.  We should then redistribute it's value
/// across all members of the array evenly by looping over the array.  If we reach the end
/// of the array then we should wrap around.
///
/// First, we find the index of the value to redistribute.
///
/// Then, we store that value a temporary variable, and zero it's index in the array.
///
/// Then, we loop around the array, redistributing it's value by means of adding one to each
/// index of the array, and subtracting one from the temporary variable, until it is zero.
///
/// To ensure we remain inside the array at all times, we use a modulus operation against the
/// length of the array.  This entures the index we move to cannot exceed the length of the array.
///
/// After this process, we return the modified array.
fn distribute(mut array: Vec<usize>) -> Vec<usize> {
    let mut index_to_distribute = find_max_index(&array);
    let mut value_to_distribute = array[index_to_distribute];
    // Zero that value
    array[index_to_distribute] = 0;
    // Track current index
    let mut current_index;
    // Loop
    while value_to_distribute > 0 {
        // Increment index
        index_to_distribute += 1;
        current_index = index_to_distribute % array.len();
        // Redistribute
        array[current_index] += 1;
        value_to_distribute -= 1;
    }
    return array;
}

/// Part one, find the first duplicate state.
///
/// Part two, find the cycle length of the first duplicate.
fn run(mut array: Vec<usize>) {
    // Declare the states array
    let mut states: Vec<String> = Vec::new();
    // and push the starting state
    states.push(collapse_array(&array));

    // Keep track of the first duplicate
    let mut first_dup: String = String::new();
    let mut first_dup_iterations = 0;
    let mut part_one = true;

    loop {
        // Do distribution
        array = distribute(array);

        // Make the new state
        let state = collapse_array(&array);

        // Implicit part two check
        if first_dup == state {
            // print_array(&array);
            // Print out how many extra iterations we've carried out
            println!("Part two = {}", states.len() - first_dup_iterations);
            // And exit the loop, as both parts are now complete
            break;
        }

        // Search for duplicate
        if part_one && states.contains(&state) {
            // We are still doing part one, and this it the first duplicate
            // So we save this state
            first_dup = state;
            // Set which iteration we are on
            first_dup_iterations = states.len();
            // print_array(&array);
            // Print out the value
            println!("Part one = {}", first_dup_iterations);
            // And turn off this check, as we are now in part two
            part_one = false;
        }

        // Add this state
        states.push(collapse_array(&array));
    }
}
