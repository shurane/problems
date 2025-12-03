#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <assert.h>

#include "rang.hpp"

using namespace std;

// thanks https://stackoverflow.com/a/1490088/198348
int len_digits(long long number) {
    int len = 1;
    long long pow10 = 10;
    while (pow10 <= number) {
        len++;
        pow10 *= 10;
    }
    return len;
}

void part1(istream&& file, bool debug=true) {
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

        if (debug)
            cout << "left: " << left << ", right: " << right << endl;

        for (long long num=left; num<=right; num++) {
            // could len digits, shift half, then compare first half to second half
            // would be much faster, right?
            // we should also just skip all odd ranges...

            int len = len_digits(num);

            if (len % 2 == 1) {
                long long next = pow(10, len) - 1;
                if (debug)
                    cout << rang::fg::yellow << "skipping this range: "
                         << num << " to " << next << rang::fg::reset << endl;
                num = next;
                continue;
            }

            const int half = len / 2;
            // kind of annoying that this is the same for the entire range of numbers with the same length of digits
            // only way to avoid recomputing is iterating over each length of digits, i.e. 0-9, 10-99, 100-999, etc
            const long long pow10_to_half = pow(10, half);
            const long long r_half = num % pow10_to_half;

            const long long recomposed = r_half * pow10_to_half + r_half;
            //cout << "num: " << num << ", r_half: " << r_half << ", recomposed: " << recomposed << endl;

            if (num == recomposed) {
                if (debug)
                    cout << "match: " << num << endl;
                total += num;
            }
        }
    }

    cout << "part1: " << rang::fg::green << "total: " << total << rang::fg::reset << endl;
}

bool check(long long number) {
    const int len = len_digits(number);

    for (int i=1; i<=len/2; i++) {
        if (len % i != 0) continue;

        const long long pow10 = pow(10, i);
        const long long partial = number % pow10;
        if (partial == 0) continue;

        long long compare = 0;

        while (compare < number) {
            compare = compare * pow10 + partial;
        }

        if (compare == number) {
            return true;
        }
    }

    return false;
}

void part2(istream&& file, bool debug=true) {
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

        if (debug)
            cout << "left: " << left << ", right: " << right << endl;

        for (long long num=left; num<=right; num++) {
            if (check(num)) {
                if (debug)
                    cout << "match: " << num << endl;
                total += num;
            }
        }
    }

    cout << "part2: " << rang::fg::green << "total: " << total << rang::fg::reset << endl;
}

int main() {
    //assert(check(11));
    //assert(check(22));
    //assert(check(111));
    //assert(check(123) == false);
    //assert(check(123123));
    //assert(check(123123123));

    // check that it's skipping the correct ranges
    //part1(istringstream("1-50000"));
    //part1(istringstream("995-1015"));

    part1(ifstream("2.sample.in"), false);
    part1(ifstream("2.in"), false);

    //part2(istringstream("95-115"));
    //part2(istringstream("2121212118-2121212124"));
    part2(ifstream("2.sample.in"), false);
    part2(ifstream("2.in"), false);
}
