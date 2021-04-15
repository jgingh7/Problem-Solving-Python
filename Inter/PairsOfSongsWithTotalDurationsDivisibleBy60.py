# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# Time: O(n)
# Space: O(n)

from collections import Counter

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [x % 60 for x in time]        
        timeCounter = Counter(time)
        
        ans = 0
        
        for time in timeCounter:
            if time == 0 or time == 30:
                ans += (timeCounter[time] * (timeCounter[time] - 1)) // 2
            else:
                pairTime = 60 - time
                if pairTime in timeCounter and timeCounter[pairTime] > 0:
                    ans += timeCounter[time] * timeCounter[pairTime]
                    timeCounter[time] = 0
                    timeCounter[pairTime] = 0
        
        return ans