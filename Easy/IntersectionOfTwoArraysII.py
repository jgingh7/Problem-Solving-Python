# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
# Time: O(max(num1, num2))
# Space: O(min(num1, num2))

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if nums1 > nums2: # to minimize space complexity
            return self.intersect(nums2, nums1)
        
        counts = Counter(nums1)
        res = []
        
        for num in nums2:
            if counts[num] > 0:
                res.append(num)
                counts[num] -= 1
                
        return res