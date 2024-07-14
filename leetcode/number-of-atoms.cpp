#include <cctype>
#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <utility>
#include <assert.h>

using namespace std;

class Solution {
public:
    string countOfAtoms(string formula) {
        vector<map<string, int>> atoms({{}});

        int i = 0;
        while (i<formula.size()) {
            if (formula[i] == '(') {
                //cout << "found (, pushing onto stack" << endl;
                atoms.push_back({});
            } else if (formula[i] == ')') {
                string digits = "";
                int count = 1;

                findDigits(formula, digits, i);
                if (!digits.empty()) {
                    count = strtol(digits.c_str(), nullptr, 10);
                }
                //cout << "found ), count: " << count << ", popping stack and merging with previous" << endl;
                const int last = atoms.size() - 1;
                for (auto const& [element, amount]: atoms[last]) {
                    //cout << "in stack: " << element << amount << ", multiplying by " << count << endl;
                    atoms[last-1][element] += amount * count;
                }
                atoms.pop_back();
            } else {
                string element = "";
                string digits = "";
                int count = 1;
                element += formula[i];

                findLower(formula, element, i);
                findDigits(formula, digits, i);

                if (!digits.empty()) {
                    count = strtol(digits.c_str(), nullptr, 10);
                }
                //cout << "element: " << element << ", count: "<< count << endl;

                atoms.back()[element] += count;
            }
            i++;
        }

        string result;
        for (auto const& [element, amount]: atoms.back()) {
            result += element;
            if (amount > 1)
                result += to_string(amount);
        }

        return result;
    }

    inline void findDigits(string& source, string& dest, int& i) {
        while (i+1 < source.size() && isdigit(source[i+1])) {
            dest.push_back(source[i+1]);
            i++;
        }
    }

    // could dedupe by using function pointers and make generic of findDigits()
    inline void findLower(string& source, string& dest, int& i) {
        while (i+1 < source.size() && islower(source[i+1])) {
            dest.push_back(source[i+1]);
            i++;
        }
    }
};

int main()
{
    Solution s;
    vector<pair<string, string>> testcases = {
        {"H2O", "H2O"},
        {"Mg(OH)2", "H2MgO2"},
        {"K4(ON(SO3)2)2", "K4N2O14S4"},
    };

    for (auto & [formula, expected]: testcases) {
        assert(s.countOfAtoms(formula) == expected);
    }
}

