#include <vector>
#include <assert.h>

using namespace std;

class Solution {
public:

/*
        1   2   3   4   5   6
    a   1   1   1   1   1   1
    e   1   2   3   4   5   6
    i   1   3   6  10  15  21
    o   1   4  10  20  35  56
    u   1   5  15  35  70 126
total   5  15  35  70 126 210
 */

    int countVowelStrings(int n) {
        vector<vector<int>> dp(n, vector<int>(5, 0));

        for (int j=0; j<5; j++){
            dp[0][j] = 1;
        }

        int prev;
        for (int i=1; i<n; i++){
            prev = 0;
            for (int j=0; j<5; j++){
                prev += dp[i-1][j];
                dp[i][j] = prev;
            }
        }

        prev = 0;
        for (int j=0; j<5; j++){
            // char c = 'a' + j;
            // cout << c << " " << dp[n-1][j] << endl;
            prev += dp[n-1][j];
        }

        return prev;
    }

    int countVowelStringsAlternate(int n) {
        vector<vector<int>> dp(n, vector<int>(5, 1));

        for (int i=1; i<n; i++){
            for (int j=1; j<5; j++){
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }

        int prev = 0;
        for (int j=0; j<5; j++){
            // char c = 'a' + j;
            // cout << c << " " << dp[n-1][j] << endl;
            prev += dp[n-1][j];
        }

        return prev;
    }

    int countVowelStringsConstantSpace(int n) {
        vector<int> dp(5, 1);

        int prev;
        for (int i=1; i<n+1; i++){
            prev = 0;
            for (int j=0; j<5; j++){
                prev += dp[j];
                dp[j] = prev;
            }
        }

        return prev;
    }
};

int main()
{
    vector<pair<int, int>> testcases = {
        {1, 5},
        {2, 15},
        {3, 35},
        {4, 70},
        {5, 126},
        {6, 210},
        {7, 330},
        {8, 495},
        {9, 715},
        {10, 1001},
        {33, 66045},
        {50, 316251},
    };

    Solution s;

    for (auto [n, expected]: testcases) {
        assert(s.countVowelStrings(n) == expected);
        assert(s.countVowelStringsAlternate(n) == expected);
        assert(s.countVowelStringsConstantSpace(n) == expected);
    }
}