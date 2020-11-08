# https://leetcode.com/problems/power-of-two/
# Time: O(n)
# Space: O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n - 1) == 0 and n != 0

# n & (n - 1) == 0 if power of 2
# ex) 100 (4) & 11 (3) == 0