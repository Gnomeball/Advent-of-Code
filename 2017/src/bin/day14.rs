use std::path::Path;
use std::fs;

fn main() {
    let path = Path::new("data/day14.txt");
    let data = fs::read_to_string(path).unwrap();
    let mut grid = build_grid(data);

    let used: usize = count_used_boxes(&grid);
    println!("Part one = {}", used);

    let groups: usize = count_groups(&mut grid);
    println!("Part two = {}", groups);
}

/// Do n steps of the knot hash algorithm
fn step(lengths: &[usize], rope: &mut Vec<usize>, rounds: usize) {
    let len = rope.len();
    // Track the skip and the position.
    let mut skip = 0;
    let mut pos = 0;
    // For the given number or rounds,
    for _round in 0..rounds { for length in lengths {
        for i in 0..(length / 2) {
            // do the required swaps.
            rope.swap((pos + i) % len, (pos + length - i - 1) % len) };
        // After the swaps, move the position and increment the skip.
        pos += length + skip;
        skip += 1;
    }}
}

/// Take in a string, return the knot hash
fn knot_hash(data: String) -> String {
    // Get the lengths array, this time as bytes
    let mut lengths: Vec<usize> = data.bytes().map(|b| b as usize).collect();
    // Extend with the required extension
    lengths.extend(&[17, 31, 73, 47, 23]);
    let mut rope: Vec<_> = (0..256).collect();
    // Do 64 iterations
    step(&lengths, &mut rope, 64);
    // Take the array, chunk it.
    let dense: Vec<String> = rope.chunks(16)
        // Then map these chunks to their dense values.
        .map(|chunk| chunk.iter().fold(0, |acc, &v| acc ^ v as u8))
        // Then format them back into a string, remembering leading zeros.
        .map(|v| format!("{:08b}", v)).collect();
    // Join them together, and return.
    return dense.join("") as String;
}

/// Taking in a string to build the hash grid from, build that grid
fn build_grid(data: String) -> Vec<Vec<usize>> {
    // First, we open a grid variable into which we build the grid.
    // This variable models a simple 2D array, and is be used to store the
    // binary values of the knot hashes.
    let mut grid: Vec<Vec<usize>> = Vec::new();

    // In addition we will also be "padding" this grid in situ, to do this we
    // will require every edge position in the grid to store the value of 0.
    // This will ensure that when we poll the grid for groups later we do not
    // touch the edge and cannot therefore hit an index out of bounds error.

    // The empty line must be a vector of 130 zeroes, the middle 128 represent
    // an empty hash value, and the extra two account for the left and right
    // padding for the grid.
    let empty_line: Vec<usize> = vec![0; 130];

    // Now that we have everything set up, we can begin building the grid.

    // To begin with, we push one of our empty lines onto the grid,
    // this acts as the top edge.
    grid.push(empty_line.clone());

    // Then, to build the centre of the grid, we have to loop through our
    // indexes, in this case that is the range 0 -> 127.
    for index in 0..128 {

        // To construct each row of the hash we first need to build the string to
        // hash.  For this we take our data string and append the index to the end.
        let hash_input: String = format!("{}-{}", data, index);

        // Then, with this string built we can resolve it's knot hash, and pad it
        // with a zero at either end, to account for the left and right padding.
        let hash_output: String = format!("0{}0", knot_hash(hash_input));

        // Because the hash ouptut is in string form, we now need to convert it
        // to an array. We start this by opening a line varable.
        let mut non_empty_line: Vec<usize> = Vec::new();
        // Then, for each character in the string, we push its value into the array.
        for c in hash_output.chars() { non_empty_line.push(c as usize - 48) };

        // And now that we have constructed that line, we push it into the grid.
        grid.push(non_empty_line);

    }

    // And to finish we push another empty line onto the grid,
    // this acts as the bottom edge.
    grid.push(empty_line.clone());

    return grid;
}

/// Given a grid, count how many boxes are used
fn count_used_boxes(grid: &Vec<Vec<usize>>) -> usize {
    let mut count: usize = 0;
    // For each value in the grid,
    for line in grid { for val in line {
        // if it's used, increment the count.
        if *val == 1 { count += 1 } } };
    return count;
}

/// Given a grid value we already know is used, empty it's group
fn clear_group(x: usize, y: usize, grid: &mut Vec<Vec<usize>>) {
    // We already know it's used, but in order to prevent us overwriting
    // values incorrectly, we put this check inside the function.
    if grid[y][x] == 1 {
        // First, reset this value, so that it cannot be seen again,
        // and prevent infinite recursion,
        grid[y][x] = 0;
        // then, call this function recursively on this values four neighours.
        clear_group(x, y-1, grid); // Above
        clear_group(x+1, y, grid); // Right
        clear_group(x, y+1, grid); // Below
        clear_group(x-1, y, grid); // Left
    }
    // When the initial call of this function exits, we have removed the group
    // from the grid in it's entirety.
}

/// Count the groups in the grid, this makes recursive calls to clear_group
fn count_groups(grid: &mut Vec<Vec<usize>>) -> usize {
    let mut groups: usize = 0;
    // For each value in the grid,
    for y in 0..grid.len() { for x in 0..grid.len() {
        // if we find a used box, this means we have found a group.
        if grid[y][x] == 1 {
            // So, we increment the group counter,
            groups += 1;
            // and we call the recursive method to clear that group.
            clear_group(x, y, grid);
        }
    }}
    return groups;
}