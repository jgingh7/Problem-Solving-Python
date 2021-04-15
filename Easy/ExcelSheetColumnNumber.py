# https://leetcode.com/problems/excel-sheet-column-number/submissions/
# Time: O(n)
# Space: O(1)

class Solution:
    def titleToNumber(self, s: str) -> int:
        stringLen = len(s)
        ans = 0
        
        for i in range(stringLen):
            ans += (ord(s[stringLen - i - 1]) - ord("A") + 1) * (26 ** i)
        
        return ans


#         if stringLen == 1:
#             return(ord(s) - ord("A") + 1)
            
#         if stringLen == 2:
#             return (ord(s[0]) - ord("A") + 1) * 26 + (ord(s[1]) - ord("A") + 1)
            
#         if stringLen == 3:
#             return (ord(s[0]) - ord("A") + 1) * 26 * 26 + (ord(s[1]) - ord("A") + 1) * 26 + (ord(s[2]) - ord("A") + 1)