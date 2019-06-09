from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        allLevels = []
        q = [(root, 0)]
        
        levelValue = 0
        levels = []
        
        while q:
            current, currentLevel = q.pop(0)
            # print(current.val, currentLevel)
            if current.left:
                q.append((current.left, currentLevel + 1)) 
            if current.right:
                q.append((current.right, currentLevel + 1))
            
            if currentLevel == levelValue:
                levels.append(current.val)
            else:
                allLevels.append(levels)
                levels = [current.val]
                levelValue = currentLevel
                
        if levels:
            allLevels.append(levels)
        
        return list(reversed(allLevels))
            
        