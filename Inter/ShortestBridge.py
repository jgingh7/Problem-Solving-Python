# https://leetcode.com/problems/shortest-bridge/
# Time: O(len(A)^2) - dfs if the first island size is len(A)^2 - 4
# Space: O(len(A)^2) - bfsQueue if the first island size is len(A)^2 - 4

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < n and 0 <= j < n and A[i][j] == 1:
                A[i][j] = -1
                bfsQueue.append((i, j))
                
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)
        
        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j

        n = len(A)
        bfsQueue = deque()
        dfs(*first()) #find some point of an island, and dfs starting from that point and make all to -1
                      # append all the indices of the island to bfsQueue

        step = 0
        levelCounter = len(bfsQueue)
        while bfsQueue: # bfs each point of first island
            i, j = bfsQueue.popleft()

            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nextI = i + x
                nextJ = j + y
                if 0 <= nextI < n and 0 <= nextJ < n:
                    if A[nextI][nextJ] == 1:
                        return step
                    elif A[nextI][nextJ] == 0:
                        A[nextI][nextJ] = -1
                        bfsQueue.append((nextI, nextJ))

            levelCounter -= 1
            if levelCounter == 0:
                step += 1
                levelCounter = len(bfsQueue)