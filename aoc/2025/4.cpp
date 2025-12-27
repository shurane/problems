#include <format>
#include <fstream>
#include <string>
#include <vector>
#include <array>
#include <utility>
#include <assert.h>

#include "rang.hpp"

using namespace std;

bool reachable(const vector<string>& matrix, const int i, const int j, const int m, const int n) {
    constexpr array<pair<int, int>, 8> directions = {{
        { 0,  1},
        { 0, -1},
        { 1,  0},
        {-1,  0},
        { 1,  1},
        { 1, -1},
        {-1,  1},
        {-1, -1},
    }};

    int count = 0;
    for (const auto& [y, x]: directions) {
        const int ni = i + y;
        const int nj = j + x;
        if (0 <= ni && ni < m && 0 <= nj && nj < n && (matrix[ni][nj] == '@' || matrix[ni][nj] == 'x')) {
            count++;
        }
    }
    return count < 4;

}

void part1(istream&& file) {
    vector<string> matrix;

    string line;

    while(getline(file, line) && line.size() != 0) {
        matrix.push_back(line);
    }

    const int m = matrix.size();
    const int n = matrix[0].size();
    int total = 0;

    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
            if (matrix[i][j] == '@' && reachable(matrix, i, j, m, n)) {
                matrix[i][j] = 'x';
                total++;
            }
        }
    }

    for (const auto& line: matrix) {
        cout << format("{}", line) << endl;
    }
    cout << "part 1: " << total << endl;
}

int main() {
    part1(ifstream("4.sample.in"));
    part1(ifstream("4.in"));
}
