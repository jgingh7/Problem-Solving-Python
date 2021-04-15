# https://leetcode.com/problems/open-the-lock/
# Time: O(4^9)
# Space: O(4^9)

from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadend = set(deadends)
        
        if target in deadend or '0000' in deadend:
            return -1
        
        if target == '0000':
            return 0
        
        def getNextCombi(combi: str) -> List[str]:
            res = []
            for i in range(4):
                nextCombi1 = combi[:i] + str((int(combi[i:i + 1]) + 1) % 10) + combi[i + 1:]
                nextCombi2 = combi[:i] + str((int(combi[i:i + 1]) - 1) % 10) + combi[i + 1:]
                if nextCombi1 not in deadend:
                    res.append(nextCombi1)
                if nextCombi2 not in deadend:
                    res.append(nextCombi2)
            return res
        
        sourceQueue = deque(['0000'])
        targetQueue = deque([target])
        
        sourceSeen = {'0000': 0}
        targetSeen = {target: 0}
        
        while len(sourceQueue) != 0 and len(targetQueue) != 0:
            sourceCombi = sourceQueue.popleft()
            targetCombi = targetQueue.popleft()
            
            for nextCombi in getNextCombi(sourceCombi):
                if nextCombi not in sourceSeen:
                    sourceSeen[nextCombi] = sourceSeen[sourceCombi] + 1
                    sourceQueue.append(nextCombi)
                    if nextCombi in targetSeen:
                        return sourceSeen[nextCombi] + targetSeen[nextCombi]
            
            for nextCombi in getNextCombi(targetCombi):
                if nextCombi not in targetSeen:
                    targetSeen[nextCombi] = targetSeen[targetCombi] + 1
                    targetQueue.append(nextCombi)
                    if nextCombi in sourceSeen:
                        return sourceSeen[nextCombi] + targetSeen[nextCombi]
        
        return -1