#include <iostream>
#include <vector>

using namespace std;

bool isLetter(char c) {
    return ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z');
}

void backtrack(const string& s, string& intermediate, vector<string>& result, int i) {
    cout << "backtrack: " << i << ", intermediate: " << intermediate << endl;
    if (i == s.size()) {
        result.push_back(intermediate);
        return;
    }

    if (isLetter(s[i])) {
        intermediate.push_back(s[i]);
        backtrack(s, intermediate, result, i+1);
        intermediate.pop_back();
    } else {
        // found '{'
        int j=i;
        vector<char> choices;
        while (j < s.size() && s[j] != '}') {
            if (isLetter(s[j])) {
                choices.push_back(s[j]);
            }
            j++;
        }
        for (char c: choices) {
            intermediate.push_back(c);
            backtrack(s, intermediate, result, j+1);
            intermediate.pop_back();
        }
    }
}

vector<string> expandTag(const string s) {
    string intermediate; // ""
    vector<string> result;
    backtrack(s, intermediate, result, 0);

    return result;
}

int main() {
    vector<string> result = expandTag("ABCD{E,F,G}HIJK{L,M,N}");
    for (int i=0; i<result.size(); i++) {
        cout << i << " " << result[i] << endl;
    }
    return 0;
}

// practice with Bhanu on a backtracking problem
// "FED{E,F,G}" -> [FEDE, FEDF, FEDG]
