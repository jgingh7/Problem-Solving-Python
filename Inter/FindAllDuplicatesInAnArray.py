# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Time: O(n)
# Space: O(1)

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
                
        return res