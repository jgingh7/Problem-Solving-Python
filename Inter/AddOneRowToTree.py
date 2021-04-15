# https://leetcode.com/problems/add-one-row-to-tree/
# Time: O(sizeOfTree)
# Space: O(heightOfTree)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            root = TreeNode(val, root)
            return root
            
        def dfs(node, level):
            if level + 1 == depth:
                if node.left:
                    temp = node.left
                    node.left = TreeNode(val, temp)
                    dfs(node.left, level + 1)
                else:
                    node.left = TreeNode(val)
            
                if node.right:
                    temp = node.right
                    node.right = TreeNode(val, right=temp)
                    dfs(node.right, level + 1)
                else:
                    node.right = TreeNode(val)
            else:
                if node.left:
                    dfs(node.left, level + 1)
                if node.right:
                    dfs(node.right, level + 1)

            
        dfs(root, 1)
        
        return root