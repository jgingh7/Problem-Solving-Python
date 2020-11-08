# https://leetcode.com/problems/container-with-most-water/submissions/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(height) - 1
        
        while (l < r):
            maxArea = max(maxArea, min(height[l], height[r]) * (r - l))
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
                
        return maxArea