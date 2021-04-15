# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# Time: O(n)
# SpaceL O(1)

# odd[i] records the number of subarray ending at arr[i] that has odd sum.
# even[i] records the number of subarray ending at arr[i] that has even sum.

# ALGO
# if arr[i](currently added num) is even:
#   even[i] = even[i - 1] + 1 -> In order to get even[i] actual subarrays, you add arr[i] to even[i - 1] actaul subarrays. (even + even = even)
#                                The count stays the same for even[i - 1] and even[i].
#                                Then you add 1 to count for stand-alone subarray of [arr[i]].
#   odd[i] = odd[i - 1] -> In order to get odd[i] actual subarrays, you add arr[i] to odd[i - 1] actaul subarrays. (odd + even = odd)
#                          The count stays the same for odd[i - 1] and odd[i].

# if arr[i](currently added num) is odd:
#   even[i] = odd[i - 1] -> In order to get even[i] actual subarrays, you add arr[i] to odd[i - 1] actaul subarrays. (odd + odd = even)
#                           The count stays the same for odd[i - 1] and even[i].
#   odd[i] = even[i - 1] + 1 -> In order to get odd[i] actual subarrays, you add arr[i] to even[i - 1] actaul subarrays. (even + odd = odd)
#                               The count stays the same for even[i - 1] and odd[i].
#                               Then you add 1 to count for stand-alone subarray of [arr[i]].


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int: 
        ans = odd = even = 0
        for element in arr:
            if element % 2 == 0:
                even += 1
            else:
                even, odd = odd, even + 1
            ans += odd
        return ans % (10 ** 9 + 7)