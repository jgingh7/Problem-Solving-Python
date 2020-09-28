#https://leetcode.com/problems/binary-tree-inorder-traversal/solution/
#Time: O(n)
#Space: O(n), it will be O(1) if not count the ans


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        curr = root
        ans = []
        
        while curr != None:
            if curr.left == None:
                ans.append(curr.val)
                curr = curr.right
            else:
                rightMost = curr.left
                nextTop = curr.left
                while rightMost.right != None:
                    rightMost = rightMost.right
                
                rightMost.right = curr
                curr.left = None
                curr = nextTop
            
        return ans


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right