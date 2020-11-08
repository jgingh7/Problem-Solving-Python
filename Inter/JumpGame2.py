# https://leetcode.com/problems/jump-game-ii/submissions/

class Solution: #BFS solution #for every while iteration, check all the elements
                                                         # to get the next end as the maximum possible reachable position
                                                         # and start and 1 above current end.   
    def jump(self, nums: List[int]) -> int:
        lastIdx, start, end, step = len(nums) - 1, 0, 0, 0
        while end < lastIdx:
            step += 1
            nextEnd = end + 1
            for i in range (start, end + 1):
                if i + nums[i] >= lastIdx:
                    return step
                nextEnd = max(nextEnd, i + nums[i]) # maximum reachable position
            start, end = end + 1, nextEnd
        
        return step #this is reached only when the while loop is ended with the condition, which is when len(nums) == 0
                    #other cases are all returned from if statement in the middle