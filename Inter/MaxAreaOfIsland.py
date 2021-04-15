# https://leetcode.com/problems/max-area-of-island/
# Time: O(mn)
# Space: O(mn) - recursion stack


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    candidate = self.dfs(grid, i, j, 0)
                    ans = max(ans, candidate)
        
        return ans
    
    
    def dfs(self, grid, i, j, candidate):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 0 # candidate also works, but candidate will always be 0 here
        
        grid[i][j] = 0
        
        candidate = 1 + \
        self.dfs(grid, i + 1, j, candidate) + \
        self.dfs(grid, i - 1, j, candidate) + \
        self.dfs(grid, i, j + 1, candidate) + \
        self.dfs(grid, i, j - 1, candidate)
        
        return candidate