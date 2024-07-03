#include <climits>
#include <functional>
#include <iostream>
#include <queue>
#include <utility>
#include <vector>
#include <assert.h>

using namespace std;

class Solution {
public:
    int minDifference(vector<int>& nums) {
        if (nums.size() <= 4) return 0;

        priority_queue<int> left;
        priority_queue<int, vector<int>, greater<int>> right;

        for (int n: nums) {
            if (right.size() < 4) {
                right.push(n);
            } else if (n > right.top()) {
                left.push(right.top());
                right.pop();
                right.push(n);
            } else {
                left.push(n);
            }

            if (left.size() > 4)
                left.pop();
        }

        vector<int> ends(left.size() + right.size());

        // cout << "left: " << endl;
        while (!left.empty()) {
            // cout << left.top() << " ";
            ends[left.size()-1] = left.top();
            left.pop();
        }
        // cout << endl;

        // cout << "right: " << endl;
        while (!right.empty()) {
            // cout << right.top() << " ";
            ends[ends.size() - right.size()] = right.top();
            right.pop();
        }
        // cout << endl;

        // cout << "ends: " << endl;
        // for (int n: ends) {
        //     cout << n << " ";
        // }
        // cout << endl;

        int mindiff = INT_MAX;
        int i = 0;
        int r = ends.size() - 4;
        while (i < 4) {
            // cout << i << " " << r << " | " << ends[i] << " " << ends[r] << endl;
            mindiff = min(mindiff, ends[r] - ends[i]);
            i++;
            r++;
        }

        return mindiff;
    }
};

int main()
{
    Solution s;
    vector<pair<vector<int>, int>> testcases = {
        {{5,3,2,4}, 0},
        {{1,5,0,10,14}, 1},
        {{3,100,20}, 0},
        {{6,6,0,1,1,4,6}, 2},
        {{10,9,8,7,6,5,4,3,2,1}, 6},
    };

    for (auto & [nums, expected]: testcases) {
        assert(s.minDifference(nums) == 10);
    }

}
