#include <cstdint>
#include <print>
#include <format>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include <assert.h>

#include "rang.hpp"

using namespace std;

bool debug = true;

bool check(vector<pair<int64_t, int64_t>>& ranges, int64_t ingredient) {
    for (const auto& [left, right]: ranges) {
        if (left <= ingredient && ingredient <= right) {
            if (debug)
                cout << "fresh: " << left << ", " << rang::fg::cyan << ingredient << rang::fg::reset << ", " << right << endl;
            return true;
        }
    }
    if (debug)
        cout << "spoiled: " << rang::fg::yellow << ingredient << rang::fg::reset << endl;
    return false;
}

void part1(istream&& file) {
    vector<pair<int64_t, int64_t>> ranges;
    vector<int64_t> ingredients;
    string line;

    while(getline(file, line) && line.size() != 0) {
        int64_t first;
        int64_t second;
        int dash = 0;
        for (int i=0; i<line.size(); i++) {
            if (line[i] == '-') {
                dash = i;
                break;
            }
        }
        const string first_str = line.substr(0, dash);
        const string second_str = line.substr(dash+1);
        first = stoll(first_str);
        second = stoll(second_str);
        if (debug)
            println("first: {} -> {}, second: {} -> {}", first_str, first, second_str, second);
        ranges.push_back({first, second});
    }

    // skip empty line

    while(getline(file, line) && line.size() != 0) {
        ingredients.push_back(stoll(line));
    }

    sort(ranges.begin(), ranges.end());

    if (debug) {
        for (auto& range: ranges) {
            println("range: {}", range);
        }
        // println("ingredients: {}", ingredients);
    }

    // vector<int64_t> spoiled;
    int fresh = 0;
    for (int64_t ingredient: ingredients) {
        if (check(ranges, ingredient)) {
            fresh++;
        } else {
            // spoiled.push_back(ingredient);
        }
    }

    // sort(spoiled.begin(), spoiled.end());
    // for (int64_t s: spoiled) {
    //     cout << "spoiled: " << rang::fg::yellow << s << rang::fg::reset << endl;
    // }

    cout << rang::fg::green << "part1: " << fresh << rang::fg::reset << endl;
}

void part2(istream&& file) {
    vector<pair<int64_t, int64_t>> ranges;
    string line;

    while(getline(file, line) && line.size() != 0) {
        int64_t first;
        int64_t second;
        int dash = 0;
        for (int i=0; i<line.size(); i++) {
            if (line[i] == '-') {
                dash = i;
                break;
            }
        }
        const string first_str = line.substr(0, dash);
        const string second_str = line.substr(dash+1);
        first = stoll(first_str);
        second = stoll(second_str);
        // println("first: {} -> {}, second: {} -> {}", first_str, first, second_str, second);
        ranges.push_back({first, second});
    }

    sort(ranges.begin(), ranges.end());

    vector<pair<int64_t, int64_t>> stack;
    int64_t count = 0;

    for (const auto& [left,right]: ranges) {
        // println("range: {}, {}", left, right);
        if (stack.empty() || stack.back().second < left) {
            // println("push: {}, {}", left, right);
            stack.push_back({left, right});
        } else {
            // const auto t = {left, right};
            // println("extend: {} -> {}, ", stack.back(), t);
            stack.back().second = max(stack.back().second, right);
        }
    }

    while (!stack.empty()) {
        const int64_t amount = stack.back().second - stack.back().first + 1;
        count += amount;
        stack.pop_back();
    }

    cout << rang::fg::green << "part2: " << count << rang::fg::reset << endl;
}

int main() {
    part1(ifstream("5.sample.in"));
    part1(ifstream("5.in"));

    part2(ifstream("5.sample.in"));
    part2(ifstream("5.in"));
}
