#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/
#Time: O(n)
#Space: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return nlargest(k, count.keys(), key = count.get)
        # Return a list with the n largest elements from the dataset defined by iterable.