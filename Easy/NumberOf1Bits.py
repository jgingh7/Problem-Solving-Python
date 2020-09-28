# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/
# Time: O(n bit length)
# Space: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            n &= n - 1 #bitwise AND operation
            c += 1
        return c
    
               
        # 1111 & 1110 => 1110
        # 1110 & 1101 => 1100
        # 1100 & 1001 => 1000
        # 1000 & 0111 => 0000
        
        # 1010 & 1001 => 1000
        # 1000 & 0111 => 0000