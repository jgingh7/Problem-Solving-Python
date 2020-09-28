# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/832/
# Time: O(nlogn) - sorting
# Space: O(1)


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        
        # find the index where positive numbers start
        i = 0
        for element in nums:
            if element <= 0:
                i += 1

        # if i is outofbound of nums, or if the first positive number is not 1,
        # 1 is the smallest missing positive
        if len(nums) == i or nums[i] != 1:
            return 1

        for j in range(i, len(nums) - 1):
            # if the current number is 1 less than the next number, or if is same as the next number,
            # keep iterating
            if nums[j] == nums[j + 1] - 1 or nums[j] == nums[j + 1]:
                continue
            #else the next number of current number is the answer
            else:
                return nums[j] + 1
            
        # if the numbers do not have missing positive in between, return the number 1 more than the last number
        return nums[-1] + 1