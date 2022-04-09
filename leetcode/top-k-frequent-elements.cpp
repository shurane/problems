#include <vector>
#include <unordered_map>
#include <queue>
#include <set>
#include <assert.h>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
        vector<int> res;

        for (auto i: nums) counter[i]++;

        for (auto kv: counter){
            q.push({kv.second, kv.first});
            if (q.size() > k) q.pop();
        }

        while (!q.empty()){
            res.push_back(q.top().second);
            q.pop();
        }

        return res;
    }
};

int main()
{
    Solution s;

    vector<tuple<vector<int>, int, set<int>>> testcases = {
        {{1,1,1,2,2,3}, 2, {2,1}},
        {{1}, 1, {1}},
        {{4,1,-1,2,-1,2,3}, 2, {-1,2}}
    };
    for (auto testcase: testcases){
        auto & [arr, k, expected] = testcase;

        auto result = s.topKFrequent(arr, k);
        auto resultSet = set<int>(result.begin(), result.end());
        assert(resultSet == expected);
    }
}
