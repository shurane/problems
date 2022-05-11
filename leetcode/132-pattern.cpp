#include <vector>
#include <utility>
#include <iostream>
#include <assert.h>
#include "helpers.h"

using namespace std;

class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        vector<pair<int, int>> intervals = {{nums[0], nums[0]}};

        for (int i=1; i<nums.size(); i++){
            // cout << "interval: " << intervals.back() << " nums[i]: " << nums[i] << endl;
            if (nums[i] > intervals.back().second) {
                intervals.back().second = nums[i];
                auto [last_lo, last_hi] = intervals.back();

                while (!intervals.empty() && last_lo <= intervals.back().first && last_hi >= intervals.back().second) {
                    intervals.pop_back();
                }
                intervals.push_back({last_lo, last_hi});

            } else if (nums[i] < intervals.back().first) {
                intervals.push_back({nums[i], nums[i]});
            }

            for (int j=intervals.size()-1; j>=0; j--) {
                // cout << "looking back on previous intervals: " << intervals[j] << endl;
                if (intervals[j].first < nums[i] && nums[i] < intervals[j].second) {
                    return true;
                }
            }
        }
        return false;
    }
};

int main()
{
    Solution s;

    vector<pair<vector<int>, bool>> testcases = {
        {{1,2,3,4}, false},
        {{3,1,4,2}, true},
        {{-1,3,2,0}, true},
        {{1,2,3,4,5,6,7,8,9,0}, false},
        {{1,2,3,4,5,6,7,8,9,1}, false},
        {{1,2,3,4,5,6,7,8,9,2}, true},
        {{10,9,8,7,6,7,8,9,10,2,1,6}, false},
        {{10,9,8,7,6,7,8,9,10,2,1,7}, true}, //6, 10, 7
    };

    testcases.push_back({{}, false});
    vector<int>& last = testcases.back().first;

    for (int i=0; i<int(2*10e5); i++) {
        last.push_back(i*1000*(i%2 == 1 ? -1 : 1));
    }

    for (auto & [nums, expected]: testcases){
        if (nums.size() < 500)
            cout << nums << " " << (expected ? "true" : "false") << endl;
        assert(s.find132pattern(nums) == expected);
    }
}
