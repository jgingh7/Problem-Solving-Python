#https://leetcode.com/problems/set-matrix-zeroes/
#Time: O(mn)
#Space: O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        maxRowIdx = len(matrix)
        maxColIdx = len(matrix[0])
        
        # 1.
        # check if the first row has zero
        firstRowHasZero = False
        for j in range(0, maxColIdx):
            if matrix[0][j] == 0:
                firstRowHasZero = True
        
        # check if the first column has zero
        firstColHasZero = False
        for i in range(0, maxRowIdx):
            if matrix[i][0] == 0:
                firstColHasZero = True
        
        # 2. 
        # just for the values other than the first row and column,
        # check the value, and if 0, use the first row and column as flag and set the as 0
        for i in range(1, maxRowIdx):
            for j in range(1, maxColIdx):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0        
                
        # 3.
        # check the first column for 0s and if 0, make all values in that row as 0
        for i in range(1, maxRowIdx):
            if matrix[i][0] == 0:
                for j in range(1, maxColIdx):
                    matrix[i][j] = 0
                    
        # check the first row for 0s and if 0, make all values in that column as 0
        for j in range(1, maxColIdx):
            if matrix[0][j] == 0:
                for i in range(1, maxRowIdx):
                    matrix[i][j] = 0
        
        # 4.
        # if the first row has 0, make all the values in the first row as 0
        if firstRowHasZero:
            for j in range(0, maxColIdx):
                matrix[0][j] = 0
                
        # if the first column has 0, make all the values in the first column as 0
        if firstColHasZero:
            for i in range(0, maxRowIdx):
                matrix[i][0] = 0
                    
