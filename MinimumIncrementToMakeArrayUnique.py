# https://leetcode.com/problems/minimum-increment-to-make-array-unique/
# Time: O(nlogn)
# Space: O(1)

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        A.sort()
        ans = 0
        currHeight = A[0]
        for i in range(0, len(A) - 1):
            if A[i] >= A[i + 1]:
                before = A[i + 1]
                A[i + 1] = A[i] + 1
                ans += (A[i + 1] - before)
            
        return ans