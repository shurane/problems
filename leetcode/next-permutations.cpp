#include <iostream>
#include <algorithm>
#include <vector>
#include <assert.h>
#include "helpers.h"
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int k=0;
        for(int i=0; i+1 < nums.size(); i++){
            if (nums[i] < nums[i+1]){
                k = i;
            }
        }

        int best = k;
        for (int i=k; i < nums.size(); i++){
            if (nums[i] > nums[k]){
                best = i;
            }
        }
        if (best != k){
            swap(nums[k], nums[best]);
            reverse(nums.begin() + k + 1, nums.end());
        }
        else {
            reverse(nums.begin(), nums.end());
        }
    }
};

int main()
{
    Solution s;
    vector<vector<int>> v {
        { 1, 5, 7, 9 },
        { 1, 5, 9, 7 },
        { 1, 7, 5, 9 },
        { 1, 7, 9, 5 },
        { 1, 9, 5, 7 },
        { 1, 9, 7, 5 },

        { 5, 1, 7, 9 },
        { 5, 1, 9, 7 },
        { 5, 7, 1, 9 },
        { 5, 7, 9, 1 },
        { 5, 9, 1, 7 },
        { 5, 9, 7, 1 },

        { 7, 1, 5, 9 },
        { 7, 1, 9, 5 },
        { 7, 5, 1, 9 },
        { 7, 5, 9, 1 },
        { 7, 9, 1, 5 },
        { 7, 9, 5, 1 },

        { 9, 1, 5, 7 },
        { 9, 1, 7, 5 },
        { 9, 5, 1, 7 },
        { 9, 5, 7, 1 },
        { 9, 7, 1, 5 },
        { 9, 7, 5, 1 }
    };

    for (int i=0; i<v.size(); i++){
        auto c = v[i];
        int inext = (i + 1) % v.size();
        s.nextPermutation(c);
        //cout << v[i] << " | " << c << endl;
        assert (c == v[inext]);
    }
}

