#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/
#Time: O(log n)
#Space: O(n) for the answer

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #find left
        #find right
        #merge
        start = self.findStart(nums, target)
        end = self.findEnd(nums, target)
        return [start, end]
    
    def findStart(self, nums: List[int], target: int) -> int:
        l, r, ans = 0, len(nums) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid
        return ans
    
    def findEnd(self, nums: List[int], target: int) -> int:
        l, r, ans = 0, len(nums) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                l = mid + 1
                ans = mid
        return ans