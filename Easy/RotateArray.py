#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
#Time: O(len(nums))
#Space: O(1) - Constant extra space is used

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n #incase k >= len(nums)
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                nextIdx = (current + k) % n #% n, incase nextIdx >= len(nums)
                nums[nextIdx], prev = prev, nums[nextIdx]
                current = nextIdx
                count += 1
                
                if start == current: #when land on same start position, break and add 1 to start
                    break
            start += 1