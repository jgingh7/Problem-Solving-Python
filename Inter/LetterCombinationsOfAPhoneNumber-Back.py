#https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/793/
#Time: O(3^n + 4^m)
#Space: O(3^n + 4^m) if count the ans
class Solution:
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if digits:
            self.backtrack("", digits, ans)
        return ans
    
    def backtrack(self, combi: str, digits: str, ans: List[str]):
        if not digits:
            ans.append(combi)
        else:
            curr = self.phone[digits[0]]
            for i in range(len(curr)):
                self.backtrack(combi + curr[i], digits[1:], ans)