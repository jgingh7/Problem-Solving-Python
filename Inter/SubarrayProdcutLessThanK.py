# https://leetcode.com/problems/subarray-product-less-than-k/
# Time: O(n)
# Space: O(1)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k: #if prod is bigger or equal to k, divide the leftmost until we get less than k
                prod /= nums[left]
                left += 1
            ans += right - left + 1 #add the idx difference to add the combianations made by adding right idx's value

        return ans