# https://leetcode.com/problems/validate-binary-search-tree/
# Time: O(number of nodes)
# Space: O(n) - recursion stack


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(curr: TreeNode, lower: int, upper: int) -> bool:
            if not curr:
                return True
            
            currVal = curr.val
            
            # if there is a lower bound and if the currVal is less than or equal to lower bound OR
            # if there is an upeer bound and if the currVal is bigger than or equal to upper bound
            # return False
            if (lower != None and currVal <= lower) or (upper != None and currVal >= upper):
                return False
            
            # check if curr.left with lower bound as lower and upper bound as currVal (because all values on left has to be less than currVal) AND
            # curr.right with lower bound as currVal and upper bound as upper (because all values on right has to be larger than currVal)
            # are both True
            # so if keep going left, there is no lower bound, and if keep going right, there is not upper bound
            return helper(curr.left, lower, currVal) and helper(curr.right, currVal, upper)
            
        return helper(root, None, None)