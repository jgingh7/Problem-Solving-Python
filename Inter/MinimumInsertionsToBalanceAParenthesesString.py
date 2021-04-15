# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
# Time: O(n)
# Space: O(1)

# res represents the number of left/right parentheses already added.
# right represents the number of right parentheses needed.

class Solution:
    def minInsertions(self, s: str) -> int:
        res = right = 0
        
        for parenthesis in s:
            if parenthesis == '(':
                if right % 2 == 1: #if one more right is needed, delete 1 from right and add 1 onto res
                    right -= 1
                    res += 1
                right += 2
                
            elif parenthesis == ')':
                right -= 1
                if right == -1: #right ever reaches -1, add left parenthesis before it, and add 2 to right to compensate for the new left
                    res += 1
                    right += 2
                    
        return right + res