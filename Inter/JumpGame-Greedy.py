#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/
#Time: O(n)
#Space: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in reversed(range(target)): # start iterating one less form the inital target
            if i + nums[i] >= target: # if the sum of currIdx value and currIdx is equal to or bigger than target, target is set to currIdx
                target = i
        
        return target == 0 #target should be zero at the end