# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
# Time: O(length of l1 + length of l2)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode(0) #the curr keeps moving, dummy stays
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1 #curr's next value is the smaller one
                l1 = l1.next #move l1 if taken by curr
            else:
                curr.next = l2 #curr's next value is the smaller one (or same one)
                l2 = l2.next #move l2 if taken by curr
            curr = curr.next #follow where curr is pointing to
        curr.next = l1 or l2 #curr.next = l1 if l1 else l2  #if l1 or l2 becomes None, cannot evaluate the val. so the non-None node becomes the end Node
        return dummy.next
                