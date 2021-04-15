# https://leetcode.com/problems/rotate-image/
# Time: O(n^2)
# Space: O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        #transpose
        jStart = 1
        for i in range(n):
            j = jStart
            while j < n:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j += 1
            jStart += 1
                    
        #reverse
        for i in range(n):
            for j in range(int(n/2)):
                matrix[i][j], matrix[i][-1 - j] = matrix[i][-1 - j], matrix[i][j]