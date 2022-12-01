/// Mathsy, I like it
fn main() {
    // Our shift value
    let shift = 380;
    // A "circular" buffer
    let mut buffer = vec![0];
    // The index of the current number
    let mut current = 0;

    // Ok, part one.. we need to loop 2017 times adding the index
    // after shifting the specified number of times.
    for i in 1..=2017 {
        // First we work out where this value needs to go, to do this we
        // add the shift to the current index, increment by one to put it
        // after, then simulate the rotation with a modulus.
        current = 1 + (current + shift) % i;
        // Then, add that number
        buffer.insert(current, i);
    }

    // After the loop, the buffer is complete, so we simply
    // print out the number that comes after that.
    println!("Part one = {}", buffer[current + 1]);

    // Part two is a bit more complicated, here
    // we need to track the index of zero,
    let mut zero = 0;
    // and again where the next number would go.
    let mut next = current;

    // Then, we have to loop fifty million times..
    // (Actually, we only need to do it thirty million times)
    for i in 2018..=29_000_000 {
        // Each time we once again increment by our shift value and
        // simulate the rotation with a modulus.
        next = (next + shift) % i;
        // However, here we don't really want to build the buffer, now do we
        // need to.  We only want to know if this thing is going at index 0.
        // And if it is, we set our pointer to store the value.
        if next == 0 { zero = i };
        // Then, we increment our current position.
        next += 1;
    }

    // Here, we simply print out the value in our pointer.
    println!("Part two = {}", zero);
}
