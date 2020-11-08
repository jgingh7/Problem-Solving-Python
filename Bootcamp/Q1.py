def twoSum(nums: List[int], target: int) -> List{int}:
    dic = {} #here we append idxs of nums in nums

    for idx, num in enumerate(nums):
        otherNum = target - num
        if otherNum in dic: # O(1)
            return[dic[otherNum], num]
        else:
            dic[num] = idx


