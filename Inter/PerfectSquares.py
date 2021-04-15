# https://leetcode.com/problems/perfect-squares/
# Time: O(n)
# Space: O(n)

class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n

        lst = [] # this has all the square numbers that are smaller than n (so only these numbers can add up to make n)
        i = 1
        while i * i <= n:
            lst.append(i * i)
            i += 1

        ans = 0
        toCheck = {n} #set

        while toCheck:
            ans += 1
            nextToCheck = set()
            for checkNum in toCheck:
                for checker in lst: 
                    if checkNum - checker < 0: #lst is in ascending order, so if current checker yields negative, next will too, so break
                        break
                    if checkNum == checker:
                        return ans
                    nextToCheck.add(checkNum - checker)
                    
            toCheck = nextToCheck

        return ans