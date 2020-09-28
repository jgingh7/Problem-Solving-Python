#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/806/
#Time: O(m+n)
#Space: O(1)

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else: # target > matrix[i][j]
                i += 1
        return False