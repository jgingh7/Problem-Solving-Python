# https://leetcode.com/problems/as-far-from-land-as-possible/
# Time: O(m*n)
# Space: O(m*n)

from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        
        q = deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])    
        # q = deque()
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             q.append((i, j))
        
            
        if len(q) == m * n or len(q) == 0: #if all land or no land, return -1
            return -1
        
        level = 0
        while q:
            size = len(q)
            for _ in range(size): #iterating current level
                i,j = q.popleft() #curr position
                for x,y in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    xi, yj = x+i, y+j
                    if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0: #if xi and yj is in the bound and is water
                        q.append((xi, yj)) #add next positions
                        grid[xi][yj] = 1 #make position into land so that other bfses do not count that area
            if q: # if there is a next level to go, increment level
                level += 1
                
        return level