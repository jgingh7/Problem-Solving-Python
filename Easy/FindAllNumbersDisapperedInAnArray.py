# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Time: O(n)
# Space: O(1)


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1

        ans = []
        for i, num in enumerate(nums):
            if num > 0:
                ans.append(i + 1)
                
        return ans