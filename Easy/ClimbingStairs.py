# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
# Time: O(n + 1)
# Space: O(n + 1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [None] * (n + 1) #make n + 1 of them because you want to have a value for dp[n]
        
        for i in range(n + 1):
            if i == 0:
                dp[i] = 1
            elif i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
                
        return dp[n]


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

