#https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/818/
#Time: O(logn)
#Space: O(1)

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         return x ** n
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)

# n == 10
# x^10 == x^5 * x^5 == (x^2)^5

# n == 11
# x^11 == x * x^5 * x^5