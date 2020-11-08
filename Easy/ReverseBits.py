# https://leetcode.com/problems/reverse-bits/submissions/
# Time: O(1)
# Sapce: O(1)s

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans <<= 1
            ans += n & 1
            n >>= 1
        return ans