#include <vector>
#include <queue>
#include <assert.h>
using namespace std;

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> q;
        for (auto stone: stones){
            q.push(stone);
        }
        while (q.size() > 1){
            int first = q.top(); q.pop();
            int second = q.top(); q.pop();
            if (first - second > 0){
                q.push(first - second);
            }
        }
        if (q.size() == 1){
            return q.top();
        }
        else {
            return 0;
        }
    }
};

int main()
{
    Solution s;

    vector<pair<vector<int>, int>> testcases = {
        {{2,7,4,1,8,1}, 1},
        {{1}, 1},
        {{20,10}, 10},
        {{20,20}, 0},
        {{20,20,20}, 20},
    };

    for (auto testcase: testcases) {
        auto & [arr, expected] = testcase;
        assert(s.lastStoneWeight(arr) == expected);
    }
}
