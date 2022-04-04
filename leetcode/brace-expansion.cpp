#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <assert.h>
#include "helpers.h"
using namespace std;

class Solution {
public:
    vector<string> expand(string s) {
        vector<string> results = {""};

        int i=0;
        while (i < s.size()){
            //cout << i << " " << results << endl;
            if (s[i] != '{'){
                for (auto &r: results){
                    r += s[i];
                }

                i++;
            }
            else {
                vector<string> expansions;
                int closeParens = i+1;
                string token = "";
                while (s[closeParens] != '}'){
                    if (s[closeParens] != ','){
                        token += s[closeParens];
                    }
                    else {
                        expansions.push_back(token);
                        token = "";
                    }
                    closeParens++;
                }
                expansions.push_back(token);
                sort(expansions.begin(), expansions.end());

                vector<string> nextResults;
                for (auto r: results){
                    for (auto e: expansions){
                        nextResults.push_back(r+e);
                    }
                }
                results = nextResults;
                i = closeParens+1;
            }
        }
        //cout << i << " " << results << endl;
        return results;
    }
};

int main()
{
    Solution s;

    vector<pair<string, vector<string>>> testcases = {
        {"abcd", {"abcd"}},
        {"{a}{b}{c}{d}", {"abcd"}},
        {"{a,b}c{d,e}f", {"acdf","acef","bcdf","bcef"}},
        {"{b,a}c{e,d}f", {"acdf","acef","bcdf","bcef"}},
    };
    for (auto testcase: testcases){
        //cout << testcase.first << " " << testcase.second << endl;
        assert(s.expand(testcase.first) == testcase.second);
    }
    assert (s.expand("{a,b,c,d}{e,f,g,h},{i,j,k,l}").size() == 64);
    assert (s.expand("{a,b,c,d}{e,f,g,h},{i,j,k,l}{m,n,o,p}").size() == 256);
    assert (s.expand("{a,b,c,d}{e,f,g,h},{i,j,k,l}{m,n,o,p}{q,r,s,t}").size() == 1024);
    assert (s.expand("{a,b,c,d}{e,f,g,h},{i,j,k,l}{m,n,o,p}{q,r,s,t}{u,v,x,y}").size() == 4096);
}
