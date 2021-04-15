# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Time: O(logn) per each add, O(nlogn) for init
# Space: O(n) - heap

import heapq

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        
        while len(self.nums) > k: #keep answer on root
            heapq.heappop(self.nums)
        
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappushpop(self.nums, val)
            
        return self.nums[0] #return root
                
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)