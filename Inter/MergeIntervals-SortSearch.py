#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/803/
#Time: O(nlogn) sorting
#Space: probably O(n) for allocating linear space to store a copy of intervals and sort that

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        ans = []
        head = intervals[0]
        
        for i in range(len(intervals)):
            curr = intervals[i]
            if head[1] >= curr[0]:
                head[1] = max(head[1], curr[1])
            else:
                ans.append(head)
                head = curr
                
        ans.append(head)
                
        return ans