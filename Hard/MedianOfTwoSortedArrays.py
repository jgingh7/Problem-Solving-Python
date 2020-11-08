# https://leetcode.com/explore/interview/card/top-interview-questions-hard/120/sorting-and-searching/859/
# Time: O(m+n) iterate through half of m+n(totalLen)
# Space: O(1)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getMedian(nums: List[int], numsLen: int) -> int:
            mid = numsLen // 2
            if numsLen % 2 == 0:
                return (nums[mid] + nums[mid - 1]) / 2
            if numsLen % 2 == 1:
                return nums[mid]
            
        m = len(nums1)
        n = len(nums2)
        
        if not m:
            return getMedian(nums2, n)
        if not n:
            return getMedian(nums1, m)
        
        totalLen = m + n
        mid = totalLen // 2
        
        i, j, counter = 0, 0, 0
        final, oneBeforeFinal = 0, 0
        
        while counter <= mid:
            if i >= m:
                oneBeforeFinal, final = final, nums2[j]
                j += 1
            elif j >= n:
                oneBeforeFinal, final = final, nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                oneBeforeFinal, final = final, nums1[i]
                i += 1
            else: # nums1[i] >= nums2[j]:
                oneBeforeFinal, final = final, nums2[j]
                j += 1
            counter += 1       
        
        
        if totalLen % 2 == 0:
            return (final + oneBeforeFinal) / 2
        if totalLen % 2 == 1:
            return final
