# https://leetcode.com/problems/largest-divisible-subset/
# Time: O(n^2)
# Space: O(n^2)

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        numsLen = len(nums)
        
        dp = []
        maxLen = 0
        ans = []
        
        for i in range(numsLen):
            addedNum = nums[i]
            if i == 0: # if first number of sorted nums, just add itself to the dp
                dp.append([addedNum])
                maxLen += 1
                ans = dp[0]
            else:
                possible = []
                for j in reversed(range(i)):
                    checkedNum = nums[j]
                    if addedNum % checkedNum == 0: # if the number to be added meets the condition,
                                                   # check which array in dp can be appended and return the largest subset
                        currCheckedArr = dp[j] + [addedNum]
                        if len(currCheckedArr) == maxLen + 1: # if appending makes a length 1 larger than max length,
                                                              # put this in dp and update ans
                            dp.append(currCheckedArr)
                            maxLen += 1
                            ans = dp[i]
                            break
                        else: # if not, update possible array to be added in dp
                            possible = max(possible, currCheckedArr, key=len)                        
                    if j == 0:
                        if not possible: # in the end, if the number does not meet condition with any array in dp, just added itself
                            dp.append([addedNum])
                        else: # else, up possible array in dp
                            dp.append(possible)
                        
        return ans
