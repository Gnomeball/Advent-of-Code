use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

use std::collections::HashMap;

fn main() {
    let path = Path::new("data/day07.txt");
    let lines = get_lines(path);
    let nodes = build_nodes(&lines);

    // I found this manually:
    let root = "vtzay";
    // Open up your text editor, search for the first node,
    // if it's only found once, it's the root,
    // else, go to it, and now search for it's parent.  Repeat.
    let node = nodes.get(root).unwrap();

    println!("{}", node_string(node, &nodes));
    // Part two I searched for manually.
    // (The above function returns valid JSON)
}

fn get_lines<P>(path: P) -> Vec<String> where P: AsRef<Path> {

    fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
    where P: AsRef<Path> {
        let file = File::open(filename)?;
        return Ok(io::BufReader::new(file).lines());
    }

    let mut lines = Vec::new();

    if let Ok(data) = read_lines(path) {
        for line in data {
            if let Ok(ip) = line {
                lines.push(ip);
            }
        }
    }

    return lines;
}

/// A data type to store a node
///
/// They will store a name, a weight, and a Vector of Strings
///
/// The String vector will be the names of their nodes child nodes
struct Node { label: String, weight: usize, children: Vec<String> }

/// Given a String, build a Node
///
/// First, we split the line into tokens seperated by whitespace.
///
/// Then, if it has length of 2, it is of the basic form "LABEL (WEIGHT)",
/// else, it has child nodes "LABEL (WEIGHT) -> {CHILDREN}".
///
/// At this time we do nothing with the child nodes other than store their labels.
fn build_node(line: &String) -> Node {
    let tokens: Vec<&str> = line.split_ascii_whitespace().collect();

    let mut ins = Node {
        label: String::from(tokens[0]),
        weight: tokens[1][1..tokens[1].len()-1].parse::<usize>().unwrap(),
        children: Vec::new() // add these below
    };

    if tokens.len() == 2 {
        // Node is basic
    } else {
        // Node has children
        for token in 3..tokens.len() {
            // Build and add child
            // println!("CHILD: {}", tokens[token]);
            let tok = tokens[token].replace(",", "");
            ins.children.push(tok);
        }
    }

    return ins;
}

/// Construct a Hashmap of name -> Node
///
/// This might help to resolve the maths?
fn build_nodes(lines: &Vec<String>) -> HashMap<String, Node> {

    let mut nodes: HashMap<String, Node> = HashMap::new();

    for line in lines {
        let tokens: Vec<&str> = line.split_ascii_whitespace().collect();
        let label = String::from(tokens[0]);
        // let weight = tokens[1][1..tokens[1].len()-1].parse::<usize>().unwrap();

        let node = build_node(line);

        nodes.insert(String::from(label), node);
    }

    return nodes;
}

/// Return the String representing this node
///
/// So I can see if stuff works
#[allow(dead_code)]
fn node_string(node: &Node, nodes: &HashMap<String, Node>) -> String {
    let mut output = String::new();
    output.push_str(&format!("[\"{}\", {}, ", node.label, node.weight));
    output.push_str(&format!("{},", node_weight(node, &nodes)));
    for child in &node.children {
        output.push_str(&format!("{},", node_string(nodes.get(child).unwrap(), &nodes)));
    }
    output.pop();
    output.push_str("]");
    return output;
}

/// Return the weight below this mode
fn node_weight(node: &Node, nodes: &HashMap<String, Node>) -> usize {
    let mut this_weight = node.weight;
    if node.children.len() != 0 {
        for child in &node.children {
            this_weight += node_weight(nodes.get(child).unwrap(), nodes);
        }
    }
    return this_weight;
}