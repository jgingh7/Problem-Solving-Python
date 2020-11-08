# https://leetcode.com/problems/maximum-product-of-three-numbers/
# Time: O(n)
# Space: O(1)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        pos = heapq.nlargest(3, nums)
        neg = heapq.nsmallest(3, nums)
        return max(pos[0] * pos[1] * pos[2], neg[0] * neg[1] * pos[0])