# Just need to get the maximum counted num, because majority's frequency is bigger than floor(n/2), so no num can have frequency that is be bigger or equal to that num
# Time: O(n)
# Space: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max(counts.keys(), key = counts.get)

# Counter: dict subclass for counting hashable objects
# if nums = [2,2,1,1,1,2,2], counts = Counter({2: 4, 1: 3}) <- can be treated as dict
# counts.keys = dict_keys([2, 1]) <- can be treated as unordered collection (still not list)

# a_dictionary = {"a": 1, "b": 2, "c": 3}
# max_key = max(a_dictionary, key=a_dictionary.get)
# print(max_key) -> c