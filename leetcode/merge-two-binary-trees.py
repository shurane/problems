from helpers2 import TreeNode, create_tree

# https://leetcode.com/problems/merge-two-binary-trees/description/
class Solution(object):
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.mergeTreesIterative(t1, t2)

    def mergeTreesRecursive(self, t1, t2):
        if t1 == None and t2 == None:
            return None
        elif t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTreesRecursive(t1.left, t2.left)
            node.right = self.mergeTreesRecursive(t1.right, t2.right)
            return node
        elif t1:
            node = TreeNode(t1.val)
            node.left = self.mergeTreesRecursive(t1.left, None)
            node.right = self.mergeTreesRecursive(t1.right, None)
            return node
        else: #elif t2:
            node = TreeNode(t2.val)
            node.left = self.mergeTreesRecursive(None, t2.left)
            node.right = self.mergeTreesRecursive(None, t2.right)
            return node

    def mergeTreesIterative(self, t1: TreeNode, t2: TreeNode):
        t1_nodes = [t1]
        t2_nodes = [t2]
        t3 = TreeNode(0)
        t3_nodes = [t3]
        #bfs algorithm
        while t1_nodes and t2_nodes:
            l = t1_nodes.pop(0)
            r = t2_nodes.pop(0)
            m = t3_nodes.pop(0)
            # print(l, r, m, t1_nodes, t2_nodes, t3_nodes)

            if l and r:
                m.val = l.val + r.val
            elif l:
                m.val = l.val
            elif r:
                m.val = r.val
            else:
                # l and r are None Should figure out a way to get rid of m so we don't have TreeNode(0) elems
                pass

            if l or r:
                if l:
                    t1_nodes.extend([l.left, l.right])
                else:
                    t1_nodes.extend([None, None])
                if r:
                    t2_nodes.extend([r.left, r.right])
                else:
                    t2_nodes.extend([None, None])

                m.left = TreeNode(0)
                m.right = TreeNode(0)
                t3_nodes.extend([m.left, m.right])

        return t3

s = Solution()

left = create_tree([1,3,2,5])
right = create_tree([2,1,3,None,4,None,7])
assert s.mergeTreesRecursive(left, right) == create_tree([3,4,5,5,4,None,7])
assert s.mergeTreesIterative(left, right) == create_tree([3,4,5,5,4,None,7])

"""
l1
        1
    2      <>
  3  <>  <>  <>

r1
        1
    <>      2
  <>  <>  <>  3

output1
        2
    2       2
  3  <>   <>  3

"""
l1 = create_tree([1,2,None,3])
r1 = create_tree([1,None,2,None,None,None,3])
assert s.mergeTreesRecursive(l1, r1) == create_tree([2,2,2,3,None,None,3])
assert s.mergeTreesIterative(l1, r1) == create_tree([2,2,2,3,None,None,3])