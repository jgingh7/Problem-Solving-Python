# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
# Time: O(n + 1)
# Space: O(n + 1)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        dp = [None] * (n + 1) #make n + 1 of them because you want to have a value for dp[n]
        dp[0] = dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]


# if 1
# 1

# if 2
# 1 1 
# 2

# if 3
# 1 1 1
# 2 1
# 1 2

# if 4
# 1 1 1 1
# 1 1 2
# 1 2 1
# 2 1 1
# 2 2

