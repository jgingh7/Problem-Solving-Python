# https://leetcode.com/problems/longest-arithmetic-subsequence/submissions/
# Time: O(n^2)
# Space: O(n^2)

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1 #default is 1, because a subsequence with i and j is at least 2
        
        return max(dp.values())