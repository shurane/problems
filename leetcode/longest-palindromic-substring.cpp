#include <string>
#include <assert.h>
using namespace std;

class Solution {
public:
    int best_start = 0;
    int best_size = 0;
    void getpal(string& s, int l, int r){
        while (l >= 0 && r < s.length() && s[l] == s[r]){
            l--;
            r++;
        }
        int start = l + 1;
        int size = r - l - 1;
        if (size > best_size){
            best_start = start;
            best_size = size;
        }
    }
    string longestPalindrome(string s) {
        best_start = 0;
        best_size = 0;
        for (int i=0; i<s.length(); i++){
            getpal(s, i, i);
            getpal(s, i, i+1);
        }

        return s.substr(best_start, best_size);
    }
};

int main ()
{
    Solution s;
    assert(s.longestPalindrome("babad") == "bab");
    assert(s.longestPalindrome("cbbd") == "bb");
    assert(s.longestPalindrome("ececabbacec") == "cecabbacec");
    assert(s.longestPalindrome("ececabbacecaaaaaaaaaa") == "cecabbacec");
    assert(s.longestPalindrome("ececabbacecaaaaaaaaaaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaaaaaaaaaa");
    string a = "";
    for (int i=0; i < 1000; i++){
        a += "a";
    }
    assert(s.longestPalindrome(a) == a);
}
