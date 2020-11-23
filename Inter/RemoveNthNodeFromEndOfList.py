# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        before = dummy
        curr = front = head
        
        for i in range(n):
            front = front.next
            
        while front:
            front = front.next
            curr = curr.next
            before = before.next
        
        before.next = curr.next
        curr.next = None
        
        return dummy.next