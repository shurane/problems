#include <vector>
#include <sstream>
#include <assert.h>
#include "helpers.h"

int main()
{
    int values1[] = {0,1,2,3,4,5,6,7,8,9};
    int values2[] = {0,1,2,3,4,5,6,7,8,9,10};
    std::vector<int> values3 = {10,11,12,13,14,15,16,17,18,19};
    std::stringstream ss;

    ss.str("");
    ss << values3;
    assert(ss.str() == "{10, 11, 12, 13, 14, 15, 16, 17, 18, 19}");

    ListNode* lst1 = toList(values1);
    ListNode* lst1copy = toList(values1);
    ListNode* lst2 = toList(values2);
    ListNode* lst3 = toList(values3);
    ListNode* lst3copy = toList(values3);

    ss.str("");
    ss << lst1;
    assert(ss.str() == "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}");

    ss.str("");
    ss << lst2;
    assert(ss.str() == "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}");

    assert(*lst1 == *lst1copy);
    assert(*lst1 != *lst2);
    assert(*lst2 != *lst1);
    assert(*lst1 != *lst3);
    assert(*lst3 == *lst3copy);
}
