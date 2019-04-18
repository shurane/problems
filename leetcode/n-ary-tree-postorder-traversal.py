# Definition for a Node.
class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root):
        if not root:
            return []
        elif not root.children:
            return [root.val]
        
        lst = []
        for child in root.children:
            values = self.postorder(child)
            lst.extend(values)
        
        lst.append(root.val)
        return lst

    def postorder_iterative(self, root):
        if not root:
            return []

        stack = [root]
        values = []

        while stack:
            node = stack.pop()
            # for child in node.children:
            #     stack.append(child)
            stack.extend(node.children)
            values.append(node.val)
        
        print(values)
        return values[::-1]

s = Solution()

t1_n3 = Node(3)
t1_n3.children = [Node(5), Node(6)]
t1 = Node(1)
t1.children = [t1_n3, Node(2), Node(4)]

assert s.postorder_iterative(None) == []
assert s.postorder_iterative(Node(1, [Node(2), Node(3)])) == [2,3,1]
assert s.postorder_iterative(t1) == [5,6,3,2,4,1]