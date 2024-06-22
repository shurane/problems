#include <vector>
#include <tuple>
#include <assert.h>

using namespace std;

class Solution {
public:
    // probably can convert the if statements into adding/multiplying bool(1) vs bool(0)
    int numberOfSubarrays(vector<int>& nums, int k) {
        int nice = 0;
        int odd = 0;
        int l = 0;
        int r = 0;
        int ahead = 1;
        while (l < nums.size()) {
            // cout << "l: " << l << ", r: " << r << endl;
            while (r < nums.size() && odd < k) {
                // cout << "extending r to fit k: " << r << endl;
                if (nums[r] % 2 == 1) odd++;
                r++;
            }
            while (r < nums.size() && nums[r] % 2 != 1) {
                // cout << "extending r==k: " << r << endl;
                ahead++;
                r++;
            }
            if (odd == k) {
                // cout << "adding nice {" << l << "," << r << "}, ahead: " << ahead << endl;
                nice += ahead;
            }
            if (nums[l] % 2 == 1) {
                odd--;
                ahead = 1;
            }
            l++;
        }

        return nice;
    }
};

int main()
{
    Solution s;
    vector<tuple<vector<int>, int, int>> testcases = {
        {{1,1,2,1,1}, 3, 2},
        {{2,4,6}, 1, 0},
        {{2,2,2,1,2,2,1,2,2,2}, 2, 16},
    };

    for (auto & [nums, k, expected]: testcases) {
        assert(s.numberOfSubarrays(nums, k) == expected);
    }
}
