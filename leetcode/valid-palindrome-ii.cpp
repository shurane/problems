#include <string>
#include <assert.h>
using namespace std;

class Solution {
public:
    bool validPalindrome(string s) {
        return valid(s, 0, s.length() - 1, 1);
    }

    bool valid(string s, int l, int r, int skip) {
        while (l < r && s[l] == s[r]){
            l++;
            r--;
        }

        if (l >= r) return true;
        else {
            if (skip != 0){
                return valid(s, l + 1, r, skip - 1) || valid(s, l, r - 1, skip - 1);
            }
            else {
                return false;
            }
        }
    }
};

int main()
{
    Solution s;
    assert(s.validPalindrome("aba") == true);
    assert(s.validPalindrome("abca") == true);
    assert(s.validPalindrome("abc") == false);
    assert(s.validPalindrome("ececabbacec") == true);

    string a = "";
    for (int i=0; i < 100000; i++){
        a += "a";
    }
    assert(s.validPalindrome(a) == true);
    a[10] = 'b';
    assert(s.validPalindrome(a) == true);
    a[11] = 'b';
    assert(s.validPalindrome(a) == false);
}
