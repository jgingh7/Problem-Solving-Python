# https://leetcode.com/problems/132-pattern/
# Time: O(n)
# Space: O(n)

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:            
        numsLen = len(nums)
        
        if numsLen <= 2:
            return False
        
        stack = []
        
        # make an array called minimum that has the minimum value from each index to the start
        minimum = [nums[0]]
        for i in range(1, numsLen):
            minimum.append(min(minimum[i - 1], nums[i])) 
               
        for i in reversed(range(0, numsLen)):
            if nums[i] > minimum[i]: #stack has numbers that are on the right that are bigger than current minimum value
                while stack and stack[-1] <= minimum[i]: #remove numbers that are on stack
                                                         #smaller than or euqal to current minimum value
                    stack.pop()
                if stack and stack[-1] < nums[i]: #the outer if states that current value is bigger than current minimum value
                                                  #which means that is a value on the left
                                                  #that is smaller than current minimum value
                                                  #Here, we return True if the stack's number is smaller than current value
                    return True
                stack.append(nums[i])
        
            
        return False