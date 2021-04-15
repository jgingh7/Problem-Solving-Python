# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
# Time: O(number of nodes)
# Space: O(number of nodes)

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        nextQueue = deque()
        ans = []
        queue.append(root)
        
        while True:
            currArr = []
            while queue:
                curr = queue.popleft()
                currArr.append(curr.val) #append curr val to currArr and append its left and right to nextQueue
                if curr.left:
                    nextQueue.append(curr.left)
                if curr.right:
                    nextQueue.append(curr.right)

            ans.append(currArr) #append currArr
            if nextQueue: #reset queue
                queue = nextQueue
                nextQueue = deque()
            else: #if there is no nextQueue, break
                break
                
        return ans