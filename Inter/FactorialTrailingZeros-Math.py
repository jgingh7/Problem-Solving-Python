# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/816/
#Time: O(log(base5)n)
#Space: O(1)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n > 0:
            n = n // 5
            ans += n
        return ans

        # if n < 5 : return 0
        # if n < 25 : return int(n/5)
        # if n < 125 : return int(n/5) + int(n/25)
        # if n < 625 : return int(n/5) + int(n/25) + int(n/125)
        