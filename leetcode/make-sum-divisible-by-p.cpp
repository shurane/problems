#include <vector>
#include <unordered_map>
#include <iostream>
#include <iomanip>

#include <assert.h>

using namespace std;

// from an editorial peek. because sliding window doesn't work
class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        const int n = nums.size();
        int remainder = 0;
        for (int i=0; i<n; i++) {
            remainder = (remainder + nums[i]) % p;
        }
        // cout << "remainder: " << remainder << ", p: " << p << endl;

        if (remainder == 0) return 0;

        unordered_map<int, int> modmap;
        modmap[0] = -1;
        int sum = 0;
        int best = n;

        for (int i=0; i<n; i++) {
            sum = (sum + nums[i]) % p;
            int needed = (sum - remainder + p) % p;
            // cout << "i: " << setw(2) << i << ", sum: " << setw(3) << sum << ", needed: " << setw(3) << needed << endl;

            if (modmap.find(needed) != modmap.end()) {
                // cout << "i: " << setw(2) << i << ", found: " << modmap[needed] << ", len: " << i - modmap[needed] << endl;
                best = min(best, i - modmap[needed]);
            }
            modmap[sum] = i;
        }

        if (best == n) return -1;
        return best;

    }
};

int main() {
    Solution s;
    vector<tuple<vector<int>, int, int>> testcases = {
        {{3, 1, 4, 2}, 6, 1},
        {{6,3,5,2}, 9, 2},
        {{1,2,3}, 3, 0},
        {{1000000000,1000000000,1000000000}, 3, 0},
        {{26,19,11,14,18,4,7,1,30,23,19,8,10,6,26,3}, 26, 3},
    };
    for (auto& [nums, p, expected]: testcases) {
        assert(s.minSubarray(nums, p) == expected);
    }
}