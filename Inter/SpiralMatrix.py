# https://leetcode.com/problems/spiral-matrix/
# Time: O(mn)
# Space: O(mn)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        ans = []
        
        for i in range(m):
            for j in range(i, n - i):
                if matrix[i][j] == '#':
                    return ans
                ans.append(matrix[i][j])
                matrix[i][j] = '#'
                
            for k in range(i + 1, m - i):
                if matrix[k][n - i - 1] == '#':
                    return ans
                ans.append(matrix[k][n - i - 1])
                matrix[k][n - i - 1] = '#'
                
            for j in reversed(range(i, n - i - 1)):
                if matrix[m - i - 1][j] == '#':
                    return ans
                ans.append(matrix[m - i - 1][j])
                matrix[m - i - 1][j] = '#'
            
            for k in reversed(range(i + 1, m - i - 1)):
                if matrix[k][i] == '#':
                    return ans
                ans.append(matrix[k][i])
                matrix[k][i] = '#'
        
        return ans