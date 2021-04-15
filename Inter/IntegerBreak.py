# https://leetcode.com/problems/integer-break/
# Time: O(log(n)) - power function takes O(log(exponent)) time
# Space: O(1)

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        threeCount = int(n/3)
        
        remainingMultiplier = n % 3
        
        if remainingMultiplier == 0:
            return 3 ** threeCount
        
        if remainingMultiplier == 1: # we can make up a 4 by not using one 3 and using a 4
            threeCount -= 1
            remainingMultiplier = 4
            
        #else remainingMultiplier will be 2 which is okay to use
        
        return (3 ** threeCount) * remainingMultiplier
    
    # If n is divided into 2 factors, it will have a maximized mutiplication
    # when (n/2)(n/2) for even
    # and ((n+1)/2)((n-1)/2) for odd.
    # (you can proved this by doing a derivation on x(n-x)=multiple)
    
    # If n > 4, it can be divided into 2 factors with a higher multiplication than itself.
    # If 5, 3*2 = 6.
    # If 6, 3*3 = 9
    # So only 1,2,3 is needed to be factors, but obviously 1 is useless to maximize a multiplication,
    # so only factorize down to 2 and/or 3.

    # If n == 4, yes 2*2 is the same as 4 so you can keep 4.
    # However, you can convince yourself that by having the number divided into 3 at most,
    # and then check if a 4 is needed is the best choice.
    # This can be explained more detailed on the next paragraph.
    
    # Why use most of 3 rather than 2?
    # If we factor down to get a factor of 6, 3*3=9 is bigger than 2*2*2=6.
    # so whenever you get to three 2s, it is better to use two 3s.
    # The maximum number of 2s you want to have is two.
        
    # It is only when n == 2 that we use two 1s,
    # and only when n == 3 that we use one 1 and one 2.