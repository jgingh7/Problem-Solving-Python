#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/
#Time: O(n^2)
#Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [1] * len(nums) # if length 1, at least the ans is 1
        maxans = 1
        
        for i in range(1, len(dp)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    
            maxans = max(maxans, dp[i])
        
        return maxans

# THERE IS A NLOGN SOLUTION WHICH I CANNOT UNDERSTAND