#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/
#Time: O(m * n)
#Space: O(m * n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for x in range(m)] for x in range(n)]        
        
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
                
        return grid[-1][-1]