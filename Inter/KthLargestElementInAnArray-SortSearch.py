#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/800/
#Time: O(n)
#Space: O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]

#Quick Selection
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         pos = self.partition(nums, 0, len(nums)-1)
#         if pos > len(nums) - k:
#             return self.findKthLargest(nums[:pos], k-(len(nums)-pos))
#         elif pos < len(nums) - k:
#             return self.findKthLargest(nums[pos+1:], k)
#         else:
#             return nums[pos]
 
#     # partitioning O(n)
#     def partition(self, nums: List[int], l: int, r: int) -> int:
#         pivot = nums[r]
#         lo = l 
#         for i in range(l, r):
#             if nums[i] < pivot:
#                 nums[i], nums[lo] = nums[lo], nums[i]
#                 lo += 1
#         nums[lo], nums[r] = nums[r], nums[lo]
#         return lo