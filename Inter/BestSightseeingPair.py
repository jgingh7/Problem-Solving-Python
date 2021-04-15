# https://leetcode.com/problems/best-sightseeing-pair/
# Time: O(n)
# Space: O(1)

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # max this -> values[i] + values[j] + dist(i, j)
        
        valueIminusDist = res = 0
        for valueJ in values:
            currMax = max(currMax, valueIminusDist + valueJ)
            valueIminusDist = max(valueIminusDist, valueJ) - 1 # gets the best (values[i] - dist(i, j))
                                                               # so that on the next iteration,
                                                               # best(values[i] - dist(i, jJustBefore)) + values[j] can be compared with currMax
        return currMax
    
    
# [8,1,5,2,6]
    
# res 8 (best)
# curr 7 (next best: (8 - 1 + nextValue) will be compared with the current res)
# =====
# res 8 (best)
# curr 6 (next best: (8 - 2 + nextValue) will be compared with the current res)
# =====
# res 11 (best)
# curr 5 (next best: (8 - 3 + nextValue) will be compared with the current res)
# =====
# res 11 (best)
# curr 4 (next best: (8 - 4 + nextValue) will be compared with the current res)
# =====
# res 11 (best)
# curr 5 (next best: (6 - 1 + nextValue) will be compared with the current res)
# =====