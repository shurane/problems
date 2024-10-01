#include <unordered_set>
#include <unordered_map>
#include <iostream>
#include <string>

#include <assert.h>

using namespace std;

class MyListNode {
public:
    // probably don't need both size and count variables
    MyListNode* prev = nullptr;
    MyListNode* next = nullptr;
    MyListNode* prevWithValue = nullptr;
    MyListNode* nextWithValue = nullptr;
    unordered_set<string> container;
    int count;
    MyListNode(int count): count(count) {}
};

class AllOne {
public:
    MyListNode* front = nullptr;
    MyListNode* minKeyLocation = nullptr;
    MyListNode* back = nullptr;
    unordered_map<string, MyListNode*> mapping;
    int size = 0;
    // AllOne() {}
    ~AllOne() {
        MyListNode* curr = front;
        while (curr) {
            MyListNode* temp = curr;
            curr = curr->next;
            delete temp;
        }
    }

    void getState() {
        MyListNode* curr = front;
        while (curr) {
            cout << "Node(" << curr->count << ")";
            if (curr == minKeyLocation)
                cout << "(min)";
            else if (curr == back)
                cout << "(max)";
            cout << ": ";
            for (const string& s: curr->container) {
                cout << s << ", ";
            }
            cout << endl;
            curr = curr->next;
        }
    }

    void incFront(const string& key) {
        if (!front) {
            front = new MyListNode(1);
        }
        front->container.insert(key);
        mapping[key] = front;

        if (size == 0) {
            back = front;
            size++;
        }

        if (minKeyLocation != front) {
            // cout << "new minKey: " << key << endl;
            if (minKeyLocation)
                minKeyLocation->prevWithValue = front;
            front->nextWithValue = minKeyLocation;
            minKeyLocation = front;
        }
    }

    void incPosition(MyListNode* position, const string& key) {
        if (!position->next) {
            position->next = new MyListNode(position->count+1);
            position->next->prev = position;
        }

        if (position->next->container.size() == 0) {
            MyListNode* further = position->nextWithValue;
            position->nextWithValue = position->next;
            position->next->prevWithValue = position;
            position->next->nextWithValue = further;
        }

        position->container.erase(key);
        position->next->container.insert(key);
        mapping[key] = position->next;

        if (back == position) {
            back = position->next;
            size++;
        }

        if (position->container.size() == 0) {
            // cout << "count: " << position->count << " is empty, rerouting" << endl;
            if (minKeyLocation == position)
                minKeyLocation = position->next;
            // skip empty nodes
            MyListNode* np = position->prevWithValue;
            MyListNode* nn = position->nextWithValue;
            if (np) np->nextWithValue = nn;
            if (nn) nn->prevWithValue = np;
            position->prevWithValue = nullptr;
            position->nextWithValue = nullptr;
        }
    }

    void inc(string key) {
        auto it = mapping.find(key);
        // cout << "inc(" << key << ") to " << (it == mapping.end() ? 1 : it->second->count + 1) << endl;
        if (it == mapping.end()) {
            incFront(key);
        } else {
            incPosition(it->second, key);
        }
    }

    void dec(string key) {
        MyListNode* position = mapping[key];
        // cout << "dec(" << key << ") to " << (position->count - 1) << endl;
        if (position->count == 1) {
            mapping.erase(key);
        } else {
            position->prev->container.insert(key);
            mapping[key] = position->prev;
        }

        position->container.erase(key);

        if (position->container.size() == 0) {
            // cout << "count: " << position->count << " is empty, rerouting" << endl;
            if (back == position) {
                back = position->prev;
                size--;
            }

            if (minKeyLocation == position) {
                if (minKeyLocation->prev) {
                    minKeyLocation = position->prev;
                } else {
                    minKeyLocation = position->nextWithValue;
                }
            }

            // skip empty nodes
            MyListNode* np = position->prevWithValue;
            MyListNode* nn = position->nextWithValue;
            if (np) np->nextWithValue = nn;
            if (nn) nn->prevWithValue = np;
            position->prevWithValue = nullptr;
            position->nextWithValue = nullptr;
        }

    }

    string getMaxKey() {
        // cout << "getMaxKey()" << endl;
        // getState();
        if (size == 0) return "";
        return *back->container.begin();
    }

    string getMinKey() {
        // cout << "getMinKey()" << endl;
        // getState();
        if (size == 0) return "";
        return *minKeyLocation->container.begin();
    }
};

int main() {
    {
        AllOne container;
        container.inc("hello");
        container.inc("hello");
        assert(container.getMaxKey() == "hello");
        assert(container.getMinKey() == "hello");
        container.inc("leet");
        assert(container.getMaxKey() == "hello");
        assert(container.getMinKey() == "leet");
    }
    {
        AllOne container;
        container.inc("hello");
        container.inc("goodbye");
        container.inc("hello");
        container.inc("hello");
        assert(container.getMaxKey() == "hello");
        container.inc("leet");
        container.inc("code");
        container.inc("leet");
        container.dec("hello");
        container.inc("leet");
        container.inc("code");
        container.inc("code");
        unordered_set<string> expected1({"leet", "code"});
        assert(expected1.find(container.getMaxKey()) != expected1.end());
    }
    {
        AllOne container;
        container.inc("hello");
        container.inc("hello");
        assert(container.getMinKey() == "hello");
        assert(container.getMaxKey() == "hello");
        container.dec("hello");
        container.dec("hello");
        assert(container.getMinKey() == "");
        assert(container.getMaxKey() == "");
        container.inc("hello");
        assert(container.getMinKey() == "hello");
        assert(container.getMaxKey() == "hello");
    }
    {
        AllOne container;
        container.inc("a");
        container.inc("b");
        container.inc("b");
        container.inc("b");
        container.inc("b");
        container.dec("b");
        container.dec("b");
        assert(container.getMaxKey() == "b");
        assert(container.getMinKey() == "a");
    }
    {
        AllOne container;
        container.inc("a");
        container.inc("b");
        container.inc("b");
        container.inc("c");
        container.inc("c");
        container.inc("c");
        container.dec("b");
        container.dec("b");
        assert(container.getMinKey() == "a");
        container.dec("a");
        assert(container.getMaxKey() == "c");
        assert(container.getMinKey() == "c");
    }
    {
        AllOne container;
        container.inc("hello");
        container.inc("hello");
        container.inc("world");
        container.inc("world");
        container.inc("hello");
        container.dec("world");
        assert(container.getMaxKey() == "hello");
        assert(container.getMinKey() == "world");
        container.inc("world");
        container.inc("world");
        container.inc("leet");
        unordered_set<string> expected1({"hello", "world"});
        assert(expected1.find(container.getMaxKey()) != expected1.end());
        assert(container.getMinKey() == "leet");
        container.inc("leet");
        container.inc("leet");
        unordered_set<string> expected2({"hello", "world", "leet"});
        assert(expected2.find(container.getMinKey()) != expected2.end());
        assert(expected2.find(container.getMaxKey()) != expected2.end());
    }
    {
        AllOne container;
        for (int i=0; i<16; i++)
            container.inc("a");
        container.inc("b");
        container.inc("b");
        container.inc("c");
        assert(container.getMinKey() == "c");
        container.dec("c");
        assert(container.getMinKey() == "b");
    }
    {
        AllOne container;
        container.inc("hello");
        container.inc("hello");
        container.inc("hello");
        container.inc("leet");
        assert(container.getMinKey() == "leet");
        container.inc("lala");
        container.inc("lala");
        container.dec("leet");
        assert(container.getMinKey() == "lala");
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */