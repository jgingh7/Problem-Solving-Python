#https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/
#Time: O(mn)
#Space: O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colLen = len(matrix)
        rowLen = len(matrix[0])
        rowOneisZero = False
        for element in matrix[0]:
            if element == 0:
                rowOneisZero = True
                
        for i in range(1, colLen):
            for j in range(rowLen):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, colLen):
            if matrix[i][0] == 0:
                for j in range(rowLen):
                    matrix[i][j] = 0
                    
        for j in range(rowLen):
            if matrix[0][j] == 0:
                for i in range(colLen):
                    matrix[i][j] = 0
        
        if rowOneisZero:
            for j in range(rowLen):
                matrix[0][j] = 0
                    