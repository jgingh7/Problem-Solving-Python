# https://leetcode.com/problems/merge-k-sorted-lists/
# Time: O(number nodes log len(lists)) - the while loop
# Space: O(len(lists)) - initial heap size

import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(head.val, linkedListID, head) for linkedListID, head in enumerate(lists) if head] #O(len(lists))
        # Python3 env will get TypeError: '<' not supported between instances of 'ListNode' and 'ListNode' if there are duplicate values in the list when making into heap.
        # so need to put linkedLisstID
        
        heapq.heapify(heap) # makes into minheap # 
        dummy = curr = ListNode(0)
 
        while heap:
            _, linkedListID, node = heap[0] # get the root of min-heap
            if node.next:
                heapq.heapreplace(heap, (node.next.val, linkedListID, node.next)) #pop-push
            else: # if a linked list is exhausted, no pushing
                heapq.heappop(heap)
                
            curr.next = node #curr.next is the current iteration's node
            curr = curr.next #the next curr is curr.next
            
        return dummy.next