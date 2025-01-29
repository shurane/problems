#include <numeric>
#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>

using namespace std;

class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        const int n = nums.size();
        vector<int> indices(n);
        vector<int> result(n);
        vector<int> indicesSorted;
        iota(indices.begin(), indices.end(), 0);
        sort(indices.begin(), indices.end(), [&](int a, int b) {
            return nums[a] < nums[b];
        });

        int i=0;
        while (i < n) {
            int r=i;
            while (r+1 < n && nums[indices[r]] + limit >= nums[indices[r+1]]) {
                r++;
            }
            // cout << "i: " << i << " to r: " << r << ", values: ";
            // for (int j=i; j<=r; j++) {
            //     cout << nums[indices[j]] << ", ";
            // }
            // cout << endl;

            indicesSorted.resize(r+1-i);
            copy(indices.begin()+i, indices.begin()+r+1, indicesSorted.begin());
            sort(indicesSorted.begin(), indicesSorted.end());

            for (int j=i; j<=r; j++) {
                // cout << "j: " << j << ", indicesSorted[j-i]: " << indicesSorted[j-i] << ", indices[j]: " << indices[j] << endl;
                result[indicesSorted[j-i]] = nums[indices[j]];
            }

            i = r+1;
        }

        return result;
    }
};

int main() {
    Solution s;

    vector<tuple<vector<int>, int, vector<int>>> testcases = {
        {{1,5,3,9,8}, 2, {1,3,5,8,9}},
        {{1,7,6,18,2,1}, 3, {1,6,7,18,1,2}},
        {{1,7,28,19,10}, 3, {1,7,28,19,10}},
        {{1,4,2,3,8}, 2, {1,2,3,4,8}},
        {{8,1,4,2,3}, 2, {8,1,2,3,4}},
        {{51,251,41,241,31,231,21,221,11,211,1,201}, 10, {1,201,11,211,21,221,31,231,41,241,51,251}}
    };

    for (auto& [nums, limit, expected]: testcases) {
        assert (s.lexicographicallySmallestArray(nums, limit) == expected);
    }
}