# https://leetcode.com/problems/unique-paths-ii/
# Time: O(n * m)
# Space: O(1)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    obstacleGrid[0][0] = 1
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                elif j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                    
        return obstacleGrid[-1][-1]