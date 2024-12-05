#include <vector>
#include <string>
#include <utility>
// #include <iostream>
#include <assert.h>

using namespace std;

class Solution {
public:
    bool canChange(string start, string target) {
        vector<pair<int, char>> start_pos;
        vector<pair<int, char>> target_pos;

        for (int i=0; i<start.size(); i++) {
            if (start[i] == 'L') {
                start_pos.push_back({i, 'L'});
            } else if (start[i] == 'R') {
                start_pos.push_back({i, 'R'});
            }

            if (target[i] == 'L') {
                target_pos.push_back({i, 'L'});
            } else if (target[i] == 'R') {
                target_pos.push_back({i, 'R'});
            }
        }

        int i=0;
        int j=0;
        for (;i<start_pos.size() && j<target_pos.size(); i++) {
            if (start_pos[i].second != target_pos[j].second) {
                return false;
            }

            if (start_pos[i].second == 'L' && target_pos[j].first > start_pos[i].first) {
                return false;
            }

            if (start_pos[i].second == 'R' && start_pos[i].first > target_pos[j].first) {
                return false;
            }
            j++;
        }

        return i == start_pos.size() && j == target_pos.size();
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
    assert(s.canChange("_L__R__R_L", "L______RR_") == false);
}