#https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/820/
#Time:O(1)
#Space:O(1)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = dividend / divisor
        if ans >= (2 ** 31) or ans < -(2 ** 31):
            return (2 ** 31) - 1
        
        return int(ans)

# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         ans = dividend / divisor
#         # 2147483648
#         if ans >= (2 ** 31) or ans < -(2 ** 31):
#             return (2 ** 31) - 1
#         if ans >= 0:
#             return dividend // divisor
#         if ans < 0:
#             return math.ceil(ans)