#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
#Time: O(len(s))
#Space: O(len(usedChar))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = ans = 0
        usedChar = {}
        for i, char in enumerate(s):
            # if new just put i as char's dictionary value

            # if not new, update ans
            # and if char's original index + 1 is larger than l, update l to char's original index + 1
            # then update char's dictionary value as i
            if char in usedChar:
                ans = max(ans, i - l)
                if usedChar[char] + 1 > l:
                    l = usedChar[char] + 1
            usedChar[char] = i
            
        # update ans with the most updated l value
        ans = max(ans, len(s) - l)
        
        return ans

        