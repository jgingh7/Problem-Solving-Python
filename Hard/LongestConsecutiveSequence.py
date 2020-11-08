# https://leetcode.com/problems/longest-consecutive-sequence/
# Time O(n) - O(n + n) because iterate through n, and while loop touches just n elements since it is blocked by "if num - 1 ..."
# Space O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        numsSet = set(nums)
        
        for num in numsSet:
            if num - 1 not in numsSet: # if num is the start of the consecutive sequence, start counting length
                currSeqLen = 1
                
                while num + 1 in numsSet: # while there is a number 1 above, keep iterating
                    num += 1
                    currSeqLen += 1
                    
                ans = max(ans, currSeqLen) # after getting currSeqLen, compare it to ans
                
        return ans