#include <vector>
#include <tuple>
#include <algorithm>
#include <assert.h>

//#include <iostream>
//#include "helpers.h"

using namespace std;

class Solution {
public:
    vector<int> minAvailableDuration(vector<vector<int>>& A, vector<vector<int>>& B, int duration) {
        sort(A.begin(), A.end());
        sort(B.begin(), B.end());

        int i = 0;
        int j = 0;

        //cout << "minAvailableDuration()" << endl;
        while (i < A.size() && j < B.size()) {
            //cout << i << " " << j << " " << A[i] << " " << B[j] << endl;
            // A[i] interval is before B[j]
            if (A[i][1] < B[j][0]) {
                i++;
                continue;
            // B[j] interval is before A[i]
            } else if (B[j][1] < A[i][0]) {
                j++;
                continue;
            }

            // intersection
            if (A[i][0] + duration <= A[i][1] && B[j][0] + duration <= B[j][1]) {
                if (A[i][0] <= B[j][0] && B[j][0] + duration <= A[i][1])
                    return {B[j][0], B[j][0] + duration};
                else if (B[j][0] < A[i][0] && A[i][0] + duration <= B[j][1])
                    return {A[i][0], A[i][0] + duration};
            }

            if (A[i][1] < B[j][1]) i++;
            else j++;
        }

        return {};
    }

    // https://leetcode.com/problems/meeting-scheduler/solution/
    vector<int> minAvailableDuration2(vector<vector<int>>& A, vector<vector<int>>& B, int duration) {
        sort(A.begin(), A.end());
        sort(B.begin(), B.end());

        int i = 0;
        int j = 0;

        while (i < A.size() && j < B.size()) {
            int left = max(A[i][0], B[j][0]);
            int right = min(A[i][1], B[j][1]);
            if (right - left >= duration)
                return {left, left + duration};

            if (A[i][1] <= B[j][1]) i++;
            else j++;
        }
        return {};
    }
};

int main()
{
    Solution s;

    vector<tuple<vector<vector<int>>, vector<vector<int>>, int, vector<int>>> testcases = {
        {{{10,50},{60,120},{140,210}}, {{0,15},{60,70}}, 8, {60, 68}},
        {{{10,50},{61,120},{140,210}}, {{0,15},{60,70}}, 8, {61, 69}},
        {{{10,50},{62,120},{140,210}}, {{0,15},{60,70}}, 8, {62, 70}},
        {{{10,50},{63,120},{140,210}}, {{0,15},{60,70}}, 8, {}},
        {{{10,50},{60,120},{140,210}}, {{0,15},{61,70}}, 8, {61, 69}},
        {{{10,50},{60,120},{140,210}}, {{0,15},{62,70}}, 8, {62, 70}},
        {{{10,50},{60,120},{140,210}}, {{0,15},{63,70}}, 8, {}},
        {{{10,50},{60,120},{140,210}}, {{0,15},{60,70}}, 12, {}},
        {{{0,2}}, {{1,3}}, 2, {}},
        {{{10,60}}, {{12,17}, {21, 50}}, 8, {21, 29}},
        {{{10,12}, {15, 25}}, {{0,100}}, 8, {15, 23}},
    };

    for (auto& [A, B, duration, expected]: testcases) {
        assert(s.minAvailableDuration(A, B, duration) == expected);
        assert(s.minAvailableDuration2(A, B, duration) == expected);
    }
}
