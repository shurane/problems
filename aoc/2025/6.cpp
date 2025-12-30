#include <print>
#include <format>
#include <fstream>
#include <string>
#include <vector>
#include <functional>
#include <algorithm>
#include <assert.h>

#include "rang.hpp"

using namespace std;

bool debug = false;

// I wish we could accept both lvalues and rvalues easily... see https://stackoverflow.com/questions/17644133/function-that-accepts-both-lvalue-and-rvalue-arguments
void part1(istream&& file) {
    vector<vector<string>> lines;
    string line;

    while (getline(file, line) && line.size() != 0) {
        lines.push_back({});

        int i=0;
        while (i<line.size()) {
            if (line[i] == ' ') {
                i++;
                continue;
            }

            int j=i;
            while (j < line.size() && line[j] != ' ') {
                j++;
            }
            lines.back().push_back(line.substr(i, j-i));
            i = j;
        }
    }

    // println("lines: {}", lines);

    vector<vector<long long>> operands;
    vector<char> operators;

    const int m = lines.size() - 1;
    const int n = lines[0].size();

    // grab all the numbers
    for (int i=0; i<m; i++) {
        operands.push_back({});
        for (int j=0; j<n; j++) {
            operands.back().push_back(stoll(lines[i][j]));
        }
    }

    // last line has all the operators
    for (int j=0; j<n; j++) {
        operators.push_back(lines[m][j][0]);
    }

    if (debug) {
        println("operands: {}", operands);
        println("operators: {}", operators);
    }

    long long result = 0;

    // iterate column by column and apply the operator
    for (int j=0; j<n; j++) {
        long long value;
        char op = operators[j];
        std::function<long long(long long, long long)> f;

        if (op == '+') {
            value = 0;
            f = std::plus<>();
        } else {
            value = 1;
            f = std::multiplies<>();
        }

        for (int i=0; i<m; i++) {
            value = f(value, operands[i][j]);
        }

        // println("column {}: {}", j, value);
        result += value;
    }

    cout << rang::fg::green << "part 1: " << result << rang::fg::reset << endl;
}

void part2(ifstream&& file) {
    vector<string> lines;
    string line;

    size_t longest = 0;

    while (getline(file, line) && line.size() != 0) {
        longest = max(longest, line.size());
        lines.push_back(line);
    }

    for (string& line: lines) {
        while (line.size() < longest) {
            line.push_back(' ');
        }
    }

    string operators = lines.back();
    lines.pop_back();


    int i=0;
    while (i<longest) {
        char op = operators[i];
        int j=i+1;
        while (j+1 < longest && operators[j+1] == ' ') {
            j++;
        }

        // i is the operator character, j is the last space before the next operator or end of line
        int width = j - i - 2;
        if (j+1 == longest) {
            width = j - i;
        }

        i = j+1;
    }

    cout << rang::fg::green << "part 2: " << 0 << rang::fg::reset << endl;

}

int main() {
    // part1(ifstream("6.sample.in"));
    // part1(ifstream("6.in"));

    part2(ifstream("6.sample.in"));
    // part2(ifstream("6.in"));
}
