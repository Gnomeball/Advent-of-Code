fn main() {
    let number = 368078;

    println!("Part one = {}", part_one(number as f32));
    println!("Part two = {}", part_two())
}

fn part_one(number: f32) -> usize {
    let mut step = number.sqrt().floor();
    while step % 2.0 != 0.0 { step += 1.0 };
    let width = step + 1.0;

    let bounds: Vec<f32> = [0.0, 1.0, 2.0, 3.0].iter().map(
        |n| (width * width) - (n * step)).collect();
    let distances: Vec<usize> = bounds.iter().map(
        |b| (b - number).abs() as usize).collect();

    return (step as usize) - distances.iter().min().unwrap();
}

fn part_two() -> usize {
    /*
     * 369601 363010 349975 330785 312453 295229 279138 266330 130654
     *        6591   6444   6155   5733   5336   5022   2450   128204
     *        13486  147    142    133    122    59     2391   123363
     *        14267  304    5      4      2      57     2275   116247
     *        15252  330    10     1      1      54     2105   109476
     *        16295  351    11     23     25     26     1968   103128
     *        17008  362    747    806    880    931    957    98098
     *        17370  35487 37402   39835  42452  45220  47108  48065
     *
     * Yes, I did it manually :p
     */
    return 369601;
}
