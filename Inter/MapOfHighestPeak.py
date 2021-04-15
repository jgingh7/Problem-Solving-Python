# https://leetcode.com/problems/map-of-highest-peak/
# Time: O(mn)
# Space: O(mn)

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        
        waters = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    waters.append((i, j))
                else:
                    isWater[i][j] = 'L'
        
        
        # bfs from each water        
        def bfs(queue):
            currLevel = 0
            levelCounter = len(queue)
            
            while queue:
                point = queue.popleft()
                currI = point[0]
                currJ = point[1]
                
                for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nextI = currI + i
                    nextJ = currJ + j

                    if 0 <= nextI < m and 0 <= nextJ < n and isWater[nextI][nextJ] == 'L':
                        isWater[nextI][nextJ] = currLevel + 1
                        queue.append((nextI, nextJ))
                        
                levelCounter -= 1
                if levelCounter == 0:
                    currLevel += 1
                    levelCounter = len(queue)
            
        
        bfs(waters)
        return isWater