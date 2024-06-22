#include <vector>
#include <utility>
#include <assert.h>
using namespace std;

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        vector<vector<int>> next = board;
        int m = board.size();
        int n = board[0].size();

        vector<pair<int, int>> dirs = {{-1,-1},{ 0,-1},{ 1,-1},
                                       {-1, 0},        { 1, 0},
                                       {-1, 1},{ 0, 1},{ 1, 1}};

        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                int neighbors = 0;
                for (auto [r,c]: dirs){
                    int nexti = i+r;
                    int nextj = j+c;
                    if (0 <= nexti && nexti < m && 0 <= nextj && nextj < n){
                        neighbors += board[nexti][nextj];
                    }
                }
                if (board[i][j] == 1 && neighbors < 2){
                    next[i][j] = 0;
                } else if (board[i][j] == 1 && neighbors < 4){
                    next[i][j] = 1;
                } else if (board[i][j] == 1 && neighbors >= 4){
                    next[i][j] = 0;
                } else if (board[i][j] == 0 && neighbors == 3){
                    next[i][j] = 1;
                }
            }
        }

        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                board[i][j] = next[i][j];
            }
        }
    }
};

int main()
{
    Solution s;
    //initializer_list<pair<initializer_list<initializer_list<int>>, initializer_list<initializer_list<int>>>> testcases = {
    vector<pair<vector<vector<int>>,vector<vector<int>>>> testcases = {
        {{{0,1,0},{0,0,1},{1,1,1},{0,0,0}}, {{0,0,0},{1,0,1},{0,1,1},{0,1,0}}},
        {{{1,1},{1,0}}, {{1,1},{1,1}}}
    };

    for (auto & [board, next] : testcases) {
        s.gameOfLife(board);
        assert(board == next);
    }

}
