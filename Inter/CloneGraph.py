# https://leetcode.com/problems/clone-graph/submissions/
# Time: O(V+E)
# Space: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        copyTracker = {node: Node(node.val)}
        self.dfs(node, copyTracker)
        
        return copyTracker[node]
    
    def dfs(self, node: 'Node', copyTracker):
        for neigh in node.neighbors:
            if neigh not in copyTracker:
                copyTracker[neigh] = Node(neigh.val)
                self.dfs(neigh, copyTracker)
                
            copyTracker[node].neighbors.append(copyTracker[neigh])