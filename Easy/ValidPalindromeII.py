# https://leetcode.com/problems/valid-palindrome-ii/
# Time: O(n)
# Space: O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        count = 0
        
        while l < r:
            if s[l] != s[r]:
                return self.checkPal(s, l + 1, r) or self.checkPal(s, l, r - 1)
            l += 1
            r -= 1
                    
        return True
    
    
    def checkPal(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
                    
        return True