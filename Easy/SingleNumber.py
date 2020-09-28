#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
#Time: O(len(nums))
#Space: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i # a xor 0 = a, a xor a = 0
        return a