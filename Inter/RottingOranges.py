# https://leetcode.com/problems/rotting-oranges/
# Time: O(mn)
# Space: O(mn)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottenOsQueue = deque()
        freshOs = set()
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rottenOsQueue.append((i, j))
                elif grid[i][j] == 1:
                    freshOs.add((i, j))
        
        if not freshOs:
            return 0
        
        def bfs(queue):
            counter = 0
            minuteCounter = len(queue) # counter of bfs level (when one level ends, 1 minute increases)
            
            while queue:
                point = queue.popleft()
                oriX = point[0]
                oriY = point[1]
                for (x, y) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nextX = oriX + x
                    nextY = oriY + y
                    
                    if nextX >= m or nextY >= n or nextX < 0 or nextY < 0:
                        continue
                        
                    if grid[nextX][nextY] == 2:
                        continue
                    
                    if grid[nextX][nextY] == 0:
                        continue
                    
                    grid[nextX][nextY] = 2 # if grid[nextX][nextY] == 1
                    freshOs.discard((nextX, nextY))
                    queue.append((nextX, nextY))
                    
                minuteCounter -= 1
                if minuteCounter == 0:
                    counter += 1
                    minuteCounter = len(queue)
                    
            return counter - 1 # take out the last addition when ending
    
        ans = bfs(rottenOsQueue)
        
        return ans if not freshOs else -1 #if there still are fresh oranges, return -1