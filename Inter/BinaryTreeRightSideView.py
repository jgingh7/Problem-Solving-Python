# https://leetcode.com/problems/binary-tree-right-side-view/
# Time: O(n)
# Space: O(n) - queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # level traverse
        # print the last one before going to another level
        if not root:
            return []
        
        queue = deque()
        nextQueue = deque()
        queue.append(root)
        ans = []
        
        while queue:
            curr = None
            while queue:
                curr = queue.popleft()
                if curr.left:
                    nextQueue.append(curr.left)
                if curr.right:
                    nextQueue.append(curr.right)
                
            ans.append(curr.val)
                            
            if nextQueue:
                queue = nextQueue
                nextQueue = deque()
            else:
                break
                
        return ans