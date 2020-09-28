#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/801/
#Time: O(logn)
#Space: O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else: #nums[mid] > nums[mid + 1]
                r = mid
        return r