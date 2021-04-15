# https://leetcode.com/problems/count-good-meals/
# Time: O(n)
# Space: O(n)

from collections import Counter

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        countOfDeliciousness = Counter(deliciousness)
        ans = 0
        
        for point, num in reversed(sorted(countOfDeliciousness.items())): # need to reverse since this can enable each point to just deal with
                                                                          # one sum which is "powerOfTwoAbovePoint"
            if bin(point).count('1') == 1: # if is_power_of_two(point):
                pairsWithZeros = num * countOfDeliciousness[0]
                pairsOfThemselves = (num - 1) * num // 2
                ans += pairsWithZeros + pairsOfThemselves
                
            else:
                powerOfTwoAbovePoint = 2 ** (len(str(bin(point))) - 2) # -2 because binary is in the form of "0b..."                  
                ans += num * countOfDeliciousness[powerOfTwoAbovePoint - point]  
                
            countOfDeliciousness.pop(point)    
            
        return ans % (10 ** 9 + 7)