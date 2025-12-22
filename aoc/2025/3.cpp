#include <format>
#include <fstream>
#include <string>
#include <vector>
#include <assert.h>

#include "rang.hpp"

using namespace std;

void part1(istream&& file) {
    string line;

    int total = 0;
    while(getline(file, line) && line.size() != 0) {
        // could also do this via a monotonic stack to get O(n), but not really necessary for such a small input
        // get that simple O(n^2) solution
        int best = 0;
        for (int i=0; i<line.size(); i++) {
            for (int j=i+1; j<line.size(); j++) {
                best = max(best, (line[i] - '0') * 10 + (line[j] - '0'));
            }
        }
        total += best;
    }
    cout << "part 1: " << total << endl;
}

string format_runs(vector<vector<int>>& stacks) {
    string result;

    for (const auto& stack :stacks) {
        for (const int num: stack) {
            if (num == -1) {
                result.push_back('_');
            } else {
                result.push_back('0' + num);
            }
        }

        if (stack != stacks.back()) {
            result += ", ";
        }
    }

    return result;
}

// I could make this work, but would need to combine the stack to an adjacent stack when it's only composed of 1 digit
long long joltage_runs(const string& line, const int keep, bool debug = false) {
    int kick = line.size() - keep;
    vector<vector<int>> stacks = {{}};

    for (char c: line) {
        const int n = c - '0';
        if (!stacks.back().empty() && stacks.back().back() > n) {
            stacks.push_back({});
        }
        stacks.back().push_back(n);
    }

    if (debug) {
        cout << rang::fg::cyan << "initial: " << line << rang::fg::reset << endl;
        cout << format(" initial     : kick: {}, stacks: {}", kick, format_runs(stacks)) << endl;
    }

    for (int i=0; i<stacks.size() && kick > 0; i++) {
        auto& stack = stacks[i];
        int j=0;
        while (kick > 0 && j < stack.size()-1 && stack[j] < stack.back()) {
            stack[j] = -1;
            j++;
            kick--;
        }
    }

    if (debug)
        cout << format(" forward pass: kick: {}, stacks: {}", kick, format_runs(stacks)) << endl;

    for (int i=stacks.size()-1; i>=0 && kick > 0; i--) {
        auto& stack = stacks[i];
        int j=stack.size()-1;
        while (kick > 0 && j >= 0 && stack[j] != -1) {
            stack[j] = -1;
            j--;
            kick--;
        }
    }

    if (debug)
        cout << format("backward pass: kick: {}, stacks: {}", kick, format_runs(stacks)) << endl;

    long long result = 0;

    for (const auto& stack: stacks) {
        for (int value: stack) {
            if (value == -1) {
                continue;
            }
            result = (result * 10) + value;
        }
    }

    if (debug)
        cout << rang::fg::yellow << "result: " << result << rang::fg::reset << endl;

    return result;
}

long long joltage_stack(const string& line, const int keep) {
    int kick = line.size() - keep;
    vector<int> stack;

    for (const char c: line) {
        const int n = c - '0';
        while (!stack.empty() && kick > 0 && stack.back() < n) {
            stack.pop_back();
            kick--;
        }
        stack.push_back(n);
    }

    while (kick > 0) {
        stack.pop_back();
        kick--;
    }

    long long value = 0;
    for (int n: stack) {
        value = (value * 10) + n;
    }
    return value;
}

void part2(istream&& file, bool debug=false) {
    string line;

    long long total = 0;
    while (getline(file, line) && line.size() != 0) {
        const long long value = joltage_stack(line, 12);
        if (debug)
            cout << "value: " << value << endl;
        total += value;
    }
    cout << rang::fg::green << "part 2: " << total << rang::fg::reset << endl;
}

int main() {
    // part1(ifstream("3.sample.in"));
    // part1(ifstream("3.in"));

    // part2(istringstream("987654321111111\n811111111111119\n234234234234278\n818181911112111"), true);
    part2(ifstream("3.sample.in"), true);
    part2(ifstream("3.in"));
}
