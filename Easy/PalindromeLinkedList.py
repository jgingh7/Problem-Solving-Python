# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
# Time: O(length of head / 2)
# Space: O(1)

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse the second half
        prev = None
        while slow:
            nextSlowNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextSlowNode
            
        # compare the first and second half nodes
        while prev: # while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            
        return True