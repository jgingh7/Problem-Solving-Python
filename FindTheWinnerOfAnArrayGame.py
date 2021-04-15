# https://leetcode.com/problems/find-the-winner-of-an-array-game/
# Time: O(n)
# Time: O(1)

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:       
        currWinner = arr[0]
        currK = k
        for i in range(1, len(arr)):
            if currWinner > arr[i]:
                currK -= 1
            else:
                currWinner = arr[i]
                currK = k - 1
                
            if currK == 0:
                return currWinner
        
        return currWinner # if iteration goes until len(arr) times, falls into infinite loop
                          # because the maximum number is on the most left