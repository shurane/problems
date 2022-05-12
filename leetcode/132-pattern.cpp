#include <vector>
#include <utility>
#include <iostream>
#include <iomanip>
#include <assert.h>
#include "helpers.h"

using namespace std;

class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        vector<pair<int, int>> intervals = {{nums[0], nums[0]}};

        for (int i: nums){
            // cout << "interval: " << intervals.back() << " i: " << i << endl;
            if (i > intervals.back().second) {
                intervals.back().second = i;
                auto [last_lo, last_hi] = intervals.back();

                while (!intervals.empty() && last_hi >= intervals.back().second) {
                    intervals.pop_back();
                }
                intervals.push_back({last_lo, last_hi});

            } else if (i < intervals.back().first) {
                intervals.push_back({i, i});
            }

            // having this for loop is somewhat sub-optimal...
            for (int j=intervals.size()-1; j>=0; j--) {
                // cout << "looking back on previous intervals: " << intervals[j] << endl;
                if (intervals[j].first < i && i < intervals[j].second) {
                    return true;
                }
            }
        }
        return false;
    }

    // inspired from https://leetcode.com/problems/132-pattern/discuss/94077/Java-O(n)-solution-using-stack-in-detail-explanation
    bool find132patternBetter(vector<int>& nums) {
        vector<pair<int, int>> intervals {{nums[0], nums[0]}};

        for (int i: nums) {
            // cout << "first: " << setw(2) << intervals.back().first
            //      << ", second: " << setw(2) << intervals.back().second
            //      << ", i: " << setw(2) << i << endl;
            // i < min, push new interval with {i, i}
            if (i < intervals.back().first) {
                intervals.push_back({i, i});
            // min < i < max
            } else if (intervals.back().first < i  && i < intervals.back().second) {
                return true;
            // max < i
            } else if (intervals.back().second < i) {
                // max < i, update last.second to i and expand interval
                auto last = intervals.back();
                last.second = i;
                intervals.pop_back();

                // get rid of overlapping intervals, where intervals.back().max <= i
                // last.first is already the lowest value for min, so we don't need to check it again
                while (!intervals.empty() && intervals.back().second <= i)
                    intervals.pop_back();

                // min < i < max
                if (!intervals.empty() && intervals.back().first < i)
                    return true;

                intervals.push_back(last);
            }
        }
        return false;
    }

    // // https://leetcode.com/problems/132-pattern/discuss/166953/Easy-and-concise-C%2B%2B-solution-using-a-stack-with-explanation-VERY-EASY-to-understand
    // bool find132patternSimpler(vector<int>& nums) {
    //     vector<int> s;
    //     int prev = INT_MIN;
    //     return false;
    // }
};

int main()
{
    Solution s;

    vector<pair<vector<int>, bool>> testcases = {
        {{1,2,3,4}, false},
        {{3,1,4,2}, true},
        {{-1,3,2,0}, true},
        {{-2,1,2,-2,1,2}, true}, // -2, 2, 1
        {{1,2,3,4,5,6,7,8,9,0}, false},
        {{1,2,3,4,5,6,7,8,9,1}, false},
        {{1,2,3,4,5,6,7,8,9,2}, true},
        {{10,9,8,7,6,7,8,9,10,2,1,6}, false},
        {{10,9,8,7,6,7,8,9,10,2,1,7}, true}, // 6, 10, 7
    };

    testcases.push_back({{}, false});
    vector<int>& last = testcases.back().first;

    for (int i=0; i<int(2*10e5); i++) {
        last.push_back(i*1000*(i%2 == 1 ? -1 : 1));
    }

    for (auto & [nums, expected]: testcases){
        // if (nums.size() < 500)
        //     cout << nums << " " << (expected ? "true" : "false") << endl;
        assert(s.find132pattern(nums) == expected);
        assert(s.find132patternBetter(nums) == expected);
    }
}
