#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

// >> Forward declarations

std::vector<int> read_data(std::string filename);
void print_data(std::vector<int> buckets);

// >> Main program

int main() {
    std::string filename = "../data/day01.txt";
    std::vector<int> buckets = read_data(filename);
    print_data(buckets);
}

std::vector<int> read_data(std::string filename) {
    std::ifstream file(filename);
    std::string line;

    int bucket = 0;
    std::vector<int> buckets;

    /// Reading line by line,
    ///   if the line is not empty
    ///     then parse it as a number, and add that number to a counter value.
    ///   if the line found is empty,
    ///     then we store the current value to the buckets, and reset the counter value.

    while (file) {
        std::getline (file, line);
        if (line != "") {
            bucket += std::stoi(line);
        } else {
            buckets.push_back(bucket);
            bucket = 0;
        }
    }

    // Sort the buckets to find the largest bucket,
    std::sort(buckets.begin(), buckets.end(),
    //        reversing them so it's at the front
              std::greater<int>());

    return buckets;
}

void print_data(std::vector<int> buckets) {
    std::cout << "Part one: " << buckets.at(0) << std::endl;
    // there is a better way to do this, no probably about it,
    // but hey, this is fast .. so does it really matter /shrug
    std::cout << "Part two: " << buckets.at(0)
                               + buckets.at(1)
                               + buckets.at(2) << std::endl;
}