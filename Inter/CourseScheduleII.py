# https://leetcode.com/problems/course-schedule-ii/
# Time: O(E + V)
# Space: O(E + V) - adjacency list

from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        stack = deque()
        visited = [False for x in range(numCourses)]
        G = defaultdict(list)
        # graph where prerequisites point to the course
        for pre in prerequisites:
            G[pre[1]].append(pre[0])
        
        #1. dfs through the graph
        #   stack in order of courses finishing dfs
        for num in range(numCourses):
            if visited[num] == False:
                self.dfs(stack, num, G, visited)
            
        #2. transpose the prerequisites
        for pre in prerequisites:
            pre[0], pre[1] = pre[1], pre[0]
        
        G = defaultdict(list) #reset G
        for pre in prerequisites:
            G[pre[1]].append(pre[0])
        
        visited = [False for x in range(numCourses)] #reset visited

        #3. dfs through the transpose in order of the stack
            #if dfs finds a course with a neighboring(prerequisite) course that has been visited, return False
            #if all courses did not have any neighboring(prerequisite) course to dfs to, return True
        ans = []
        while stack:
            currCourse = stack.pop()
            visited[currCourse] = True
            ans.append(currCourse)
            
            for neighbor in G[currCourse]:
                if visited[neighbor] == False:
                    return []
                
        return ans
            
        
    def dfs(self, stack, num, G, visited):
        visited[num] = True
        
        for neighbor in G[num]:
            if visited[neighbor] == False:
                self.dfs(stack, neighbor, G, visited)
        stack.append(num) #when all neighboring(prerequisite) courses have been visited, stack