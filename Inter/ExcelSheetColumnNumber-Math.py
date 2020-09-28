#https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/817/
#Time: O(n)
#Space: O(1)

class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in s:
            res = res * 26 + ord(i) - ord('A') + 1
            # + 1, because if you think about A, A-A gives 0, so need to add 1
            #The ord() function returns an integer representing the Unicode character.
        return res