# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/add-two-numbers/submissions/
# Time: O(n)
# Space: O(n)

from collections import deque

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = deque()
        stack2 = deque()
        ansStack = deque()
        
        # 1. make stacks of numbers
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        # 2. make stack to make the answer ListNode
        addOne = False
        while stack1 or stack2:
            curr1 = curr2 = 0
            if stack1:
                curr1 = stack1.popleft()
            if stack2:
                curr2 = stack2.popleft()
            
            currSum = curr1 + curr2
            if addOne:
                currSum += 1
            
            if currSum >= 10:
                addOne = True
                currSum -= 10
            else:
                addOne = False
            
            ansStack.append(currSum)
            
        if addOne:
            ansStack.append(1)
        
        # 3. make the answer ListNode
        ans = None
        while ansStack:
            newNode = ListNode()
            newNode.val = ansStack.pop()
            newNode.next = ans
            ans = newNode
        
        return ans