# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Time: O(ElogV) - extract min, O(VlogV)
#                - add relaxed node of a after vertex for every neighbors of a before vertex (after vertex = "vertex of edge's start")
#                  -> O(degree(before vertex))*O(logV) for every vertex -> O(ElogV)
# Space: O(E)

import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        #dijkstra's

        edges = defaultdict(dict)
        
        #build something like adjacency list
        for start, end, weight in flights:
            edges[start][end] = weight

        heap = [(0, src, 0)] #sssp, starting vertex, kcounter
        
        while heap:
            sssp, start, k = heapq.heappop(heap) #extract min
            if start == dst:
                return sssp
            if k <= K:
                for end in edges[start]: #populate the heap with neighbors from current node
                                         #which has sssp from src to current vertex in node

                                         #keep incrementing k, so that if k value for the vertex goes over K, and the vertex is not dst
                                         #it can be popped out from the heap without going into any if statements
                    heapq.heappush(heap, (sssp + edges[start][end], end, k + 1))
                    
        return -1