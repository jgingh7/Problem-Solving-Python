# https://leetcode.com/problems/132-pattern/
# Time: O(n)
# Space: O(n)

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:            
        numsLen = len(nums)
        
        if numsLen <= 2:
            return False
        
        # make an array called minimum that has the minimum value from each index to the start
        minimum = [nums[0]]
        for i in range(1, numsLen):
            minimum.append(min(minimum[i - 1], nums[i])) 

        stack = []
        for i in reversed(range(numsLen)):
            if nums[i] > minimum[i]: #stack has numbers that are on the right that are bigger than current minimum value
                while stack and stack[-1] <= minimum[i]: # Remove numbers that are on stack smaller than or euqal to current minimum value
                                                         # This way the stack reamins sorted (bottom with largest).

                                                         # Assume the stack is sorted, and you pop out the numbers smaller than current min.
                                                         # (this allows stacked number(if currNum is stacked) to be the smallest number on the stack that is larger than current min)
                                                         # If stack[top] is smaller than current number, return True (currmin < stack[top] < currNum)
                                                         # else, stack[top] is larger than or equal to current number, and the current number is stacked.
                                                         # Since "stacked number <= stack[top]" the stack remains sorted.
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        
            
        return False