# https://leetcode.com/problems/binary-tree-right-side-view/
# Time: O(n)
# Space: O(n) - queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        from collections import deque 
        
        ans = []
        if root:
            nextLevel = deque() 
            nextLevel.append(root)
            while nextLevel:
                currLevel = nextLevel
                nextLevel = deque()
                while currLevel:
                    curr = currLevel.popleft()
                    if not currLevel:
                        ans.append(curr.val)
                    if curr.left:
                        nextLevel.append(curr.left)
                    if curr.right:
                        nextLevel.append(curr.right)


        return ans