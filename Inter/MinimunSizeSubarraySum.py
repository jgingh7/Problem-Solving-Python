# https://leetcode.com/problems/minimum-size-subarray-sum/
# Time: O(n)
# Space: O(1)

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        total = left = 0
        res = len(nums) + 1
        for right, num in enumerate(nums):
            total += num
            while total >= s:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
                
        return res if res <= len(nums) else 0