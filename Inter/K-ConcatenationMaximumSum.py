# https://leetcode.com/problems/k-concatenation-maximum-sum/
# Time: O(n)
# Space: O(1)

class Solution:       
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        def Kadane(arr: List[int]): #Kadane's algo
            res = curr = 0
            for num in arr:
                curr = max(num, num + curr) # maximum sub-array sum ending at num
                res = max(res, curr)
            return res
        
        ans = (k - 2) * max(sum(arr), 0) + Kadane(arr * 2) if k > 1 else Kadane(arr)
        return ans % (10 ** 9 + 7)
    
    
    # "all minus in arr" is taken care of by "max(sum(arr), 0)""
    # "arr sum is minus" is taken care of by "max(sum(arr), 0) "
    
    # what if max at only once in the boundary part? is take care of by "Kadane(arr * 2)"
    # this not only handles cases where two ends are needed, -> (k - 2) * sum(arr) + Kadane(arr * 2)
      # 100, -1, -2, -5,  100, -1, -2, -5,  100, -1, -2, -5,  100, -1, -2, -5
    # but also when the boundary part is the answer  -> 0 + Kadane(arr * 2)
      # 100, -1000, -2000, 5,  100, -1000, -2000, 5,  100, -1000, -2000, 5,  100, -1000, -2000, 5
    # if Kadane(arr * 2) does not cross the boundary, then Kadane(arr * 2) == Kadane(arr)
      # 100, -1000, -2000, -5,  100, -1000, -2000, -5,  100, -1000, -2000, -5,  100, -1000, -2000, -5