#https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/
#Time: O(n * 2^n)
#Space: O(n * 2^n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(sorted(nums), 0, [], ans)
        return ans
    
    def backtrack(self, nums: List[int], start: int, path: List[int], ans: List[List[int]]):
        ans.append(path)
        for i in range(start, len(nums)):
            self.backtrack(nums, i + 1, path + [nums[i]], ans)
        # [] 1 12 123 13 2 23 3

