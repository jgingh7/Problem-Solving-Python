#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/
#Time: O(nlogn)
#Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        
        if len(nums) <= 1: #if the nums' length is less than or equal to 1, just return the nums' length
            return len(nums)
        
        dp.append(nums[0]) #append first num
        for num in nums:
            if num > dp[-1]: #if num is bigger than last element of dp, append num
                dp.append(num)
            else: #if not, binary search the dp for the smallest number that is larger than num, and change that number to num
                  #this keeps the future subsequence to be able to append with smaller number
                  #which makes it possible for longer subsequence to be made, if exists
                l = 0
                r = len(dp) - 1
                while l < r:
                    mid = l + ((r - l) // 2)
                    if dp[mid] < num:
                        l = mid + 1
                    elif dp[mid] >= num:
                        r = mid
                dp[r] = num
                
        return len(dp)