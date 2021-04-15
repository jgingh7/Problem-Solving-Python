# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode.com/problems/linked-list-cycle-ii/
# Time: O(n)
# Space: O(1)

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
     
        # 1. look for cycle
        slow = fast = head
        
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        # 2. get the starting point
        while slow != head:
            slow = slow.next
            head = head.next
            
        return slow
    
    #     ANS: dist head -> enterance
    #     MEET: dist enterance -> meet point
    #     CL: cycle's length
    #     SC: # of cycles slow goes through
    #     FC: # of cylces fast goes through

    #     slow traveled ANS + SC * L + MEET
    #     fast traveled ANS + FC * L + MEET

    #     Since fast traveled twice that of slow,
    #     2(ANS + SC * L + MEET) = ANS + FC * L + MEET
    #     or ANS = L(FC-2SC) - MEET

    #     Consider having slow to take ANS steps.
    #     This the steps taken will be the same as
    #     1) go back MEET steps
    #     2) and do (FC-2SC) loops in the cylce.
    #     This will make slow to end up in enterance.

    #     Therefore take head to go MEET steps, and also have slow take MEET steps.
    #     Both will meet at the enterance.
    
    
    #     interesting fact:
    #     for 1. even below works to look for cycles (if where slow ends up does not matter):

    #         while fast and fast.next and fast.next.next and fast.next.next.next:
    #             slow = slow.next
    #             fast = fast.next.next.next.next
    #             if slow == fast:
    #                 return break
    #         else:
    #             return None