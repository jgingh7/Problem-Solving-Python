# https://leetcode.com/problems/minimum-window-substring/solution/
# Time: O(S + T)
# Space: O(S + T)

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        tCounter = Counter(t)

        l = formedCharCount = 0
        requiredCharCount = len(tCounter)
        windowCounts = {}

        impossibleLenOfSub = len(s) + 1
        ans = (impossibleLenOfSub, None, None)

        for r, charR in enumerate(s):
            windowCounts[charR] = windowCounts.get(charR, 0) + 1

            # increment only when the charR's count in the window is the same as string t's count
            if windowCounts[charR] == tCounter[charR]:
                formedCharCount += 1

            # the right above "if" statement makes the instance to enter while loop only when
            # 1. the window's character counts are exactly the same as string t's character counts
            # 2. or when one or more character's count in the window is more than character's count in string t
            while formedCharCount == requiredCharCount:

                # Save the smallest window until checking through current index r
                currWindLen = r - l + 1
                if currWindLen < ans[0]:
                    ans = (currWindLen, l, r)

                # take the leftmost char out, decreasing the window size
                charL = s[l]
                windowCounts[charL] -= 1
                l += 1

                # After taking a char out from the left, check if formedCharCount should change.
                # If count of charL is larger or equal, do not change formedCharCount
                # so that we can keep the inner while loop working to get a smaller window substring, before increasing index r.
                # If formedCharCount should change, it means we need to further increase index r to further check string s
                # to find the character that can make a window with all characters in string t.
                # Therefore so we break out of inner while loop by decrementing foremdCharCount
                if windowCounts[charL] < tCounter[charL]:
                    formedCharCount -= 1

        return "" if ans[0] == impossibleLenOfSub else s[ans[1]: ans[2] + 1]