# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
# Time: O(nlogn)
# Space: O(n)

from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arrDict = Counter(arr)
        sortedArr = sorted(arr, key = lambda x:(arrDict[x],x)) #sort by c[x], and if same, sort by x
        return len(set(sortedArr[k:]))