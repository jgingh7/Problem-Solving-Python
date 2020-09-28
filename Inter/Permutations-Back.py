#https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/
# Time: complex
# Space: O(n) - recursio stack


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack([], nums, ans)
        return ans
    
    def backtrack(self, path: List[int], nums: List[int], ans: List[List[int]]):
        if not nums:
            ans.append(path)
        else:
            for num in nums:
                numsCopy = nums.copy()
                numsCopy.remove(num)
                self.backtrack(path + [num], numsCopy, ans)