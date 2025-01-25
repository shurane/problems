#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <utility>
#include <tuple>

#include <assert.h>

using namespace std;

class UnionFind {
public:
    vector<int> root;
    vector<int> rank;
    UnionFind(int k) {
        root.resize(k);
        rank.resize(k);
        for (int i=0; i<k; i++) {
            root[i] = i;
            rank[i] = 1;
        }
    }

    int find_(int i) {
        if (i == root[i])
            return i;
        return root[i] = find_(root[i]);
    }

    void union_(int i, int j) {
        int u = find_(i);
        int v = find_(j);

        if (rank[u] > rank[v]) {
            root[v] = u;
            rank[u] += rank[v];
        } else {
            root[u] = v;
            rank[v] += rank[u];
        }
    }
};

bool areSentencesSimilar(const vector<string>& sentence1, const vector<string>& sentence2,
                         const vector<pair<string, string>>& similarPairs) {

    if (sentence1.size() != sentence2.size()) {
        return false;
    }

    unordered_map<string, int> words;
    int pos = 0;

    for (int i=0; i<similarPairs.size(); i++) {
        const string& w1 = similarPairs[i].first;
        const string& w2 = similarPairs[i].second;
        if (words.find(w1) == words.end()) {
            words[w1] = pos++;
        }
        if (words.find(w2) == words.end()) {
            words[w2] = pos++;
        }
    }

    for (const string& w: sentence1) {
        if (words.find(w) == words.end()) {
            words[w] = pos++;
        }
    }

    for (const string& w: sentence2) {
        if (words.find(w) == words.end()) {
            words[w] = pos++;
        }
    }

    // setup union-find data structure
    const int n = sentence1.size();
    const int k = words.size();
    UnionFind uf(k);

    for (int i=0; i<similarPairs.size(); i++) {
        const string& w1 = similarPairs[i].first;
        const string& w2 = similarPairs[i].second;
        uf.union_(words[w1], words[w2]);
    }

    for (int i=0; i<n; i++) {
        int w1pos = words[sentence1[i]];
        int w2pos = words[sentence2[i]];
        // cout << "i: " << i << " " << w1pos << " " << w2pos << " " << uf.find_(w1pos) << " " << uf.find_(w2pos) << endl;

        if (uf.find_(w1pos) != uf.find_(w2pos)) {
            return false;
        }
    }

    return true;
}

int main() {
    // debug your code below
    vector<tuple<vector<string>, vector<string>, vector<pair<string, string>>, bool>> testcases = {
        {{"Let's", "code", "in", "Python"}, {"Let's", "program", "in", "Python"}, {{"code", "program"}}, true},
        {{"i", "love", "coding"}, {"i", "love", "coding"}, {}, true},
        {{"i", "love", "coding"}, {"i", "really", "love", "coding"}, {}, false},
        {{"i", "love", "coding"}, {"i", "adore", "coding"}, {{"love", "adore"}}, true},
        {{"i", "enjoy", "coding", "very", "much"},
         {"i", "love", "programming", "so", "much"},
         {{"enjoy", "love"}, {"coding", "programming"}, {"very", "so"}},
         true},
        // missing similarity of {"coding", "programming"}
        {{"i", "enjoy", "coding", "very", "much"},
         {"i", "love", "programming", "so", "much"},
         {{"enjoy", "love"}, {"very", "so"}},
         false},
        {{"i", "enjoy", "coding", "very", "much"},
         {"i", "love", "programming", "so", "much"},
         {{"enjoy", "love"}, {"very", "so"}, {"coding", "programming"}},
         true},
    };

    for (auto& [s1, s2, similarPairs, expected]: testcases) {
        assert(areSentencesSimilar(s1, s2, similarPairs) == expected);
    }

    return 0;
}
