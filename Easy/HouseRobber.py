# https://leetcode.com/problems/house-robber/
# Time: O(n)
# Space: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numsLen = len(nums)
        
        dp = [0] * numsLen
        
        dp[0] = nums[0]        
        if numsLen == 1:
            return dp[0]
        
        dp[1] = max(nums[0], nums[1])
        if numsLen == 2:
            return dp[1]
        
        for i in range(2, numsLen):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            
        return dp[-1]