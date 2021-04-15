# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        levelVals = collections.defaultdict(list)
        
        
        def dfs(node, level):
            levelVals[level].append(node.val)
            
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
            
        dfs(root, 0)


        ans = []    
        for i in reversed(range(len(levelVals))):
            ans.append(levelVals[i])
        
   
        return ans