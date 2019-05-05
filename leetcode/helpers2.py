class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.val})"

    def __eq__(self, other):
        if other is None:
            return False
        return self.val == other.val

    def printLevels(self, level = 0):
        s = f"{' ' * (2*level)}{level}:{self}\n"

        if self.left:
            s += "l" + self.left.printLevels(level + 1)

        if self.right:
            s += "r" + self.right.printLevels(level + 1)

        return s

def create_tree(lst: 'List'):
    if len(lst) == 0:
        return None

    q = [TreeNode(lst[0])]

    for i in range(1, len(lst)):
        value = lst[i]
        if value != None:
            node = TreeNode(value)
            q.append(node)

            parent = (i - 1) // 2
            if i % 2 == 1:
                q[parent].left = node
            else:
                q[parent].right = node
        else:
            q.append(None)

    return q[0]

def create_tree_recursive(lst: 'List', i=0):
    if not lst:
        return None

    node = TreeNode(lst[i])

    left = i * 2 + 1
    if left < len(lst) and lst[left] != None:
        node.left = create_tree_recursive(lst, left)

    right = i * 2 + 2
    if right < len(lst) and lst[right] != None:
        node.right = create_tree_recursive(lst, right)

    return node

## testing for tree methods
# for lst in [[1,2,3,4,5,6], [1,2,3,4,None,6]]:
#     print("working with this list:", lst)
#     iterative = create_tree(lst)
#     print("iterative\n", iterative.printLevels())

#     recursive = create_tree_recursive(lst)
#     print("recursive\n", recursive.printLevels())