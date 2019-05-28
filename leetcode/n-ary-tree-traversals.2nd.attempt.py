# Definition for a Node.
class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

class Solution:
    # https://leetcode.com/problems/n-ary-tree-postorder-traversal/
    def postorder(self, root):
        if not root: return []

        lst = []
        for child in root.children:
            values = self.postorder(child)
            lst.extend(values)

        lst.append(root.val)
        return lst

    def postorder_iterative(self, root):
        if not root: return []

        stack = [root]
        values = []

        while stack:
            node = stack.pop()
            # for child in node.children:
            #     stack.append(child)
            stack.extend(node.children)
            values.append(node.val)

        return values[::-1]

    # https://leetcode.com/problems/n-ary-tree-preorder-traversal/
    def preorder(self, root):
        if not root: return []

        lst = []
        lst.append(root.val)
        for values in map(self.preorder, root.children):
            lst.extend(values)
        return lst

    def preorder_iterative(self, root):
        if not root: return []

        queue = [root]
        values = []

        while queue:
            node = queue.pop(0)
            values.append(node.val)
            queue = node.children + queue # insert children at the front of the list

        return values

    # https://leetcode.com/problems/n-ary-tree-level-order-traversal/
    def levelorder(self, root, level=0):
        if not root: return []

        values = [(level, root.val)]

        for child in root.children:
            values.extend(self.levelorder(child, level=level + 1))

        # doesn't look elegant, but technically it's recursive + a reconstruction afterwards
        if level == 0:
            levels = []
            for l, value in values:
                if len(levels) <= l:
                    levels.append([])
                
                levels[l].append(value)
            
            return levels

        else:
            return values
            

    def levelorder_iterative(self, root):
        if not root: return []

        levels = []
        queue = [(0, root)]

        while queue:
            level, node = queue.pop(0)
            for child in node.children:
                queue.append((level + 1, child))

            if len(levels) <= level:
                levels.append([])

            levels[level].append(node.val)
        
        return levels

    def levelorder_iterative2(self, root):
        # inspiration from https://leetcode.com/problems/n-ary-tree-level-order-traversal/discuss/148877/Python-5-lines-BFS-solution
        queue = [root]
        levels = []

        while queue:
            levels.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children if child]

        return levels
            

s = Solution()

t1_n3 = Node(3)
t1_n3.children = [Node(5), Node(6)]
t1 = Node(1)
t1.children = [t1_n3, Node(2), Node(4)]

assert s.postorder(None) == []
assert s.postorder(Node(1, [Node(2), Node(3)])) == [2,3,1]
assert s.postorder(t1) == [5,6,3,2,4,1]

assert s.postorder_iterative(None) == []
assert s.postorder_iterative(Node(1, [Node(2), Node(3)])) == [2,3,1]
assert s.postorder_iterative(t1) == [5,6,3,2,4,1]

assert s.preorder(None) == []
assert s.preorder(Node(1, [Node(2), Node(3)])) == [1,2,3]
assert s.preorder(t1) == [1,3,5,6,2,4]

assert s.preorder_iterative(None) == []
assert s.preorder_iterative(Node(1, [Node(2), Node(3)])) == [1,2,3]
assert s.preorder_iterative(t1) == [1,3,5,6,2,4]

assert s.levelorder_iterative2(t1) == [[1], [3,2,4], [5,6]]