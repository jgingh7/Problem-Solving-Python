# https://leetcode.com/problems/valid-parentheses/
# Time: O(length of s)
# Space: O(length of s) - stack space

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mapping = {")":"(", "}":"{", "]":"["}
        
        for element in s:
            if element in mapping:
                pair = stack.pop() if stack else '#'
                if pair != mapping[element]:
                    return False
            else:
                stack.append(element)
                
        return not stack # the stack has to be empty