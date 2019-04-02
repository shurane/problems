from helpers import TreeNode, listToTree

# https://leetcode.com/problems/merge-two-binary-trees/description/
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
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

    def mergeTreesIterative(self, t1, t2):
        t1_nodes = [t1]
        t2_nodes = [t2]
        t3 = TreeNode(0)
        t3_nodes = [t3]
        #bfs algorithm
        while t1_nodes and t2_nodes:
            l = t1_nodes.pop(0)
            r = t2_nodes.pop(0)
            m = t3_nodes.pop(0)
            print(l, r, m, t1_nodes, t2_nodes, t3_nodes)

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

        
left = listToTree([1,3,2,5])
right = listToTree([2,1,3,None,4,None,7])

input1_t1 = listToTree([1,2,None,3])
input1_t2 = listToTree([1,None,2,None,None,None,3])

"""
input1_t1
        1
    2      <>
  3  <>  <>  <>

input1_t2
        1
    <>      2
  <>  <>  <>  3

output1
        2
    2       2
  3  <>   <>  3

"""

s = Solution()
merged = s.mergeTrees(left, right)
output1 = s.mergeTrees(input1_t1, input1_t2)