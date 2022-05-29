#include <vector>
#include <utility>
#include <assert.h>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int i = 0;
        int n = nums.size();

        while (i < n) {
            if (nums[i] < 1 || nums[i] >= n){
                i++;
            } else if (nums[i] == nums[nums[i]]) {
                i++;
            } else {
                swap(nums[i], nums[nums[i]]);
            }
        }

        i = 1;
        while (i < n) {
            if (nums[i] != i)
                return i;
            i++;
        }
        if (nums[0] == i)
            i++;
        return i;
    }

    int firstMissingPositiveCleaner(vector<int>& nums) {
        int n = nums.size();

        for (int i=0; i<n; i++) {
            while(0 < nums[i] && nums[i] < n && nums[i] != nums[nums[i]])
                swap(nums[i], nums[nums[i]]);
        }

        for (int i=1; i<n; i++)
            if (nums[i] != i)
                return i;

        if (nums[0] == n)
            return n+1;

        return n;
    }

    int firstMissingPositiveSecondAttempt(vector<int>& nums) {
        int i = 0;
        int n = nums.size();

        // shift i into position i-1
        while (i < n) {
            if (0 < nums[i] && nums[i] < n && nums[i] != nums[nums[i]-1]){
                swap(nums[i], nums[nums[i]-1]);
            } else {
                i++;
            }
        }

        for (i=0; i<n; i++)
            if (nums[i] != i+1)
                return i+1;
        return n+1;
    }

    // basically https://leetcode.com/problems/first-missing-positive/discuss/17071/My-short-c%2B%2B-solution-O(1)-space-and-O(n)-time
    int firstMissingPositiveThirdAttempt(vector<int>& nums) {
        int n = nums.size();

        for (int i=0; i<n; i++) {
            while (0 < nums[i] && nums[i] < n && nums[i] != nums[nums[i]-1])
                swap(nums[i], nums[nums[i]-1]);
        }

        for (int i=0; i<n; i++)
            if (nums[i] != i+1)
                return i+1;
        return n+1;
    }
};

int main()
{
    Solution s;

    vector<pair<vector<int>, int>> testcases = {
        {{1,2,0}, 3},
        {{3,4,-1,1}, 2},
        {{7,8,9,10,11,12}, 1},
        {{1}, 2},
        {{2}, 1},
        {{1,1}, 2},
        {{0,1,2,3}, 4},
        {{4,1,2,3}, 5},
    };

    for (auto & [testcase, expected]: testcases) {
        assert(s.firstMissingPositive(testcase) == expected);
        assert(s.firstMissingPositiveCleaner(testcase) == expected);
        assert(s.firstMissingPositiveSecondAttempt(testcase) == expected);
        assert(s.firstMissingPositiveThirdAttempt(testcase) == expected);
    }

}
