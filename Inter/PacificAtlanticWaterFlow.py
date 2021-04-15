# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Time: O(mn)
# Space: O(mn)

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        
        
        pacificSet = set()
        atlanticSet = set()
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i, row in enumerate(matrix):
            pacificSet.add((i, 0))
            atlanticSet.add((i, n - 1))
            
        for i, col in enumerate(matrix[0]):
            pacificSet.add((0, i))
            atlanticSet.add((m - 1, i))
                    
        if m <= 1 or n <= 1:
            return pacificSet
        
        def bfs(queue):
            reachable = set()
            while queue:
                point = queue.popleft()
                reachable.add(point)
                oriX = point[0]
                oriY = point[1]
                for (x, y) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nextX = oriX + x
                    nextY = oriY + y
                    
                    if nextX >= len(matrix) or nextY >= len(matrix[0]) or nextX < 0 or nextY < 0:
                        continue
                    
                    if (nextX, nextY) in reachable:
                        continue
                    
                    if matrix[oriX][oriY] > matrix[nextX][nextY]:
                        continue
                        
                    queue.append((nextX, nextY))
                    
            return reachable
        
        
        pacificReachable = bfs(deque(pacificSet))
        atalanticReachable = bfs(deque(atlanticSet))
        ansSet = pacificReachable.intersection(atalanticReachable)
        
        ans = []
        for val in ansSet:
            ans.append(list(val))
        
        return ans
