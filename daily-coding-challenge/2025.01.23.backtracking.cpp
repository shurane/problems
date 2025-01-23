#include <iostream>
#include <iomanip>
#include <vector>
#include <utility>
#include <climits>
#include "../leetcode/helpers.h"

using namespace std;

struct TreeNode {
    int val;
    vector<TreeNode*> children;

    TreeNode() : val(0) {}
    TreeNode(int x) : val(x) {}
    // TODO whack way, fix with smart pointers
    ~TreeNode() {
        for (TreeNode* child: children) {
            delete child;
        }
    }
};

int recurse(TreeNode* node) {
    if (node->children.size() == 0) {
        return node->val;
    }

    int minCost = INT_MAX;

    for (TreeNode* child: node->children) {
        int tempCost = recurse(child);
        if (tempCost < minCost) {
            minCost = tempCost;
        }
    }
    return node->val + minCost;
}

void backtrackHelper(TreeNode* node, int& cost, int& globalMinCost, vector<int>& path, vector<int>& globalMinPath) {
    cost += node->val;
    path.push_back(node->val);
    cout << "visiting: " << node->val << ", cost: " << cost << endl;

    if (node->children.size() == 0) {
        cout << "path to leaf: " << path << endl;
        cout << "leaf node, accumulated cost: " << cost << ", less than globalMinCost? " << boolalpha << (cost < globalMinCost) << endl;

        if (cost < globalMinCost) {
            globalMinCost = cost;
            globalMinPath = path;
        }
    }

    for (TreeNode* child: node->children) {
        backtrackHelper(child, cost, globalMinCost, path, globalMinPath);
    }

    cost -= node->val;
    path.pop_back();
}

pair<int, vector<int>> backtrack(TreeNode* node) {
    int cost = 0;
    int globalMinCost = INT_MAX;
    vector<int> path;
    vector<int> globalMinPath;
    backtrackHelper(node, cost, globalMinCost, path, globalMinPath);

    return {globalMinCost, globalMinPath};
}

int main() {

    TreeNode* root = new TreeNode(0);
    root->children.push_back(new TreeNode(5));
    root->children.push_back(new TreeNode(3));
    root->children.push_back(new TreeNode(6));
    root->children[0]->children.push_back(new TreeNode(4));
    root->children[1]->children.push_back(new TreeNode(2));
    root->children[1]->children[0]->children.push_back(new TreeNode(1));
    root->children[1]->children[0]->children[0]->children.push_back(new TreeNode(1));
    root->children[1]->children.push_back(new TreeNode(0));
    root->children[1]->children[1]->children.push_back(new TreeNode(10));
    root->children[2]->children.push_back(new TreeNode(1));
    root->children[2]->children.push_back(new TreeNode(5));

    auto [minPathSum, minPath] = backtrack(root);
    cout << "minPathSum: " << minPathSum << ", minPath: " << minPath << endl;
    delete root;
    return 0;
}

// practice with Bhanu on https://abhinaygupta1998.medium.com/sales-path-d1a9f0144cc7