#include <vector>
#include <string>
#include <assert.h>
using namespace std;

class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> scores;
        for (auto op: ops){
            if (op == "+"){
                int s1 = scores[scores.size()-1];
                int s2 = scores[scores.size()-2];
                scores.push_back(s1 + s2);
            } else if (op == "D"){
                int s1 = scores[scores.size()-1];
                scores.push_back(s1*2);
            } else if (op == "C"){
                scores.pop_back();
            } else {
                scores.push_back(stoi(op));
            }
        }

        // return accumulate(scores.begin(), scores.end(), 0);
        int sum = 0;
        for (auto score: scores)
            sum += score;
        return sum;
    }
};

int main()
{
    Solution s;

    vector<pair<vector<string>, int>> testcases = {
        {{"5","2","C","D","+"}, 30},
        {{"5","-2","4","C","D","9","+","+"}, 27},
        {{"1"}, 1},
        {{"2","2","+","+","+","+"}, 2+2+4+6+10+16},
        {{"2","D","D","D","D"}, 2+4+8+16+32},
        {{"2","D","D","D","D","C","C","C","C"}, 2},
    };

    for (auto testcase: testcases) {
        auto & [ops, expected] = testcase;
        assert(s.calPoints(ops) == expected);
    }
}
