#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/
#Time: O(n log n)
#Space: O(n)

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
              
        counterTup = []
        for key, val in counter.items():
            counterTup.append((val, key))
        
        heapq._heapify_max(counterTup)
        
        ans = []
        for i in range(k):
            ans.append(heapq._heappop_max(counterTup)[1])
            
        return ans