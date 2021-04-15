# https://leetcode.com/problems/all-paths-from-source-to-target/
# Time: O(n 2^n)
# Space: O(n 2^n)

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:        
        final = []
        
        self.dfs(graph, [0], final)
        
        return final
    
    def dfs(self, graph: List[List[int]], tracker: List[int], final: List[int]) -> None:
        currIdx = tracker[-1]
        if currIdx == len(graph) - 1:
            final.append(tracker)
            return      
        
        for neighbor in graph[currIdx]:
            self.dfs(graph, tracker + [neighbor], final)