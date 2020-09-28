# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
# Time: O(len(nums))
# Space: O(len(nums) - 1), the dictionary size

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(nums):
            otherNum = target - num
            if otherNum in d:
                return [d[otherNum], idx]
            else:
                d[num] = idx