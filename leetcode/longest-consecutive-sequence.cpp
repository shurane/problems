#include <vector>
#include <unordered_map>
#include <utility>
#include <assert.h>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() <= 1) return nums.size();

        unordered_map<int, pair<int, int>> counter;
        int longest = 1;

        for (int num: nums) {
            if (counter.find(num) == counter.end()) {
                // cout << "first occurrence: " << num;
                int lo = num;
                if (counter.find(num-1) != counter.end())
                    lo = counter[num-1].first;

                int hi = num;
                if (counter.find(num+1) != counter.end())
                    hi = counter[num+1].second;

                counter[num] = {lo, hi};
                counter[hi] = {lo, hi};
                counter[lo] = {lo, hi};

                // cout << ", lo: " << lo << ", hi: " << hi << endl;

                longest = max(longest, hi - lo + 1);
            }
        }
        return longest;
    }
};
int main()
{
    Solution s;
    vector<pair<vector<int>, int>> testcases = {
        {{}, 0},
        {{15}, 1},
        {{100,4,200,1,3,2}, 4},
        {{0,3,7,2,5,8,4,6,0,1}, 9},
        {{0,1,2,3,4,5,6,7,8,9}, 10},
        {{9,8,7,6,5,4,3,2,1,0}, 10},
        {{0,9,1,8,2,7,3,6,4,5}, 10},
        {{4,5,3,6,2,7,1,8,0,9}, 10},
        {{0,1,2,3,4,9,8,7,6,0}, 5},
        {{0,1,2,3,4,9,8,7,6,5}, 10},
    };

    for (auto& [testcase, expected]: testcases) {
        assert(s.longestConsecutive(testcase) == expected);
    }

}
