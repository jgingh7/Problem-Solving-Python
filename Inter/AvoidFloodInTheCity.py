# https://leetcode.com/problems/avoid-flood-in-the-city/
# Time: O(nlogn) - O(n) for the for loop and O(logn) for heap insert and pop
# Space: O(n)

from collections import deque, defaultdict
import heapq

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakeNDays = defaultdict(deque)
        for day, lake in enumerate(rains):
            lakeNDays[lake].append(day)
        
        ans = []
        closest = []  # "closest" minheap 
        for day, lake in enumerate(rains):
            if closest and closest[0] == day: # if the closest day to rain is today, it means there were no dry days in between to pop out "day",
                return [] # so return "impossible"
            
            if lake == 0: # if dry day,
                if not closest: # and if there are no lakes that are filled, append 1
                    ans.append(1) 
                    continue
                    
                nextRainDay = heapq.heappop(closest) #pop the day that will rain in the closest future,
                ans.append(rains[nextRainDay]) #and dry that rainy day's lake
                
            else: # if not a dry day,
                ans.append(-1) # append -1

                currLakeDays = lakeNDays[lake] # get queue of days of "lake"
                currLakeDays.popleft() # pop the oldest
                
                if currLakeDays: # if there is a future day that will rain on "lake", append day value to closest
                    heapq.heappush(closest, currLakeDays[0])

                
        return ans