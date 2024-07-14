#include <algorithm>
#include <string>
#include <tuple>
#include <vector>
#include <assert.h>

using namespace std;

struct Robot {
    int number;
    int position;
    int health;
    char direction;
};

class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        int n = positions.size();
        vector<Robot> robots;

        for (int i=0; i<n; i++) {
            robots.push_back({i+1, positions[i], healths[i], directions[i]});
        }

        sort(robots.begin(), robots.end(), [](const Robot& a, const Robot& b) {
            return a.position < b.position;
        });

        vector<int> result;
        for (int i=0; i<n; i++) {
            // Robot& r = robots[i];
            // cout << "num: " << r.number << ", pos: " << r.position << ", health: " << r.health << ", direction: " << r.direction << endl;
            if (result.empty() ||
                robots[i].direction == 'R' ||
                robots[result.back()].direction == 'L') {
                result.push_back(i);
            } else {
                Robot& leftie = robots[i];
                while (!result.empty() && robots[result.back()].direction == 'R' && leftie.health > 0) {
                    Robot& top = robots[result.back()];
                    // cout << "found robot moving right, fight: " << top.health << ", " << leftie.health << endl;
                    // destroy leftie
                    if (top.health > leftie.health) {
                        top.health--;
                        leftie.health = 0;
                    // knock robots off the top
                    } else if (leftie.health > top.health) {
                        top.health = 0;
                        leftie.health--;
                        result.pop_back();
                    // same health, destroy both
                    } else {
                        top.health = 0;
                        leftie.health = 0;
                        result.pop_back();
                    }
                }

                if (leftie.health > 0) result.push_back(i);
            }
        }

        sort(result.begin(), result.end(), [&](const int a, const int b) {
            return robots[a].number < robots[b].number;
        });

        for (int i=0; i<result.size(); i++) {
            Robot& r = robots[result[i]];
            // cout << "num: " << r.number << ", pos: " << r.position << ", health: " << r.health << ", direction: " << r.direction << endl;
            result[i] = r.health;
        }

        return result;
    }
};

int main()
{
    Solution s;
    vector<tuple<vector<int>, vector<int>, string, vector<int>>> testcases = {
        {{5,4,3,2,1}, {2,17,9,15,10}, "RRRRR", {2, 17, 9, 15, 10}},
        {{3,5,2,6}, {10,10,15,12}, "RLRL", {14}},
        {{1,2,5,6}, {10,10,11,11}, "RLRL", {}},
        {{3,40}, {49,11}, "LL", {49, 11}},
        {{11,44,16}, {1, 20, 17}, "RLR", {18}},
    };

    for (auto & [positions, healths, directions, expected]: testcases) {
        assert(s.survivedRobotsHealths(positions, healths, directions) == expected);
    }

}
