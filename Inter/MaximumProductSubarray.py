# https://leetcode.com/problems/maximum-product-subarray/
# Time: O(n)
# Space: O(1)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        currMin = currMax = res = nums[0]
        
        #need to keep track of currMax to get the maximum product,
        #but also currMin to get maximum product when curr num is negative.
        #also, if nums is the start of new subarray, make it currMax or currMin
        for i in range(1, len(nums)):
            currMax, currMin = max(currMax * nums[i], currMin * nums[i], nums[i]), \
                                min(currMax * nums[i], currMin * nums[i], nums[i])
            res = max(res, currMax)
            
        return res