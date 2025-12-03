#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <format>
#include <assert.h>

// https://github.com/agauniyal/rang
#include "rang.hpp"

using namespace std;

int mod(int a, int b) {
    return ((a % b) + b) % b;
}

void part1() {
    int lineno = 1;
    int count = 0;
    int dial = 50;
    ifstream file("1.in");
    string line;
    while (getline(file, line) && line.size() != 0) {
        const char direction = line[0];
        const int magnitude = stoi(line.substr(1));
        cout << std::format("{}: {} {}", lineno, direction, magnitude) << endl;

        const int sign = (direction == 'L') ? -1 : 1;
        dial += sign * magnitude;

        dial = mod(dial, 100);
        if (dial == 0) {
            count++;
        }
        lineno++;
    }

    cout << std::format("hit zero {} times", count) << endl;
}

// first time that I learned about anonymous rvalue references via "&&"
int part2(istream&& file, bool debug=false) {
    int lineno = 1;
    int count = 0;
    int dial = 50;
    string line;
    while (getline(file, line) && line.size() != 0) {
        const char direction = line[0];
        const int magnitude = stoi(line.substr(1));
        //cout << std::format("{}: dial: {}, {} {}", lineno, dial, direction, amount) << endl;

        const int sign = (direction == 'L') ? -1 : 1;
        const int amount = sign * magnitude;
        const int before = dial;
        dial += amount;

        int quotient = magnitude / 100;
        const int remainder = mod(dial, 100);
        //if (remainder == 0 && quotient > 0) {
            //quotient--;
        //}
        bool lbound = dial < 0 && 0 < before;
        bool rbound = before < 100 && 100 < dial;

        const int landsOnZero = remainder == 0 && before != 0;
        const int bigRevolutions = quotient + landsOnZero;
        const int smallRevolutions = lbound | rbound;

        if (bigRevolutions)
            count += bigRevolutions;
        else
            count += smallRevolutions;

        if (debug) {
            cout << std::format(
                    "before: {} → {}{} → {} | quotient:{}, remainder:{}, count: {}",
                    before, direction, magnitude, dial, quotient, remainder, count
            ) << endl;
        }

        dial = remainder;
        lineno++;
    }

    if (debug) {
        cout << rang::fg::green << std::format("hit zero {} times", count) << rang::fg::reset << endl;
    }

    return count;
}

int main() {
    //part1();
    assert(part2(ifstream("1.sample.in"), true) == 6);
    assert(part2(istringstream("R1"), true) == 0);
    assert(part2(istringstream("R50\nR0\nL0"), true) == 1);
    assert(part2(istringstream("R1000"), true) == 10);
    assert(part2(istringstream("R149"), true) == 1);
    assert(part2(istringstream("R150"), true) == 2);
    assert(part2(istringstream("R151"), true) == 2);
    assert(part2(istringstream("R50\nL150"), true) == 2);
    assert(part2(istringstream("R50\nR100\nR150"), true) == 3);
    assert(part2(istringstream("R50\nL107\nR8\nL2"), true) == 4);
    assert(part2(istringstream("R51\nL200"), true) == 3);
    assert(part2(istringstream("R51\nL200\nR99"), true) == 4);
    assert(part2(istringstream("R49\nR2\nL2"), true) == 2);
    assert(part2(istringstream("R49\nR2\nL2\nR2"), true) == 3);
    cout << "answer: " << part2(ifstream("1.in"), false) << endl;
}

// 6631 -- too low
//

