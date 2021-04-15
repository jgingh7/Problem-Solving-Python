# https://leetcode.com/problems/word-search/
# Time: O(mn * 4^len(word))   4^len(word): because you have four directions per choice
#                             There are mn starting positions for dfs, so mn*4^len(word)
# Space: O(mn + len(word))
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        startChar = word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == startChar:
                    if self.dfs(i, j, board, word, 0):
                        return True
        return False

                    
    def dfs(self, i: int, j: int, board: List[List[str]], word: str, k: int) -> bool:
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k]:
            return False

        if k == len(word) - 1: #if board[i][j] == word[k] and k is the last index of word, return True
            return True
        
        # to prevent dfs backwards
        temp = board[i][j]
        board[i][j] = "#"
            
        k += 1
        if self.dfs(i + 1, j, board, word, k) \
        or self.dfs(i - 1, j, board, word, k) \
        or self.dfs(i, j + 1, board, word, k) \
        or self.dfs(i, j - 1, board, word, k):
            board[i][j] = temp #put temp back since other dfs could go through this element
            return True
        else:
            board[i][j] = temp
            return False