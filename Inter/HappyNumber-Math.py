#https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/815/
#Time: O(n*m)
#Space: O(n)

class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        
        while n != 1: #O(n)
            if n in mem:
                return False #if the same number appears, we are in a continuous loop
            
            mem.add(n)
            
            n = sum([int(x) ** 2 for x in str(n)]) #O(m)
        return True # if n is 1 or n reaches 1, return True