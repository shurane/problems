#include <vector>
#include <string>
#include <utility>
// #include <iostream>
#include <assert.h>

using namespace std;

class Solution {
public:
    bool canChange(string start, string target) {
        vector<int> s_inds;
        vector<int> t_inds;

        for (int i=0; i<start.size(); i++) {
            if (start[i] != '_') {
                s_inds.push_back(i);
            }
            if (target[i] != '_') {
                t_inds.push_back(i);
            }
        }

        int i=0;
        int j=0;
        for (;i<s_inds.size() && j<t_inds.size(); i++, j++) {
            if (start[s_inds[i]] != target[t_inds[j]] ||
                (start[s_inds[i]] == 'L' && s_inds[i] < t_inds[i]) ||
                (start[s_inds[i]] == 'R' && s_inds[i] > t_inds[i])) {
                return false;
            }
        }

        return i == s_inds.size() && j == t_inds.size();
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