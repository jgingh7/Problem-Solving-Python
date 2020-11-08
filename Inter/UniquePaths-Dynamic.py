#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/
#Time: O(m * n)
#Space: O(n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1]