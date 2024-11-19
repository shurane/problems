#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

bool inRange(char c) {
  return ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z') || c == '-' || c == '\'';
}
char toLower(char c) {
  constexpr int upperLowerDiff = 'A' - 'a';
  if ('A' <= c && c <= 'Z')
    return c - upperLowerDiff;
  return c;
}

vector<vector<string>> wordCountEngine(const string & document) {
  unordered_map<string,pair<int, int>> wordCount;
  int l = 0;
  while (l < document.size()) {
    if (!inRange(document[l])) {
      l++;
      continue;
    }

    int r = l;
    while (r < document.size() && inRange(document[r])) {
      r++;
    }
    // const int len = r - l;
    string word;
    for (int i = l; i < r; i++) {
      if (!isalpha(document[i])) {
        continue;
      }
      word.push_back(toLower(document[i]));
    }
    wordCount[word].first++;
    if (wordCount[word].first == 1) {
      wordCount[word].second = l;
    }
    l = r;
  }
  vector<pair<string, pair<int, int>>> wordCountVector(wordCount.begin(), wordCount.end());
  sort(wordCountVector.begin(), wordCountVector.end(), [](const auto & a,
    const auto & b) {
    if (a.second.first != b.second.first) {
      return a.second.first > b.second.first;
    }
    return a.second.second < b.second.second;
  });

  vector<vector<string>> result;
  for (int i = 0; i < wordCountVector.size(); i++) {
    result.push_back({
      wordCountVector[i].first,
      to_string(wordCountVector[i].second.first)
    });
  }
  return result;
}

int main() {
  return 0;
}
