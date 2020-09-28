#https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/797/
#Time: O(2^n * 2^m)
#Space: O(2^n * 2^m) : num of recursion stack 인듯 근데 O(nm)이라는 사람 좀 있음

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, board, word):
                        return True
        return False
    
    def dfs(self, i: int, j: int, board: List[List[str]], word: str) -> bool:
        print(word)
        if not word:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[0]:
            return False
        
        temp = board[i][j]
        board[i][j] = '0'
        
        if self.dfs(i + 1, j, board, word[1:]) or self.dfs(i - 1, j, board, word[1:]) \
        or self.dfs(i, j + 1, board, word[1:]) or self.dfs(i, j - 1, board, word[1:]):
            return True
        
        board[i][j] = temp
        return False