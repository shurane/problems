#include <tuple>
#include <vector>
#include <map>
#include <unordered_map>
#include <assert.h>
#include "helpers.h"
using namespace std;

// https://stackoverflow.com/a/15302448/198348
long choose(long n, long k){
    if (k == 0) return 1;
    return (n * choose(n - 1, k - 1)) / k;
}

class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        map<int, int> m;
        int i, j, k;
        int mod = 1e9+7;
        long res = 0;
        for (auto value: arr){ m[value]++; }

        for (auto it = m.begin(); it != m.end(); it++){
            i = it->first;

            // unique i, j, k
            auto jt = it;
            jt++;
            for (;jt != m.end(); jt++){
                j = jt->first;
                k = target - i - j;
                if (i < j && j < k && m.find(k) != m.end()){
                    long times = m[i] * m[j] * m[k];
                    //cout << "match " << i << " " << j << " " << k << " times: " << times << endl;
                    res += times;
                }
            }

            // i shows up twice, j once
            j = target - (i * 2);
            if(i != j && m[i] > 1 && m.find(j) != m.end()){
                long times =  choose(m[i], 2) * m[j];
                //cout << "match " << i << " " << i << " " << j << " times: " << times << endl;
                res += times;
            }
        }

        // i shows up 3 times
        if (target % 3 == 0 && m[target/3] > 2){
            long times = choose(m[target/3], 3);
            //cout << "match " << target/3 << " " << target/3 << " " << target/3 << " times: " << times << endl;
            res += times;
        }
        return res % mod;
    }
    // https://leetcode.com/problems/3sum-with-multiplicity/discuss/1918457/C%2B%2B-Simplest-Solution-or-W-Easy-Explanation-or-Intuitive
    int threeSumMulti2(vector<int>& arr, int target) {
        int n = arr.size();
        int mod = 1e9+7;
        int ans = 0;
        unordered_map<int, int> m;

        for (int i=0; i<n; i++){
            ans = (ans + m[target - arr[i]]) % mod;

            for (int j=0; j<i; j++){
                m[arr[i] + arr[j]]++;
            }
        }
        return ans % mod;
    }
    // https://leetcode.com/problems/3sum-with-multiplicity/discuss/181131/C%2B%2BJavaPython-O(N-%2B-101-*-101)
    // It's O(101 * 101) because there are only 101 possible values in arr, from [0, 100]
    // similar to my solution, but doesn't worry about iterators or using a 'triangular' loop instead of a 'square' loop
    int threeSumMulti3(vector<int>& arr, int target) {
        unordered_map<int, long> c;
        for (int i: arr)
            c[i]++;

        long res = 0;
        for (auto it: c){
            for (auto it2: c){
                int i = it.first;
                int j = it2.first;
                int k = target - i - j;
                if (!c.count(k)) continue;
                if (i == j && j == k)
                    res += c[i] * (c[i] - 1) * (c[i] - 2) / 6; // n choose 3?
                else if (i == j && j != k)
                    res += c[i] * (c[i] - 1) / 2 * c[k];
                else if (i < j && j < k)
                    res += c[i] * c[j] * c[k];
            }
        }
        return res % int(1e9+7);
    }
};

int main()
{
    Solution s;

    vector<tuple<vector<int>, int, int>> testcases = {
        {{1,1,2,2,3,3,4,4,5,5}, 8, 20},
        {{1,1,2,2,2,2}, 5, 12},
        {{2,2,2}, 6, 1},
        {{2,2,2,2}, 6, 4},
        {{2,2,2,2,2}, 6, 10},
        {{2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2}, 6, 14190},
        {{}, 0, 495500972},
    };
    for (int i=0; i<3000; i++){ get<0>(testcases[testcases.size()-1]).push_back(0); }

    for (auto testcase: testcases){
        auto & [arr, target, expected] = testcase;

        assert(s.threeSumMulti(arr, target) == expected);
        assert(s.threeSumMulti2(arr, target) == expected);
        assert(s.threeSumMulti3(arr, target) == expected);
    }
}
