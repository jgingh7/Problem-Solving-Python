# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# Time: O(m*n log(sqrt(m^2 + n^2))) or O(k log(sqrt(m^2 + n^2)))
# Space: O(m*n) - visited

import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        ans = []
        candid = [(nums1[0] + nums2[0], (0, 0))] # elements are in the form of "sum, (rowIdx, colIdx)"
        visited = set()
        
        while len(ans) < k and candid:
            _, (i, j) = heapq.heappop(candid)
            ans.append([nums1[i], nums2[j]])
            
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                    heapq.heappush(candid, (nums1[i] + nums2[j + 1], (i, j + 1)))
                    visited.add((i, j + 1))
                    
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                    heapq.heappush(candid, (nums1[i + 1] + nums2[j], (i + 1, j)))
                    visited.add((i + 1, j))
                    
        return ans