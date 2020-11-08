# https://leetcode.com/problems/longest-palindromic-substring/
# Time: O(n^2)
# Space: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
                         #odd                     #even
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)

        return res
 
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]