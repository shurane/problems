#include <iostream>
#include <vector>
#include <utility>

// https://stackoverflow.com/a/23397700/198348
template<typename T>
std::ostream& operator<< (std::ostream& out, const std::vector<T>& v)
{
    out << "{";
    size_t last = v.size() - 1;
    for(size_t i = 0; i < v.size(); ++i) {
        out << v[i];
        if (i != last)
            out << ", ";
    }
    out << "}";
    return out;
}

// https://stackoverflow.com/a/16956609/198348
template<typename T, typename U>
std::ostream& operator<<(std::ostream& o, const std::pair<T,U>& p)
{
  return o << "{" << p.first << ", " << p.second << "}";
}

// TODO ListNode helpers, see helpers2.py for reference
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
    ~ListNode(){ if (next) delete next; }
};

// TODO TreeNode helpers

static std::ostream& operator<< (std::ostream& out, const ListNode *l)
{
    out << "{";
    while (l != nullptr){
        out << l->val;
        if (l->next != nullptr)
            out << ", ";
        l = l->next;
    }
    out << "}";
    return out;
}

// converting from a reference to a pointer to do comparisons doesn't seem ideal
// is there a better approach considering that the Leetcode ListNode definition is not modifiable?
static bool operator==(ListNode &lhs, ListNode &rhs)
{
    const ListNode *l = &lhs;
    const ListNode *r = &rhs;
    while (l != nullptr and r != nullptr){
        if (lhs.val != rhs.val)
            return false;
        l = l->next;
        r = r->next;
    }
    return l == r;
}
static bool operator!=(ListNode &lhs, ListNode &rhs) { return !(lhs == rhs); }

// is this a situation to use unique_ptr?
// should I investigate constraints and concepts... https://en.cppreference.com/w/cpp/language/constraints
// or using iterator traits: https://stackoverflow.com/questions/20244743/pass-iterator-as-a-function-parameter
// https://stackoverflow.com/questions/53252321/how-to-write-a-function-that-can-take-in-an-array-or-a-vector
template<class Iterable>
ListNode* toList(Iterable a, Iterable b)
{
    ListNode dummy = ListNode();
    ListNode *curr = &dummy;
    while (a != b){
        curr->next = new ListNode(*a);
        curr = curr->next;
        a++;
    }
    curr = dummy.next;
    dummy.next = nullptr;
    return curr;
}

template<class T>
ListNode* toList(const T& container)
{
    return toList(std::begin(container), std::end(container));
}
