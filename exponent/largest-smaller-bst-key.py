# https://www.tryexponent.com/practice/prepare/largest-smaller-bst-key

##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 70 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################


from typing import Optional

# A node
class Node:
    # Constructor to create a new node
    def __init__(self, key: int):
        self.key: int = key
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.parent: Optional['Node'] = None

# A binary search tree
class BinarySearchTree:
    # Constructor to create a new BST
    def __init__(self):
        self.root: Optional[Node] = None

    def find_largest_smaller_key(self, num: int) -> Optional[int]:

        # bestValue = -1
        # def helper(node: Node) -> None:
        #     nonlocal bestValue
        #     nonlocal num
        #     if node is None:
        #         return
        #     elif node.key >= num:
        #         helper(node.left)
        #     else:
        #         bestValue = max(bestValue, node.key)
        #         helper(node.right)

        # helper(self.root)

        bestValue = -1
        current = self.root
        while current is not None:
            if current.key >= num:
                current = current.left
            else:
                bestValue = max(bestValue, current.key)
                current = current.right

        return bestValue

    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key: int) -> None:
        # 1) If tree is empty, create the root
        if (self.root is None):
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)

        while(currentNode is not None):
            if(key < currentNode.key):
                if(currentNode.left is None):
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if(currentNode.right is None):
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.right

#########################################
# Driver program to test above function #
#########################################

bst = BinarySearchTree()

# Create the tree given in the above diagram
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

result: Optional[int] = bst.find_largest_smaller_key(17)

print("Largest smaller number is %d " % (result if result is not None else -1))