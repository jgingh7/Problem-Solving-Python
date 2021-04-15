# https://leetcode.com/problems/validate-binary-search-tree/
# Time: O(n)
# Space: O(n) - recursion stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def isValidBST(self, root: TreeNode) -> bool:
        self.currVal = None
        
        def helper(root):
            if root:
                if root.left: 
                    if not helper(root.left): #currVal is kept smaller than root if returns True
                        return False
                
                # on root.left, currVal slowly increases, but should not be bigger than root.val
                # on root.right, currVal which is a beforeVal, is compared to current root.val, and beforeVal should always be smaller than root.val
                if self.currVal != None and self.currVal >= root.val:
                    return False
                self.currVal = root.val

                if root.right:
                    if not helper(root.right): #currVal is kept larger than root if returns True
                        return False

                return True
        
        return helper(root)