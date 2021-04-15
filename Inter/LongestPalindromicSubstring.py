# https://leetcode.com/problems/longest-palindromic-substring/
# Time: O(n^2)
# Space: O(n)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ansIdxes = 0, 0
        for i in range(len(s)):
                                     #odd                     #even
            ansIdxes = max(self.helper(s, i, i), self.helper(s, i, i + 1), ansIdxes, key=lambda x: x[1] - x[0])
        return s[ansIdxes[0]:ansIdxes[1]]
    
    
    def helper(self, s: str, l: int, r: int) -> (int, int):
        while l >=0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            
        return l+1, r
            
        