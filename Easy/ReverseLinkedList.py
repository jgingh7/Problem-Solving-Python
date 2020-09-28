# https://leetcode.com/problems/reverse-linked-list/solution/
# Time: O(length of list)
# Space: O(length of list). The extra space comes from implicit stack space due to recursion.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
    


# Time: O(length of list)
# Space: O(length of list). The extra space comes from implicit stack space due to recursion.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        p = self.reverseList(head.next) #this goes to the end of the linked list
        head.next.next = head #reverse the pointer
        head.next = None #cut the connection to the original next
        return p