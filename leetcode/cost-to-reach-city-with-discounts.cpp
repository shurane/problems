#include <vector>
#include <queue>
#include <tuple>
#include <iostream>
#include <functional>
#include <climits>
#include <assert.h>

using namespace std;

class Solution {
public:
    int minimumCost(int n, vector<vector<int>>& highways, int discounts) {
        vector<vector<pair<int, int>>> graph(n);
        int rate = 1;

        if (discounts >= n-1) {
            discounts = 0;
            rate = 2;
        }

        for (const auto& h: highways) {
            const int cityA = h[0];
            const int cityB = h[1];
            const int toll = h[2] / rate;
            graph[cityA].push_back({cityB, toll});
            graph[cityB].push_back({cityA, toll});
        }

        vector<vector<int>> citiesMinCosts(n, vector<int>(discounts+1, INT_MAX));
        for (int j=0; j<=discounts; j++) {
            citiesMinCosts[0][j] = 0;
        }

        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> toVisit;
        toVisit.push({0, 0, discounts});

         while (!toVisit.empty()) {
             auto [cost, city, discountLeft] = toVisit.top(); toVisit.pop();
             //cout << "visiting: " << city << ", cost: " << cost << ", discountLeft: " << discountLeft << endl;

             for (auto [next, toll]: graph[city]) {
                 const int newCost = cost + toll;
                 const int newCostDiscount = cost + toll / 2;

                 if (newCost < citiesMinCosts[next][discountLeft]) {
                     //cout << "no discount, found shorter distance from " << city << " to " << next << ": " << newCost << " < " << citiesMinCosts[next][discountLeft] << endl;
                     citiesMinCosts[next][discountLeft] = newCost;
                     toVisit.push({newCost, next, discountLeft});
                 }
                 if (discountLeft > 0 && newCostDiscount < citiesMinCosts[next][discountLeft-1]) {
                     //cout << "   discount, found shorter distance from " << city << " to " << next << ": " << newCostDiscount << " < " << citiesMinCosts[next][discountLeft-1] << endl;
                     citiesMinCosts[next][discountLeft - 1] = newCostDiscount;
                     toVisit.push({newCostDiscount, next, discountLeft - 1});
                 }
             }
         }
         //cout << "value in citiesMinCosts[n-1][0]: " << citiesMinCosts[n-1][0] << endl;
         if (citiesMinCosts[n-1][0] == INT_MAX) return -1;

        return citiesMinCosts[n-1][0];

        return 0;
    }
};

int main()
{
    Solution s;

    vector<tuple<int, vector<vector<int>>, int, int>> testcases = {
        {5, {{0,1,4}, {2,1,3}, {1,4,11}, {3,2,3}, {3,4,2}}, 1, 9},
        {4, {{1,3,17}, {1,2,7}, {3,2,5}, {0,1,6}, {3,0,20}}, 20, 8},
        {4, {{0,1,3}, {2,3,2}}, 0, -1},
        {5, {{0,2,2},{2,1,4},{2,3,3},{3,1,4},{2,4,5},{3,0,5}}, 4, 3},
    };

    for (auto& [n, highways, discounts, expected]: testcases) {
        assert(s.minimumCost(n, highways, discounts) == expected);
    }

}

