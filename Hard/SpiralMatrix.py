# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/828/
# Time: O(mn)
# Space: O(n) if count the answer

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiralCoords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2: # put this in to not execute below 
                                    # in situations where only 1 row or 1 column exists
                                    # if executed, double counting occurs
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix:
            return []
        
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiralCoords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            # to the next inner rectanlge
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return ans