#include <vector>
#include <queue>
#include <utility>
#include <tuple>
#include <assert.h>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int n = cardPoints.size();
        int bestSum = 0;
        int sum = 0;

        // use a sliding window, and decrement head of the sliding window once count >= k
        for (int count=0; count != 2*k; count++) {
            int i = (n - k + count) % n;
            sum += cardPoints[i];

            if (count >= k){
                int head = n + (i - k);
                sum -= cardPoints[head];
            }

            // if (count >= k - 1)
            bestSum = max(bestSum, sum);
            // cout << "count: " << count << ", i: " << i << ", cardPoints[i]: " << cardPoints[i] <<  ", sum: " << sum << endl;
        }
        return bestSum;
    }

    int maxScore2(vector<int>& cardPoints, int k) {
        int n = cardPoints.size();
        int r = n - k;
        int total = 0;
        int bestSum = 0;
        for (int num: cardPoints)
            total += num;

        // subtract up to r
        for (int i=0; i<r; i++) {
            total -= cardPoints[i];
        }

        // add from 0 to k, removing from r as well
        for (int i=0; i<k; i++) {
            //cout << "i: " << i << ", cardPoints[i]: " << cardPoints[i] << ", cardPoints[r]: " << cardPoints[r] << ", total: " << total << endl;
            bestSum = max(bestSum, total);
            total += cardPoints[i];
            total -= cardPoints[r];
            r++;
        }
        bestSum = max(bestSum, total);

        return bestSum;
    }

    int maxScore3(vector<int>& cardPoints, int k) {
        int n = cardPoints.size();
        int r = n - k;
        int total = 0;
        int bestSum = 0;

        // add from r to n
        for (int i=r; i<n; i++) {
            total += cardPoints[i];
        }
        bestSum = max(bestSum, total);

        // add from 0 to k, removing from r as well
        for (int i=0; i<k; i++) {
            //cout << "i: " << i << ", cardPoints[i]: " << cardPoints[i] << ", cardPoints[r]: " << cardPoints[r] << ", total: " << total << endl;
            total += cardPoints[i] - cardPoints[r];
            r++;
            bestSum = max(bestSum, total);
        }

        return bestSum;
    }

};

int main()
{
    Solution s;
    vector<tuple<vector<int>, int, int>> testcases = {
        {{1,2,3,4,5,6,1}, 3, 12},
        {{1,2,3,4,5}, 4, 14},
        {{5,4,3,2,1}, 4, 14},
        {{2,2,2}, 2, 4},
        {{9,7,7,9,7,7,9}, 7, 55},
        {{2,2,2,1000,1,1}, 3, 1002},
        {{1,1,1000,2,2,2}, 3, 1002},
    };

    for (auto& [testcase, k, expected]: testcases) {
        assert(s.maxScore(testcase, k) == expected);
        assert(s.maxScore2(testcase, k) == expected);
        assert(s.maxScore3(testcase, k) == expected);
    }

}
