# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Time: O(n^2)
# Space: O(n) because sqrt(2 * n^2)

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        level = [(0, 0)]
                
        res = 0
        while level:
            nextLevel = []
            res += 1
            for currI, currJ in level:
                if currI == n - 1 and currJ == n - 1:
                    return res

                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    nextI = currI + i
                    nextJ = currJ + j

                    if 0 <= nextI < n and 0 <= nextJ < n and grid[nextI][nextJ] != 1:
                        nextLevel.append((nextI, nextJ))
                        grid[nextI][nextJ] = 1

            level = nextLevel
        return -1

