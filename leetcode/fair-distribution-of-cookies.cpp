#include <algorithm>
#include <iostream>
#include <vector>
#include <assert.h>

using namespace std;

class Solution {
public:
    int distributeCookies(vector<int>& cookies, int k) {
        vector<int> children(k);
        return helper(cookies, children, 0);
    }

    int helper(vector<int>& cookies, vector<int>& children, int i) {
        if (i == cookies.size()) {
            // for (int c: children) {
            //     cout << c << " ";
            // }
            // cout << endl;
            return *max_element(children.begin(), children.end());
        }

        int unfairness = INT_MAX;
        for (int j=0; j<children.size(); j++) {
            children[j] += cookies[i];
            unfairness = min(unfairness, helper(cookies, children, i+1));
            children[j] -= cookies[i];
        }

        return unfairness;
    }
};

int main()
{
    Solution s;

    vector<tuple<vector<int>, int, int>> testcases = {
        {{8, 15, 10, 20, 8}, 2, 31},
        {{6,1,3,2,2,4,1,2}, 3, 7},
    };

    for (auto& [cookies, children, expected]: testcases)
        assert(s.distributeCookies(cookies, children) == expected);
}