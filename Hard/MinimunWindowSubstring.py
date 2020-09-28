# https://leetcode.com/problems/minimum-window-substring/

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

        required = len(tCounter)

        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filteredS = []
        for i, char in enumerate(s):
            if char in tCounter:
                filteredS.append((i, char))

        lFS, rFS = 0, 0
        formed = 0
        windowCounts = {}

        ans = (float("inf"), None, None)

        # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
        # Hence, we follow the sliding window approach on as small list.
        while rFS < len(filteredS):
            character = filteredS[rFS][1]
            windowCounts[character] = windowCounts.get(character, 0) + 1

            if windowCounts[character] == tCounter[character]:
                formed += 1 #fully formed when fromed == required

            # If the current fliter window has or more of the required frequency of each characters check for the length of the original window
            while formed == required:
                character = filteredS[lFS][1]

                # Save the smallest original window until now.
                start = filteredS[lFS][0]
                end = filteredS[rFS][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                windowCounts[character] -= 1
                if windowCounts[character] < tCounter[character]:
                    #if more still formed, but if less, take decrement 1, because not formed yet
                    formed -= 1
                lFS += 1    

            rFS += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]