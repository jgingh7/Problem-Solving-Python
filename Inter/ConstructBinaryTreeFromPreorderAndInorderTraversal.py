# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Time: O(n^2)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
                
        ans = TreeNode(preorder.pop(0))
        leftMax = inorder.index(ans.val)

        ans.left = self.buildTree(preorder, inorder[:leftMax])      
        ans.right = self.buildTree(preorder, inorder[leftMax + 1:])

        return ans
    


# Optimized to be O(n) in Time and Space
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.counter = 0
        inOrderdict = {val:i for i, val in enumerate(inorder)}
                
        def helper(start: int, end: int) -> TreeNode:
            if start > end:
                return None

            ans = TreeNode(preorder[self.counter]) # Optimize pop(0)
            idx = inOrderdict[ans.val] # Optimize .index
            self.counter += 1

            ans.left = helper(start, idx - 1)      
            ans.right = helper(idx + 1, end)
            
            return ans

        return helper(0, len(preorder) - 1)