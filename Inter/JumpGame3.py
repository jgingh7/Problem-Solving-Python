# https://leetcode.com/problems/jump-game-iii/
# Time: O(n)
# Space: O(n)

class Solution: #BFS solution
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = [start]
        
        while q:
            node = q.pop()
            if arr[node] == 0:
                return True
            if arr[node] < 0: #if visited already, don't need to look
                continue
                
            for i in [node + arr[node], node - arr[node]]:
                if 0<= i < n:
                    q.append(i) #append the possible positions that can be reached
                                #the positions are all checked 
            
            arr[node] = -arr[node] #mark as visited
        
        return False #return false if there are no more qs (no more indices that can be reached)
                     #and 0 was still not reached


class Solution: #DFS solution
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0<= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True
            
            arr[start] = -arr[start] #mark as visited
            return self.canReach(arr, start - arr[start]) or self.canReach(arr, start + arr[start])
        
        return False #False if start goes out of range or lands on visited index
                     #so if the recursion returns False for both sides, the answer is False.