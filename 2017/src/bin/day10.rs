use std::path::Path;
use std::fs;

/// This one is not simple
fn main() {
    let path = Path::new("data/day10.txt");
    let data = fs::read_to_string(path).unwrap();
    let lengths: Vec<usize> = data.split(",").map(
        |n| n.parse::<usize>().unwrap()).collect();

    let mut nums: Vec<usize> = Vec::new();
    for i in 0..256 { nums.push(i) };

    let mut current_pos: isize = 0;
    let mut skip_size: isize = 0;

    for len in lengths {
        do_exchange(current_pos, len as isize, &mut nums);
        current_pos += len as isize + skip_size;
        skip_size += 1;
    }

    println!("Part one = {}", nums[0] * nums[1]);
}

/// Swap two elements in an array
fn swap(x: usize, y: usize, array: &mut Vec<usize>) -> &mut Vec<usize> {
    let temp = array[x];
    array[x] = array[y];
    array[y] = temp;
    return array;
}

fn do_exchange(pos: isize, len: isize, mut array: &mut Vec<usize>) -> &mut Vec<usize> {

    // get the range to reverse
    let mut start: isize = pos;
    let mut end: isize = pos + len - 1;

    // swap that range
    let range_len: isize = end - start;
    let n_swaps: isize = (range_len as f32 / 2.0).ceil() as isize;

    for _ in 1..=n_swaps {
        start = start % array.len() as isize;
        end = end % array.len() as isize;
        if end < 0 { end += array.len() as isize };
        // println!("Swapping {} and {}", start, end);
        array = swap(start as usize, end as usize, array);
        start += 1;
        end -= 1;
    }

    return array;
}


