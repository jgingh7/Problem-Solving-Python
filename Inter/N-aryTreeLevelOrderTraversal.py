# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# Time: O(nodes)
# Space: O(max number of nodes in a level)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        nextLevel = deque()
        nextLevel.append(root)
        
        ans = []
              
        while nextLevel:
            currLevel = nextLevel
            nextLevel = deque()
            
            insideArr = []
            while currLevel:
                currNode = currLevel.popleft()
                for child in currNode.children:
                    nextLevel.append(child)
                    
                insideArr.append(currNode.val)
            
            if insideArr:
                ans.append(insideArr)
        
        return ans