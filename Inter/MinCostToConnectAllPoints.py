# https://leetcode.com/problems/min-cost-to-connect-all-points/
# Time: O(V^2) to make adjency list, O(ElogV) if without the part of constructing adjacency list
# Space: O(E)

from collections import defaultdict

#Kruskal's
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:     
        V = len(points)
        
        # 1) make forest of vertices, O(V)
        # make components as like a linked list using dictionary
        components = defaultdict(list)
        for i in range(V):
            points[i].append(i)
            components[i].append(points[i])
            
        edges = []
        
        
        # extra) construct edges with weights, O(V^2)
        for i in range(V):         
            for j in range(i + 1, V):
                start = points[i]
                end = points[j]
                edges.append((start, end, abs(start[0] - end[0]) + abs(start[1] - end[1])))
            

        # 2) sort edges, O(ElogE) = O(ElogV)
        edges.sort(key=lambda x: x[2]) 
        
        
        MST = []
        
        # 3)
        for edge in edges:
            if len(MST) == V - 1: # if MST is completed, break
                break

            if edge[0][2] == edge[1][2]: # if the two points of edge are in the same component, then continue
                continue
            else: # if the two vertices are in different components, take the smaller component and change its component to the larger one, O(VlogV) when for looped, O(ElogV)
                if len(components[edge[0][2]]) < len(components[edge[1][2]]):
                    for vertex in components[edge[0][2]]:
                        vertex[2] = edge[1][2]
                        components[edge[1][2]].append(vertex)
                else:
                    for vertex in components[edge[1][2]]:
                        vertex[2] = edge[0][2]
                        components[edge[0][2]].append(vertex)
                MST.append(edge) # add edge, O(E) when for looped

        ans = 0
        for edge in MST:
            ans += edge[2]
            
        return ans


#Prim's
import heapq
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        V = len(points)
        edgesAdjList = defaultdict(list)
        
        # extra) make adjacency list of edges, labling each vertices with value of i and j (0,1,2,...,V-1)
        for i in range(V):
            for j in range(i + 1, V):
                weight = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                edgesAdjList[i].append((weight, j))
                edgesAdjList[j].append((weight, i))
        

        heap = edgesAdjList[0]
        
        heapq.heapify(heap) #heapify all the neighbors of starting vertex
        
        MST = {}
        MST[0] = 0 # 1) start with any vertex s; set w(s) = 0
        
        while heap: # 3) while pr.queue not empty
            weight, vertex = heapq.heappop(heap) # 3) extract min, O(VlogV)
            
            if vertex in MST: # this is like the part of 3) where if w(q) > w(q,x) then decrease
                              # rather than decrease, here, you only pop and skip that vertex to never let it be put in the MST
                continue
                
            MST[vertex] = weight # add edge to T (mark x in T), O(V) (keeps track of min edge O(1) * V)
            
            for neighbor in edgesAdjList[vertex]: # for each (unmarked) neighbor q of x, O(E)
                if neighbor not in MST: # not necessary, but makes heap size smaller
                    heapq.heappush(heap, neighbor) #O(logV)
            
            # works without this, but becomes very slow
            # if we have MST with all the vertices, end the while loop
            if len(MST) >= V:
                break
        
        
        return sum(MST.values())