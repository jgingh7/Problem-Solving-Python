# https://leetcode.com/problems/is-graph-bipartite/
# Time: Recursion happens for the respective edges(E) for each V so it should just be O(V + E) only?
# Space: O(V + E) - dictionary + recursion stack

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #dfs/bfs using the first node
        #color them BWBWBW
        #if a BB or WW is met, False
        #if a node is not colored, False
        
        
        nodeColors = {0: 'B'}
        
        
        def dfs(nodeIdx):
            res = True
            nextColor = 'B'
            if nodeIdx in nodeColors and nodeColors[nodeIdx] == 'B':
                nextColor = 'W'
            
            neighbors = graph[nodeIdx]
            
            for neighbor in neighbors:
                if neighbor in nodeColors:
                    if nodeColors[neighbor] != nextColor:
                        return False
                else:
                    nodeColors[neighbor] = nextColor
                    res = dfs(neighbor)
            
            return res
             
        for i in range(len(graph)):
            if not dfs(i):
                return False
            
        
        return True