#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
#Time: O(n^2)
#Space: O(n) - dictionary

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsLen = len(nums)
        if numsLen < 3:
            return []
            
        ans = set()
        
        nums.sort()
        for i in range(numsLen - 2):
            l = i + 1
            r = numsLen - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
                    
        ans = list(ans)
        for i in range(len(ans)):
            ans[i] = list(ans[i])

        return ans
        