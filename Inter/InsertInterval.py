# https://leetcode.com/problems/insert-interval/
# Time: O(n)
# Space: O(n)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for i in intervals:
            #adding of non-overlapping intervals smaller than newInterval
            if i[1] < s:
                left += i,
            #adding of non-overlapping intervals larger than newInterval
            elif i[0] > e:
                right += i,
            #update of overlapping intervals
            else:
                s = min(s, i[0])
                e = max(e, i[1])
                
        return left + [[s, e]] + right