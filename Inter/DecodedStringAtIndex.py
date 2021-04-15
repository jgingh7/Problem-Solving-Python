# https://leetcode.com/problems/decoded-string-at-index/
# Time: O(len(S))
# Space: O(1)

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        # Find size = length of decoded string
        for char in S:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1

                
        for char in reversed(S):
            
            # this does not work on situations where K is the length of decoded string  ex) "a23" 6
            # if K == size and char.isalpha(): 
            #     return char

            K %= size # if K < size, this results K
            
                      # elif K == size, K == 0
                      #   this means that size was decreased enough to meet K
                    
                      # else, currDecodedString[new K] == nonBrokenDownDecodedString[before K]
                      # nonBroken is the String that you had before doing /= int(char)
                      # *here decoded string does not exist, it only exists in the form of size.
            
            if K == 0 and char.isalpha():
                return char
            
            if char.isdigit():
                size /= int(char) # break down the deoded string into single string that was reapted by int(char)
            else:
                size -= 1 # decrement size by 1, until size is decreased to meet K or until a new digit is seen