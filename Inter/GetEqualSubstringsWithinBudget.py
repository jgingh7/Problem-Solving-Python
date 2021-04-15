# https://leetcode.com/problems/get-equal-substrings-within-budget/
# Time O(n)
# Space O(1)

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = 0
        for j in range(len(s)):
            maxCost -= abs(ord(s[j]) - ord(t[j]))
            if maxCost < 0: # if maxCost is less than 0, increment i
                            # this makes the maxLength to be preserved since i is incremented after j is incremented 
                maxCost += abs(ord(s[i]) - ord(t[i]))
                i += 1
        
        return j - i + 1