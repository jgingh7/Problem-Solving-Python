#https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/821/
#Time: O(n) : until how much to divide
#Space: O(n)


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator / denominator < 0 else ''
        
        n, remainder = divmod(abs(numerator), abs(denominator))
        #The divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
        
        res = [sign + str(n) + '.']
        stack = []
        repeat = True

        while remainder not in stack:
            if remainder == 0:
                repeat = False
                break
            stack.append(remainder)
            n, remainder = divmod(remainder * 10, abs(denominator))
            res.append(str(n))
                        
        if repeat:
            idx = stack.index(remainder)
            res.insert(idx + 1, '(')
            res.append(')')
        return ''.join(res).rstrip('.')
        # myTuple = ("John", "Peter", "Vicky")
        # x = "#".join(myTuple)
        # print(x) -> John#Peter#Vicky

        # txt = "banana,,,,,ssqqqww....."
        # x = txt.rstrip(",.qsaw")
        # print(x) -> banan