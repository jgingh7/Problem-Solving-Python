# https://leetcode.com/problems/linked-list-in-binary-tree/
# Time: O(sizeOfTree * sizeOfLinkedList) - search in string
# Space: O(max(heightOfTree, sizeOfLinkedList))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        checker = ""
        while head:
            checker += str(head.val) + ','
            head = head.next
        
        def dfs(node, scanned):
            scanned += str(node.val) + ','
            if checker in scanned:
                return True
            
            if node.left:
                left = dfs(node.left, scanned)
                if left:
                    return True
            if node.right:
                right = dfs(node.right, scanned)
                if right:
                    return True
            
            return False
            
            
        ans = dfs(root, "")
        return ans