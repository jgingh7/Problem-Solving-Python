#https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/
#Time: O(len(nums))
#Space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = maxSum = nums[0]
        for num in nums[1:]:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)

        return maxSum