# https://leetcode.com/problems/container-with-most-water/
# Time: O(n)
# Space: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            maxWater = max(maxWater, min(height[l], height[r]) * (r - l))
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        
        return maxWater