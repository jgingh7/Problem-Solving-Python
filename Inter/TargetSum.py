# https://leetcode.com/problems/target-sum/
# Time: O(2^n)
# Space: O(2^n)


from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        count = defaultdict(int) # all possible sums are defaulted to 0
        count[0] = 1 # 'nums' have 1 <= size <= 20, so least number of steps to reach 0 is 1
                
        for numToFigure in nums:
            nextCount = defaultdict(int)
            for currSubarraySum in count:
                nextCount[currSubarraySum + numToFigure] += count[currSubarraySum]
                nextCount[currSubarraySum - numToFigure] += count[currSubarraySum]
            count = nextCount
            print(count)

        return count[S]