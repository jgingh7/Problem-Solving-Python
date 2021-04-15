# https://leetcode.com/problems/find-median-from-data-stream/solution/
# Time: addNum: O(3logn) -> O(logn) - push, pop, push
#       findMedian: O(1)
# Space: O(n)

from heapq import *

class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num)) #push negative num to small(max heap), and pop the max of small, and push to large
        else:
            heappush(self.small, -heappushpop(self.large, num)) #push num to large(min heap), and pop the min of large, and push to small
            

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])