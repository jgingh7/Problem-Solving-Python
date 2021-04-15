# https://leetcode.com/problems/shortest-path-with-alternating-colors/
# Time: O(V + E) (not O(E) because can be composed of multiple components)
# Space: O(E)

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        G = [[[], []] for i in range(n)]
        for start, end in red_edges:
            G[start][0].append(end)
        for start, end in blue_edges:
            G[start][1].append(end)
            
        # G[startPoint][color] = endPoints
        # if color == 0, red
        # if color == 1, blue
        
        ans = [[0, 0]] + [[n * 2, n * 2] for i in range(n - 1)] # n * 2 is the maximum possible size of steps + 1
        bfs = [[0, 0], [0, 1]]
        
        for start, color in bfs:
            for end in G[start][color]: # G[i][c] are list of js, j is the end of directed edge
                if ans[end][color] == n * 2: # if not, ans[end][color] will already be in its least step
                    otherColor = 1 - color
                    ans[end][color] = ans[start][otherColor] + 1
                    bfs.append([end, otherColor])
        
        return [x if x < n * 2 else -1 for x in map(min, ans)]