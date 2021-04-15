# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Time: O(n)
# Space: O(n) - 2 stacks

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        LtoR = deque()
        RtoL = deque()
        
        LtoR.append(root)
        ans = []
        while LtoR or RtoL:
            ansPart = []
            
            if LtoR:
                while LtoR:
                    curr = LtoR.pop()
                    ansPart.append(curr.val)
                    if curr.left:
                        RtoL.append(curr.left)
                    if curr.right:
                        RtoL.append(curr.right)     
            else:
                while RtoL:
                    curr = RtoL.pop()
                    ansPart.append(curr.val)
                    if curr.right:
                        LtoR.append(curr.right)
                    if curr.left:
                        LtoR.append(curr.left)        
                        
            ans.append(ansPart)
                        
        return ans