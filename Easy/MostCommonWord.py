# https://leetcode.com/problems/most-common-word/
# Time: O(n + m) - O(n) to make normalized_str, O(m) to make banned_words
# Space: O(n + m)

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #1). replace the punctuations with spaces,
        #      and put all letters in lower case
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        #2). split the string into words
        words = normalized_str.split()
        print(words)
        
        word_count = {}
        banned_words = set(banned)

        #3). count the appearance of each word, excluding the banned words
        for word in words:
            if word not in banned_words:
                word_count[word] = word_count.get(word, 0) + 1

        #4). return the word with the highest frequency
        return max(word_count, key=word_count.get)