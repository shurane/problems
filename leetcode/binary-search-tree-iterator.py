from helpers2 import TreeNode

def leftmost(node: TreeNode, lst: List[TreeNode]) -> TreeNode:
    if not node:
        return None
    while node.left:
        lst.append(node)
        node = node.left
    return node

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root:      TreeNode = root
        self.current:   TreeNode = root
        self.lst:     List[TreeNode] = []
        if self.current:
            self.current = leftmost(self.current, self.lst)
            
        print([item.val for item in self.lst])

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.current
        
        if self.current.right:
            self.current = leftmost(self.current.right, self.lst)
        else:
            if self.lst:
                self.current = self.lst.pop()
            else:
                self.current = None
            
        return node.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.current != None
