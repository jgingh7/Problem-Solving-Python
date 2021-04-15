# https://leetcode.com/problems/evaluate-division/
# Time: O(E + V * len(queries)) - goes through all the edges once for each query
# Space: O(E) + O(len(queries)) - recursion stack, answer list


from collections import defaultdict

class Solution:
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        G = self.build_graph(equations, values)
        return [self.dfs(beg, target, G, set(), 1.0) for beg, target in queries] #set() should be initialized here, because different set() is needed for different query

    def build_graph(self, equations, values):
        graph = defaultdict(dict)

        def add_edge(start, end, value):
            graph[start][end] = value

        for vertices, value in zip(equations, values):
            start, end = vertices
            # edge for both directions
            add_edge(start, end, value)
            add_edge(end, start, 1/value)

        return graph

    def dfs(self, start, end, graph, visited, value):
        # if starting point is not in graph or ending point is not in graph, or you are in a cycle, return -1
        if (start not in graph) or (end not in graph) or (start in visited): 
            return -1.0
        if start == end: # if one of the neighbors is finally the target point, return the value
            return value
        
        visited.add(start)
        
        # for all of the neighboring points, 
        for neighbor, currEdgeVal in graph[start].items():
            dfsVal = self.dfs(neighbor, end, graph, visited, currEdgeVal*value)
            if dfsVal != -1.0:
                return dfsVal
            
        # if all neighbors return -1, return -1
        return -1.0