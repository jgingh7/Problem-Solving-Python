# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
# Time: O(elements of grid) - iterate through all elements in grid
# Space: O(max(maxRowIdx, maxColIdx))

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        
        maxRowIdx = len(grid)
        maxColIdx = len(grid[0])

        skylineTB = grid[0].copy()
        for row in grid:
            for j in range(maxColIdx):
                skylineTB[j] = max(skylineTB[j], row[j])
        
        skylineLR = []
        for row in grid:
            skylineLR.append(max(row))
        

        for i in range(maxRowIdx):
            for j in range(maxColIdx):
                toVal = min(skylineTB[j], skylineLR[i])
                ans += toVal - grid[i][j]
        
        return ans