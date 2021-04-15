# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        orderedEle = self.inorder(root)
        
        return orderedEle[k - 1]
        
    
    def inorder(self, root: TreeNode) -> List[int]:
        if root:
            return self.inorder(root.left) + [root.val] + self.inorder(root.right)
        else:
            return []