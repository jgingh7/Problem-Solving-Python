# https://leetcode.com/problems/minimum-size-subarray-sum/
# Time: O(n)
# Space: O(1)

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = 0
        minLen = float('inf')
        
        for r in range(len(nums)):
            s -= nums[r]
            while s <= 0:
                minLen = min(minLen, r - l + 1)
                s += nums[l]
                l += 1
                          
        return 0 if minLen == float('inf') else minLen