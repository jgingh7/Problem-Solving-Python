# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/837/
# Time: O(n) the popping in while loop is done at most n(len(nums)) times.
# Space: O(n) the maximum size of deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        bigger = deque()
        for i, n in enumerate(nums):
            # make sure the rightmost one is the smallest
            # make all the numbers smaller than n to be popped
            while bigger and nums[bigger[-1]] <= n:
                bigger.pop()

            # add in
            bigger += [i]
            print(bigger)

            # make sure the leftmost one is in-bound
            if i - bigger[0] >= k:
                bigger.popleft()

            # if i + 1 < k, then we are initializing the bigger array
            # append when the rightmost is decided for current window
            if i + 1 >= k:
                res.append(nums[bigger[0]])
        return res