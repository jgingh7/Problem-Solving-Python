# https://leetcode.com/problems/3sum-closest/
# Time: O(n^2)
# Space: O(1)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        numsLen = len(nums)
        ansDiff = float('inf'), float('inf'), float('inf'), float('inf')

        
        nums.sort()
        for i in range(numsLen):
            l = i + 1
            r = numsLen - 1
            
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if abs(sum - target) < ansDiff[0]:
                    ansDiff = abs(sum - target), nums[i], nums[l], nums[r]
                    
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    break
                    
            if ansDiff[0] == 0:
                break
                               
        return ansDiff[1] + ansDiff[2] + ansDiff[3]