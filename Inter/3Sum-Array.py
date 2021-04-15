#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
#Time: O(n^2)
#Space: O(len(nums) C 3) - if count the ans

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsLen = len(nums)
        if numsLen < 3:
            return []
        
        ans = []
        nums.sort()
        
        for i in range(numsLen - 2):
            if i > 0 and nums[i] == nums[i - 1]: # skip same numbers
                continue
            l, r = i + 1, numsLen - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1 
                elif s > 0:
                    r -= 1
                else:
                    ans.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]: # skip same numbers
                        l += 1
                    while l < r and nums[r] == nums[r - 1]: # skip same numbers
                        r -= 1
                    l += 1
                    r -= 1
                    
        for i in range(len(ans)):
            ans[i] = list(ans[i])
            
        return ans   