use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let path = Path::new("data/day13.txt");
    let lines = get_lines(path);

    let mut firewall = build_firewall(lines);
    setup(&mut firewall);
    let result = calculate_score(&mut firewall);
    println!("Part one = {}", result.points);

    let mut done: bool = false;
    let mut offset: usize = 0;

    while !done {
        for i in 0..firewall.len() { step(&mut firewall[i]) };
        // print_firewall(&firewall, offset);
        offset += 1;
        let result = calculate_score(&mut firewall);
        if result.hit == false { println!("Part two = {}", offset); done = true; }
    }
}

fn get_lines<P>(path: P) -> Vec<String> where P: AsRef<Path> {
    fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
    where P: AsRef<Path> {
        let file = File::open(filename)?;
        return Ok(io::BufReader::new(file).lines());
    }
    let mut lines = Vec::new();
    if let Ok(data) = read_lines(path) {
        for line in data { if let Ok(ip) = line { lines.push(ip) } } };
    return lines;
}

/// These exist so I don't have to wrangle .n indexs .. which I really dislike
#[derive(PartialEq)]
enum Direction {
    UP, DOWN
}

struct Wall {
    size: usize,
    pos: usize,
    dir: Direction
}

struct Score {
    points: usize,
    hit: bool
}

/// From a list of lines, build a firewall
///
/// Kind of want this to be accurate because a pretty print could look cool
///
/// Anyway, make a vector, then start adding the bin sizes.  If at any point we
/// encounter a bin that isn't instantly appendable to the array, extend it until
/// we can just push it.  This saves us working out the length ahead of time.
fn build_firewall(lines: Vec<String>) -> Vec<Wall> {
    let mut firewall: Vec<Wall> = Vec::new();
    for line in lines {
        let line = line.replace(":", "");
        let tokens: Vec<usize> = line.split_ascii_whitespace()
            .map(|t| t.parse::<usize>().unwrap()).collect();
        while tokens[0] >= firewall.len() { // Push empty walls
            firewall.push(Wall { size: 0, pos: 0, dir: Direction::DOWN } ) };
        firewall[tokens[0]] = Wall { size: tokens[1], pos: 0, dir: Direction::DOWN };
    }
    return firewall;
}

/// Move a single wall by a single tick
///
/// First we check the direction for a flip, then we move it.
fn step(wall: &mut Wall) {
    if wall.size == 0 {
        // This wall has no height, do nothing
    } else {
        // Check for direction flip
        if wall.pos == wall.size - 1 && wall.dir == Direction::DOWN {
            // If it's at the bottom going down
            wall.dir = Direction::UP;
        }
        if wall.pos == 0 && wall.dir == Direction::UP {
            // If it's at the top and going up
            wall.dir = Direction::DOWN;
        }
        // Move the beam
        match wall.dir {
            Direction::DOWN => wall.pos += 1,
            Direction::UP   => wall.pos -= 1
        }
    }
}

/// Setup the firewall
///
/// We do this by pre-shifting all of the walls by their offset + their
/// position in the array.  This has the effect of staggering time across
/// the array and allows us to calculcate a score in situ.
fn setup(firewall: &mut Vec<Wall>) {
    for i in 0..firewall.len() { for _ in 0..i { step(&mut firewall[i]) } };
}

/// Calculate the score for the firewall
///
/// Because we've alweady "ticked" it, we only need to check index 0 for
/// each wall.  If there's a hit at any point we check that boolean, and
/// we add to the points total.
fn calculate_score(firewall: &mut Vec<Wall>) -> Score {
    let mut points: usize = 0;
    let mut hit: bool = false;
    for i in 0..firewall.len() {
        let wall = &firewall[i];
        if wall.size != 0 && wall.pos == 0 {
            points += i * wall.size;
            hit = true; } }
    return Score{ points, hit };
}

/// Print the firewall
///
/// Turns out this uglier than I thought
#[allow(dead_code)]
fn print_firewall(firewall: &Vec<Wall>, time: usize) {
    // Print the offset
    println!("Offset {}:", time);
    // Column names
    for i in 0..firewall.len() { print!(" {}  ", i) };
    println!();
    // Walls
    let mut max_height: usize = 0;
    for wall in firewall {
        if wall.size > max_height { max_height = wall.size } };
    for h in 0..max_height {
        for wall in firewall {
            print!("{} ", if wall.size > h {
                if wall.pos == h {"[S]"} else {"[ ]"}
            } else {
                if wall.size == 0 && h == 0 {"..."} else {"   "}
            });
        }
        println!();
    }
}