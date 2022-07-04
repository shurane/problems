#include <vector>
#include <queue>
#include <utility>
#include <assert.h>

using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        int total = 0;
        vector<int> candies(n, 1);

        for (int i=1; i<n; i++) {
            if (ratings[i] > ratings[i-1] && candies[i] <= candies[i-1])
                candies[i] = candies[i-1] + 1;
        }

        for (int i=n-2; i>=0; i--) {
            if (ratings[i] > ratings[i+1] && candies[i] <= candies[i+1])
                candies[i] = candies[i+1] + 1;
            total += candies[i];
        }
        total += candies[n-1];

        return total;
    }

    int candyWithHeap(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> candies(n, 1);
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> ratingQueue;

        for (int i=0; i<n; i++) {
            ratingQueue.push({ratings[i], i});
        }

        int total = 0;

        while (!ratingQueue.empty()) {
            auto [r, i] = ratingQueue.top();
            ratingQueue.pop();

            if (i-1 >= 0 && ratings[i] > ratings[i-1] && candies[i] <= candies[i-1]) {
                candies[i] = candies[i-1] + 1;
            }

            if (i+1 < n && ratings[i] > ratings[i+1] && candies[i] <= candies[i+1]) {
                candies[i] = candies[i+1] + 1;
            }

            total += candies[i];
        }

        return total;
    }
};

int main()
{
    Solution s;

    vector<pair<vector<int>, int>> testcases = {
        {{1,0,2}, 5},
        {{1,2,2}, 4},
        {{1,2,3,4,5}, 15},
        {{5,4,3,2,1}, 15},
        {{1,2,3,4,5,4,3,2,1}, 25},
        {{5,4,3,2,1,2,3,4,5}, 29},
    };

    for (auto& [testcase, expected]: testcases) {
        assert(s.candy(testcase) == expected);
        assert(s.candyWithHeap(testcase) == expected);
    }
}
