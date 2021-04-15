# https://leetcode.com/problems/network-delay-time/
# Time: O(ElogV)
# Space: O(V) #size of heap (at most V because heap only adds neighbors of the current SSSPT)

import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        #SSSP, use dijkstra's algo
        #return the maximum among the SSSPs of vertices
        #if a vertex is not included in the SSSP tree, return -1
        
        edges = defaultdict(dict)
        
        #build something like adjacency list
        for start, end, weight in times:
            edges[start][end] = weight
  
        heap = [(0, K)] #sssp, start vertex
        SSSPT = {}
        while heap:
            sssp, vertex = heapq.heappop(heap) # 1) extract min, O(VlogV)
            if vertex in SSSPT: # if the vertex is already in SSSPT,
                                # it means that the vertex already has a sssp value (the node has a larger sssp candidate value)
                                # so pop the node and continue
                continue
                
            SSSPT[vertex] = sssp # 2) add vertex to SSSP, O(V)
                                 # you can put this vertex with this sssp value in the SSSPT because
                                 # a. it is a neighbor of a component of SSSPT
                                 # b. it is the smallest value in the heap, so this is like adding the smallest sum weight edge's end vertex (vertex with SSSP) to the SSSPT
            for neighbor in edges[vertex]: # 3) for degree of vertex, O(E)
                if neighbor not in SSSPT: # not necessary, but makes heap size smaller
                                          # if neighbor is not in SSSPT, put them in the heap with possible sssp candidates
                                          # only heaps that are neighbors of a SSSPT component will be pushed due to first if statement in while loop
                    heapq.heappush(heap, (sssp + edges[vertex][neighbor], neighbor)) #O(logV)
                    
        return -1 if len(SSSPT) < N else max(SSSPT.values())