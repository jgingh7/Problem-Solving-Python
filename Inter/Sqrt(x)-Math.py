#https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/819/
#Time: O(logn)
#Space: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (r + l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else: # mid * mid < x
                l = mid + 1