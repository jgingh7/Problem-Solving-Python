# https://leetcode.com/problems/subarray-sum-equals-k/
# Time: O(n)
# Space: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = summation = 0
        d = {} #use hashmap in case of encountering 0
        d[0] = 1
        for num in nums:
            summation += num 
            if (summation - k) in d: #the hashmap having (summation - k) implies that
                                     #from (summation - k), which is also a summation of continuous nums elements that existed before,
                                     #to the current num, the summation in between has been added up to k.
                                     #therefore we increment count by 1 (most probably).
                                     #the count can be more than 1 beause say you have [0,4,3].
                                     #when you reach 3, 2 should be incremented
                count += d[summation - k]
            d[summation] = d.get(summation, 0) + 1
            
        return count