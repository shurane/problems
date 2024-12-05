#include <vector>
#include <string>
// #include <iostream>
#include <assert.h>

using namespace std;

class Solution {
public:
    bool canChange(string start, string target) {
        vector<int> l_positions;
        vector<int> r_positions;
        int l_count = 0;
        int r_count = 0;
        // const string initial = start;

        for (int i=0; i<target.size(); i++) {
            if (target[i] == 'L') {
                l_positions.push_back(i);
            } else if (target[i] == 'R') {
                r_positions.push_back(i);
            }
            l_count += (start[i] == 'L');
            r_count += (start[i] == 'R');
        }

        if (l_count != l_positions.size() || r_count != r_positions.size()) {
            return false;
        }

        int matches = 0;
        const int total = l_positions.size() + r_positions.size();
        int j=0;
        for (int i=0; i<start.size() && j < l_positions.size(); i++) {
            if (start[i] == 'L') {
                const int expected = l_positions[j];
                int moveLeft = i;
                while (expected <= moveLeft-1 && start[moveLeft-1] == '_') {
                    moveLeft--;
                }

                if (expected != moveLeft) {
                    return false;
                }

                swap(start[i], start[moveLeft]);
                matches++;
                j++;
            }
        }

        j=r_positions.size()-1;
        for (int i=start.size()-1; i>=0 && j>=0; i--) {
            if (start[i] == 'R') {
                const int expected = r_positions[j];
                int moveRight = i;
                while (moveRight+1 <= expected && start[moveRight+1] == '_') {
                    moveRight++;
                }
                if (expected != moveRight) {
                    return false;
                }

                swap(start[i], start[moveRight]);
                matches++;
                j--;
            }
        }

        // cout << "initial: " << initial << ", ";
        // cout << "  final: " << start << ", expected: " << target << endl;
        // cout << "l_count: " << l_count << ", l_pos.size(): " << l_positions.size() << ", ";
        // cout << "r_count: " << r_count << ", r_pos.size(): " << r_positions.size() << ", ";
        // cout << "matches: " << matches << ", total: " << total << endl;
        return matches == total;
    }
};

int main() {
    Solution s;

    assert(s.canChange("____L", "L____") == true);
    assert(s.canChange("__L_L", "LL___") == true);
    assert(s.canChange("__L_L", "L_L__") == true);
    assert(s.canChange("__L_L", "___LL") == false);

    assert(s.canChange("R____", "____R") == true);
    assert(s.canChange("R_R__", "___RR") == true);
    assert(s.canChange("R_R__", "__R_R") == true);
    assert(s.canChange("R_R__", "RR___") == false);

    assert(s.canChange("_L__R__R_", "L______RR") == true);
    assert(s.canChange("R_L_", "__LR") == false);
    assert(s.canChange("_R", "R_") == false);
    assert(s.canChange("R_L__R__R_", "_L______RR") == false);
}