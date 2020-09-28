#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/804/
#Time: O(log n)
#Space: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find pivot
        #binary search on either side
        l, r, pivot = 0, len(nums) - 1, len(nums) - 1
        while l < r: #check
            mid = (r + l) // 2
            if nums[mid] > nums[mid + 1]:
                pivot = mid
                break
            else: #nums[mid] < nums[mid + 1]:
                if nums[0] <= nums[mid]:
                    l = mid + 1
                else: #nums[0] > nums[mid]
                    r = mid
        
        if nums[0] == target:
            return 0
        elif nums[0] < target:
            return self.searchAns(0, pivot, nums, target)
        else: #nums[0] > target:
            return self.searchAns(pivot + 1, len(nums) - 1, nums, target)
            
    def searchAns(self, l: int, r: int, nums: List[int], target: int) -> int:
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
        