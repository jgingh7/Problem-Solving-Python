# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/794/
# Time: complex
# Space: complex

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.backtrack("", 0, 0, ans, n)
        return ans
    
    def backtrack(self, combi: str, start: int, end: int, ans: str, n: int):
        if len(combi) == n * 2:
            ans.append(combi)
            return
        
        if start < n:
            self.backtrack(combi + "(", start + 1, end, ans, n)
        if end < start:
            self.backtrack(combi + ")", start, end + 1, ans, n)