# https://leetcode.com/problems/course-schedule/
# Time: O(E + V)

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        stack = deque()
        visited = [False for x in range(numCourses)]
        directions = defaultdict(list)
        for pre in prerequisites:
            directions[pre[0]].append(pre[1])
        
        #1. dfs through the graph
        #   stack in order of courses finishing dfs
        for num in range(numCourses):
            if visited[num] == False:
                self.dfs(stack, num, directions, visited)
            
        #2. transpose the prerequisites
        for pre in prerequisites:
            pre[0], pre[1] = pre[1], pre[0]
        
        directions = defaultdict(list) #reset directions
        for pre in prerequisites:
            directions[pre[0]].append(pre[1])
        
        visited = [False for x in range(numCourses)] #reset visited

        #3. dfs through the transpose in order of the stack
            #if current course has no neighboring(prerequisite) courses, continue the while loop
            #if dfs finds a course with a neighboring(prerequisite) course that has been visited, return False
            #if all courses did not have any neighboring(prerequisite) course to dfs to, return True
        while stack:
            currCourse = stack.pop()
            visited[currCourse] = True
            
            if currCourse not in directions:
                continue
            
            for neighbor in directions[currCourse]:
                if visited[neighbor] == False:
                    return False
                
        return True
    
    
    def dfs(self, stack, num, directions, visited):
        visited[num] = True
        
        if num not in directions: #if no neighboring(prerequisite) courses, return
            stack.append(num)
            return
        
        for neighbor in directions[num]:
            if visited[neighbor] == False:
                self.dfs(stack, neighbor, directions, visited)
        stack.append(num) #when all neighboring(prerequisite) courses have been visited, stack