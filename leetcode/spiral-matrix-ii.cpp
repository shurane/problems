#include <vector>
#include <assert.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> m(n, vector<int>(n));
        int count = 1;

        for (int layer=0; layer<n/2; layer++){
            // top
            for (int i=layer; i<n-1-layer; i++){
                m[layer][i] = count++;
            }
            // right
            for (int j=layer; j<n-1-layer; j++){
                m[j][n-1-layer] = count++;
            }
            // bottom
            for (int i=n-1-layer; i>layer; i--){
                m[n-1-layer][i] = count++;
            }
            // left
            for (int j=n-1-layer; j>layer; j--){
                m[j][layer] = count++;
            }
        }
        if (n % 2 == 1){
            m[n/2][n/2] = count;
        }

        return m;
    }
};

int main()
{
    Solution s;

    vector<vector<vector<int>>> testcases = {
        {{}},
        {{1}},
        {{ 1, 2},
         { 4, 3}},
        {{ 1, 2, 3},
         { 8, 9, 4},
         { 7, 6, 5}},
        {{ 1, 2, 3, 4},
         {12,13,14, 5},
         {11,16,15, 6},
         {10, 9, 8, 7}},
        {{ 1, 2, 3, 4, 5},
         {16,17,18,19, 6},
         {15,24,25,20, 7},
         {14,23,22,21, 8},
         {13,12,11,10, 9}},
        {{ 1, 2, 3, 4, 5, 6},
         {20,21,22,23,24, 7},
         {19,32,33,34,25, 8},
         {18,31,36,35,26, 9},
         {17,30,29,28,27,10},
         {16,15,14,13,12,11}},
        {{ 1, 2, 3, 4, 5, 6, 7},
         {24,25,26,27,28,29, 8},
         {23,40,41,42,43,30, 9},
         {22,39,48,49,44,31,10},
         {21,38,47,46,45,32,11},
         {20,37,36,35,34,33,12},
         {19,18,17,16,15,14,13}},
    };

    for (int i=1;i<testcases.size(); i++){
        assert(s.generateMatrix(i) == testcases[i]);
    }

}
