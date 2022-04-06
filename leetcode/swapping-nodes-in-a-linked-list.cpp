#include "helpers.h"
#include <vector>
#include <assert.h>
using namespace std;

class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        int i = 1;
        ListNode* left = nullptr;
        ListNode* right  = nullptr;
        ListNode* curr = head;
        while (curr) {
            if (i == k){
                left = curr;
            }
            curr = curr->next;
            i++;
        }
        int n = i;

        i = 1;
        curr = head;
        while (curr) {
            if (i == n - k){
                right = curr;
                break;
            }
            curr = curr->next;
            i++;
        }

        int temp = left->val;
        left->val = right->val;
        right->val = temp;

        return head;
    }
};

int main()
{
    Solution s;
    int n = 100;
    vector<int> values;
    for (int i=0; i<n; i++){ values.push_back(i);}

    for (int i=1; i <= n; i++){
        vector<int> expected = values;
        swap(expected[i-1], expected[n-i]);
        ListNode *l1 = toList(values);
        ListNode *l2 = toList(expected);
        s.swapNodes(l1, i);
        assert(*l1 == *l2);
        deleteList(l1);
        deleteList(l2);
    }
}
