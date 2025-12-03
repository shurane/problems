#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <assert.h>

#include "rang.hpp"

using namespace std;

// thanks https://stackoverflow.com/a/1490088/198348
int count_digits(long long number) {
    int count = 1;
    long long pow10 = 10;
    while (pow10 <= number) {
        count++;
        pow10 *= 10;
    }
    return count;
}

void part1(istream&& file) {
    string line;
    long long total = 0;

    while(getline(file, line, ',') && line.size() != 0) {
        istringstream iss(line);
        string left_str;
        string right_str;
        getline(iss, left_str, '-');
        getline(iss, right_str, '-');

        const long long left = stoll(left_str);
        const long long right = stoll(right_str);

        cout << "left: " << left << ", right: " << right << endl;

        for (long long num=left; num<=right; num++) {
            // could count digits, shift half, then compare first half to second half
            // would be much faster, right?
            // we should also just skip all odd ranges...

            int count = count_digits(num);

            if (count % 2 == 1) {
                long long next = pow(10, count) - 1;
                cout << rang::fg::yellow << "skipping this range: "
                     << num << " to " << next << rang::fg::reset << endl;
                num = next;
                continue;
            }

            const int half = count / 2;
            // kind of annoying that this is the same for the entire range of numbers with the same length of digits
            // only way to avoid recomputing is iterating over each length of digits, i.e. 0-9, 10-99, 100-999, etc
            const long long pow10_to_half = pow(10, half);
            const long long r_half = num % pow10_to_half;

            const long long recomposed = r_half * pow10_to_half + r_half;
            //cout << "num: " << num << ", r_half: " << r_half << ", recomposed: " << recomposed << endl;

            if (num == recomposed) {
                cout << "match: " << num << endl;
                total += num;
            }
        }
    }

    cout << rang::fg::green << "total: " << total << rang::fg::reset << endl;
}

void part2(istream&& file) {
}

int main() {
    // check that it's skipping the correct ranges
    //part1(istringstream("1-50000"));
    //part1(istringstream("995-1015"));

    //part1(ifstream("2.sample.in"));
    //part1(ifstream("2.in"));
    part2(ifstream("2.sample.in"));
    //part2(ifstream("2.in"));
}
