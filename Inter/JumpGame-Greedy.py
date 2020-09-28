#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/
#Time: O(n)
#Space: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastIdx = len(nums) - 1
        goodIdx = lastIdx
        for i in range(lastIdx - 1, -1, -1): #iterating backwards
            if i + nums[i] >= goodIdx: #if currentIdx + the value of currentIdx is big enough to reach goodIdx, goodIdx = i
                goodIdx = i
                
        return goodIdx == 0