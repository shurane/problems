#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
#include "helpers.h"

using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](auto const& a, auto const& b) -> bool {
            if (a[0] != b[0])
                return a[0] < b[0];
            return a[1] > b[1];
        });

        // cout << "sorted: " << points << endl;

        int arrows = 0;
        int i = 0;
        while(i<points.size()-1) {
            arrows++;
            // no overlap
            if (points[i][1] < points[i+1][0]) {
                // cout << "no overlap " << points[i][0] << " " << points[i][1] << ", "
                //                       << points[i+1][0] << " " << points[i+1][1] << endl;
                i++;
            // overlap
            } else {
                // cout << "collapsing following points: ";
                // cout << points[i][0] << " " << points[i][1] << ", ";
                // cout << points[i+1][0] << " " << points[i+1][1] << ", ";
                int j = i + 2;
                int lo = points[i+1][0];
                int hi = min(points[i][1], points[i+1][1]);
                while (lo <= hi
                        && j < points.size()
                        && points[j][0] <= hi
                        && points[j][1] >= lo) {
                    lo = max(lo, points[j][0]);
                    hi = min(hi,points[j][1]);
                    // cout << points[j][0] << " " << points[j][1] << ", ";
                    j++;
                }
                // cout << "- " << (j - i) << " points by 1 arrow, lo:" << lo
                //      << ", hi:" << hi << endl;

                i = j;
            }
        }
        if (i < points.size()) {
            // cout << "balloon left at the end" << endl;
            arrows++;
        }
        return arrows;
    }
};

int main()
{
    Solution s;

    vector<pair<vector<vector<int>>, int>> testcases = {
        {{{10,16},{2,8},{1,6},{7,12}}, 2},
        {{{1,2},{3,4},{5,6},{7,8}}, 4},
        {{{1,2},{2,3},{3,4},{4,5}}, 2},
        {{{1,2},{4,5},{1,5}}, 2},
        {{{9,12},{1,10},{4,11},{8,12},{3,9},{6,9},{6,7}}, 2},
    };

    for (auto & [testcase, expected]: testcases) {
        // cout << "checking for testcase: " << testcase << endl;
        assert(s.findMinArrowShots(testcase) == expected);
        cout << endl;
    }

}
