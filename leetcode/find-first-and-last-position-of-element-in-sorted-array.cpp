#include <vector>
#include <tuple>
#include <assert.h>
using namespace std;

class Solution {
public:
    // https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/573123/C%2B%2B-how-to-nail-binary-search-the-very-first-time(explained)
    vector<int> searchRange(vector<int>& nums, int target) {
        int lowerbound = -1;
        int higherbound = -1;
        int lo, hi, mid;

        lo = 0;
        hi = nums.size() - 1;
        while (lo <= hi) {
            // cout << "lower, lo " << lo << ", hi " << hi << endl;
            mid = (lo + hi) / 2;

            if (target < nums[mid]) {
                hi = mid - 1;
            } else if (target > nums[mid]) {
                lo = mid + 1;
            } else {
                if (mid == lo || nums[mid] != nums[mid-1]) {
                    lowerbound = mid;
                    break;
                } else {
                    hi = mid - 1;
                    lowerbound = mid - 1;
                }
            }
        }

        lo = 0;
        hi = nums.size() - 1;
        while (lo <= hi) {
            // cout << "higher, lo " << lo << ", hi " << hi << endl;
            mid = (lo + hi) / 2;

            if (target < nums[mid]) {
                hi = mid - 1;
            } else if (target > nums[mid]) {
                lo = mid + 1;
            } else {
                if (mid == hi || nums[mid] != nums[mid+1]) {
                    higherbound = mid;
                    break;
                } else {
                    lo = mid + 1;
                    higherbound = mid + 1;
                }
            }
        }

        return {lowerbound, higherbound};
    }
};

int main() {
    Solution s;

    vector<tuple< vector<int>, int, vector<int>>> testcases = {
        {{5,7,7,8,8,10}, 6, {-1, -1}},
        {{5,7,7,8,8,10}, 8, {3, 4}},
        {{-5}, -5, {0, 0}},
        {{-5}, 5, {-1, -1}},
        {{3,3,3}, 3, {0, 2}},
        {{2,3,3,3}, 3, {1, 3}},
        {{3,3,3,4}, 3, {0, 2}},
    };

    for (auto & [nums, target, expected]: testcases) {
        assert(s.searchRange(nums, target) == expected);
    }
}
