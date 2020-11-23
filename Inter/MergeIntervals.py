# https://leetcode.com/problems/merge-intervals/
# Time: O(nlogn)
# Space: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def getZero(a: List[int]):
            return a[0]
        
        intervals.sort(key = getZero)
        
        ans = []
        for interval in intervals:
            if ans and interval[0] <= ans[-1][1]:
                if interval[1] > ans[-1][1]:
                    ans[-1][1] = interval[1]
            else:
                ans.append(interval)

        return ans
        
    