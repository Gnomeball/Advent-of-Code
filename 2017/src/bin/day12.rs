use std::path::Path;
use std::fs;

use std::collections::HashMap;
use std::collections::HashSet;

fn main() {
    let path = Path::new("data/day12.txt");
    let data = fs::read_to_string(path).unwrap();
    let lines: Vec<String> = data.lines().map(|l| String::from(l)).collect();

    let map = build_map(&lines);
    // println!("{:?}", map);

    let mut remaining_nodes: Vec<usize> = Vec::new();
    for i in 0..2000 { remaining_nodes.push(i) };

    let mut n_groups: usize = 0;

    while remaining_nodes.len() != 0 {
        let node = remaining_nodes.pop().unwrap();
        // println!("Finding links from {}", node);
        let mut links = links_to(node, &map);
        // println!("Links to {} = {:?}", node, links);

        if links[0] == 0 {
            println!("Part One = {}", links.len());
        }

        links.pop();
        for link in links {
            // println!("Removing {}", link);
            let index = remaining_nodes.iter().position(|x| *x == link).unwrap();
            remaining_nodes.remove(index);
        }
        n_groups += 1;
    }

    println!("Part Two = {}", n_groups);

}

/// Convert lines into a HashMap of int -> [int]
fn build_map(lines: &Vec<String>) -> HashMap<usize, HashSet<usize>> {
    let mut map: HashMap<usize, HashSet<usize>> = HashMap::new();

    for line in lines {
        let line = &line.replace(",", " ");
        let tokens: Vec<&str> = line.split_ascii_whitespace().collect();

        let key = tokens[0].parse::<usize>().unwrap();

        let mut values: HashSet<usize> = HashSet::new();
        for i in 2..tokens.len() {
            let digit: usize = tokens[i].parse::<usize>().unwrap();
            values.insert(digit);
        }

        map.insert(key, values);
    }

    return map;
}

/// Check if a link exists
fn link_exists(this: usize, that: usize, map: &HashMap<usize, HashSet<usize>>, tried: &mut HashSet<String>) -> bool {

    // println!("Trying link {} to {}", this, that);
    tried.insert(String::from(format!("{}-{}", this, that)));

    let mut result = false;

    if map.get(&this).unwrap().contains(&that) {
        // if this node link directly
        result = true;
    } else {
        // else, we check its links
        let this_links = map.get(&this).unwrap(); // 2
        for link in this_links {
            // see if this is in there
            let link_string: String = String::from(format!("{}-{}", *link, that));
            if !tried.contains(&link_string) {
                result |= link_exists(*link, that, map, tried);
            }
        }
    }

    // println!("Tried = {:?}", tried);

    return result;
}

/// Return list of all nodes pointing to x
fn links_to(this: usize, map: &HashMap<usize, HashSet<usize>>) -> Vec<usize> {
    let mut links: Vec<usize> = Vec::new();

    for i in 0..=map.len() {
        if link_exists(this, i as usize, &map, &mut HashSet::new()) {
            links.push(i);
        }
    }

    return links;
}