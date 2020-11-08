# https://leetcode.com/problems/minimum-path-sum/
# Time: O(m * n)
# Space: O(1)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        y = len(grid)
        x = len(grid[0])
        
        for i in range(1, x):
            grid[0][i] += grid[0][i - 1]
            
        for j in range(1, y):
            grid[j][0] += grid[j - 1][0]
        
        for i in range(1, y):
            for j in range(1, x):
                grid[i][j] = min(grid[i][j - 1] + grid[i][j], grid[i - 1][j] + grid[i][j])
                
        return grid[-1][-1]