#include "helpers.h"

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
    // TODO ListNode helpers and testcases
    // [1,2,3,4,5,6,7,8,9,10] with values of k between 1-10
}
