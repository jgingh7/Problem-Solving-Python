# https://leetcode.com/problems/remove-k-digits/
# Time: O(len(num))
# Space: O(len(num))

from collections import deque

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:    
        stack = deque()
        for digit in num:
            while stack and k and stack[-1] > digit: #this keeps the answer to keep an increasing in digits until k is used up
                k -= 1
                stack.pop()
            stack.append(digit)
        
        if k: # this part deals with "1123 k=2" where k is not depleted because towards the end the digits keep increasing
            for i in range(k):
                stack.pop()
        
        return "".join(stack).lstrip("0") or "0" # if "".join(stack).lstrip("0") part is "", return "0"