# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/submissions/
# Time: O(n) - length of s
# Space: O(nk) - set of length n, and each string with k length

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # make an int need which is the number of all possible permutations
        need = 2 ** k
        permute = set()

        # check if curr is not in permute
        # if not, this means curr is a new permutation, so decrement need
        # if need becomes 0, it means all possible permutations have occured, so return True

        # keep adding curr to get all permutations in s
        for i in range(0, len(s) - k + 1):
            curr = s[i:i+k]
            if curr not in permute:
                need -= 1
                if need == 0:
                    return True
            permute.add(curr)

        # if at the end need does not reach 0, return False
        return False
