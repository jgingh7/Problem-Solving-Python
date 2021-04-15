# https://leetcode.com/problems/word-break/


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for i in range(n + 1)]
        dp[0] = True # imaginary True put to give True for the first word in str consiting s[0] in wordDict

        for i in range(1, n + 1):
            for word in wordDict:
                if s[i - len(word): i] == word and dp[i - len(word)]: #if there is word in s
                                                                      #and the dp value just before this word is True
                                                                      #    (which means that there is a word that does not overlap w)
                                                                      #put True on do[i]
                    dp[i] = True

        return dp[-1] #just check the last of dp since if this is True, it means that words in wordDict composes s without overlaps