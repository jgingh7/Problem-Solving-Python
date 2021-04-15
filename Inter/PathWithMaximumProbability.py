# https://leetcode.com/problems/path-with-maximum-probability/
# Time: O(ElogV)
# Space: O(E)


from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # use dijkstra with multiplication

        # make adjacency list of edges
        edgesAdjList = defaultdict(dict)
        for i in range(len(edges)):
            edgesAdjList[edges[i][0]][edges[i][1]] = succProb[i]
            edgesAdjList[edges[i][1]][edges[i][0]] = succProb[i]
            
       
        heap = [(-1, start)] # use maxheap
        visited = set()
        
        while heap:
            score, beg = heapq.heappop(heap)
            visited.add(beg) # add to the tree of vertices with maximum probablity score
            
            if beg == end:
                return score * -1 # return with multiplication of -1, because we are intending to use a maxheap
            for fin in edgesAdjList[beg]:
                if fin not in visited:
                    heapq.heappush(heap, (score * edgesAdjList[beg][fin], fin))       
        
        return 0